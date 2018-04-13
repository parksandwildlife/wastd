# -*- coding: utf-8 -*-
"""Conservation models."""
from __future__ import unicode_literals, absolute_import

# import itertools
# import urllib
# import slugify
# from datetime import timedelta
# from dateutil import tz
import logging

from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
# from django.contrib.gis.db import models as geo_models
# from django.contrib.gis.db.models.query import GeoQuerySet
# from django.core.urlresolvers import reverse
# from rest_framework.reverse import reverse as rest_reverse
# from django.template import loader
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# from django.utils.safestring import mark_safe

# from polymorphic.models import PolymorphicModel
# from durationfield.db.models.fields.duration import DurationField
# from django.db.models.fields import DurationField
from django_fsm import FSMIntegerField, transition
from django_fsm_log.decorators import fsm_log_by
# from django_fsm_log.models import StateLog

from taxonomy.models import Taxon, Community
from wastd.users.models import User

logger = logging.getLogger(__name__)


def fileattachment_media(instance, filename):
    """Return an upload path for fileattachment media."""
    return 'attachment/{0}/{1}/{2}'.format(instance.content_type, instance.object_id, filename)


@python_2_unicode_compatible
class FileAttachment(models.Model):
    """A generic file attachment to any model."""

    attachment = models.FileField(upload_to=fileattachment_media)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    title = models.CharField(
        blank=True, null=True,
        max_length=500,
        verbose_name=_("Title"),
        help_text=_("A self-explanatory title for the file attachment."))
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        blank=True, null=True,
        help_text=_("The person who authored and endorsed this file."))

    def __str__(self):
        """The full name."""
        return "{0} {1}".format(self.title, self.author)


@python_2_unicode_compatible
class ConservationList(models.Model):
    """A Conservation List like BCA, EPBC, RedList."""

    APPROVAL_IMMEDIATE = 10
    APPROVAL_PANEL = 20
    APPROVAL_MINISTER = 30

    APPROVAL_LEVELS = (
        (APPROVAL_IMMEDIATE, 'Immediate'),
        (APPROVAL_PANEL, 'Panel'),
        (APPROVAL_MINISTER, 'Minister'),
    )

    code = models.CharField(
        max_length=500,
        unique=True,
        verbose_name=_("Code"),
        help_text=_("A Conservation List code."),
    )

    label = models.CharField(
        blank=True, null=True,
        max_length=500,
        verbose_name=_("Label"),
        help_text=_("An explanatory label."),
    )

    description = models.TextField(
        blank=True, null=True,
        verbose_name=_("Description"),
        help_text=_("A comprehensive description."),
    )

    active_from = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_("Active from"),
        help_text=_("The date and time from which this list is current."),
    )

    active_to = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_("Active to"),
        help_text=_("The date and time from which this list is non-current."),
    )

    scope_wa = models.BooleanField(
        db_index=True,
        default=False,
        verbose_name=_("Applies to WA"),
        help_text=_("Whether this list is applicable state-wide."),
    )

    scope_cmw = models.BooleanField(
        db_index=True,
        default=False,
        verbose_name=_("Applies to Commonwealth"),
        help_text=_("Whether this list is applicable nation-wide."),
    )

    scope_intl = models.BooleanField(
        db_index=True,
        default=False,
        verbose_name=_("Applies Internationally"),
        help_text=_("Whether this list is applicable internationally."),
    )

    scope_species = models.BooleanField(
        db_index=True,
        default=False,
        verbose_name=_("Applies to Species"),
        help_text=_("Whether this list is applicable to individual species."),
    )

    scope_communities = models.BooleanField(
        db_index=True,
        default=False,
        verbose_name=_("Applies to Communities"),
        help_text=_("Whether this list is applicable to ecological communities."),
    )

    approval_level = models.PositiveIntegerField(
        verbose_name=_("Approval Level"),
        default=APPROVAL_MINISTER,
        choices=APPROVAL_LEVELS,
        help_text=_("What is the highest required approval instance for this list?"), )

    class Meta:
        """Class opts."""

        verbose_name = "Conservation List"
        verbose_name_plural = "Conservation Lists"
        ordering = ["-active_from", ]

    def __str__(self):
        """The full name."""
        return self.code


@python_2_unicode_compatible
class ConservationCategory(models.Model):
    """A Conservation Category like CR, EN, VU."""

    conservation_list = models.ForeignKey(
        ConservationList,
        verbose_name=_("Conservation List"),
        help_text=_("The conservation list this code is described in."),
    )

    code = models.CharField(
        max_length=500,
        verbose_name=_("Code"),
        help_text=_("A category code, unique within its conservation list."),
    )

    label = models.CharField(
        blank=True, null=True,
        max_length=500,
        verbose_name=_("Label"),
        help_text=_("An explanatory label."),
    )

    description = models.TextField(
        blank=True, null=True,
        verbose_name=_("Description"),
        help_text=_("A comprehensive description."),
    )

    rank = models.PositiveIntegerField(
        verbose_name=_("Rank"),
        blank=True, null=True,
        help_text=_("Display order, lowest number goes first."), )

    class Meta:
        """Class opts."""

        unique_together = ("conservation_list", "code")
        ordering = ["conservation_list", "rank"]
        verbose_name = "Conservation Category"
        verbose_name_plural = "Conservation Categories"

    def __str__(self):
        """The full name."""
        return "[{0}] {1}".format(self.conservation_list.code, self.code)


@python_2_unicode_compatible
class ConservationCriterion(models.Model):
    """A Conservation Criterion like A4a."""

    conservation_list = models.ForeignKey(
        ConservationList,
        verbose_name=_("Conservation List"),
        help_text=_("The conservation list this code is described in."),
    )

    code = models.CharField(
        max_length=500,
        verbose_name=_("Code"),
        help_text=_("A criterion code, unique within its conservation list."),
    )

    label = models.CharField(
        blank=True, null=True,
        max_length=500,
        verbose_name=_("Label"),
        help_text=_("An explanatory label."),
    )

    description = models.TextField(
        blank=True, null=True,
        verbose_name=_("Description"),
        help_text=_("A comprehensive description."),
    )

    rank = models.PositiveIntegerField(
        verbose_name=_("Rank"),
        blank=True, null=True,
        help_text=_("Display order, lowest number goes first."), )

    class Meta:
        """Class opts."""

        unique_together = ("conservation_list", "code")
        ordering = ["conservation_list", "rank"]
        verbose_name = "Conservation Criterion"
        verbose_name_plural = "Conservation Criteria"

    def __str__(self):
        """The full name."""
        return "[{0}] {1}".format(self.conservation_list.code, self.code)


@python_2_unicode_compatible
class Gazettal(models.Model):
    """The allocation of a ConservationCategory.

    Approval state is tracked as django-fsm field.
    ConservationCategory can change during approval process.
    Inheritance can override transitions.

    Documents are attached as MediaAttachments.

    Some conservation categories are mutually exclusiver than others.
    To prevent invalid combinations of ConservationCategories,
    the transition to Gazettal.STATUS_GAZETTED must take care of
    closing just the mutually exclusive ones.
    """

    STATUS_PROPOSED = 0
    STATUS_IN_EXPERT_REVIEW = 10
    STATUS_IN_PUBLIC_REVIEW = 20
    STATUS_IN_PANEL_REVIEW = 30
    STATUS_IN_BM_REVIEW = 40
    STATUS_IN_DIR_REVIEW = 50
    STATUS_IN_DG_REVIEW = 60
    STATUS_IN_MIN_REVIEW = 70
    STATUS_GAZETTED = 80
    STATUS_DELISTED = 90

    APPROVAL_STATUS = (
        (STATUS_PROPOSED, "Proposed"),
        (STATUS_IN_EXPERT_REVIEW, "In review with experts"),
        (STATUS_IN_PUBLIC_REVIEW, "In review with public"),
        (STATUS_IN_PANEL_REVIEW, "In review with panel"),
        (STATUS_IN_BM_REVIEW, "In review with Branch Manager"),
        (STATUS_IN_DIR_REVIEW, "In review with Division Director"),
        (STATUS_IN_DG_REVIEW, "In review with Director General"),
        (STATUS_IN_MIN_REVIEW, "In review with Minister"),
        (STATUS_GAZETTED, "Gazetted"),
        (STATUS_DELISTED, "De-listed"),
    )

    SOURCE_MANUAL_ENTRY = 0
    SOURCE_THREATENED_FAUNA = 1
    SOURCE_THREATENED_FLORA = 2
    SOURCE_THREATENED_COMMUNITIES = 3

    SOURCES = (
        (SOURCE_MANUAL_ENTRY, 'Manual entry'),
        (SOURCE_THREATENED_FAUNA, 'Threatened Fauna'),
        (SOURCE_THREATENED_FLORA, 'Threatened Flora'),
        (SOURCE_THREATENED_COMMUNITIES, 'Threatened Communities'),
    )

    SCOPE_WESTERN_AUSTRALIA = 0
    SCOPE_COMMONWEALTH = 1
    SCOPE_INTERNATIONAL = 2
    SCOPE_ACTION_PLAN = 3

    SCOPES = (
        (SCOPE_WESTERN_AUSTRALIA, 'WA'),
        (SCOPE_COMMONWEALTH, 'CMW'),
        (SCOPE_INTERNATIONAL, 'INT'),
        (SCOPE_ACTION_PLAN, 'AP'),
    )

    source = models.PositiveIntegerField(
        verbose_name=_("Data Source"),
        default=SOURCE_MANUAL_ENTRY,
        choices=SOURCES,
        help_text=_("Where was this record captured initially?"), )

    source_id = models.CharField(
        max_length=1000,
        blank=True, null=True,
        verbose_name=_("Source ID"),
        help_text=_("The ID of the record in the original source, if available."), )

    scope = models.PositiveIntegerField(
        verbose_name=_("Scope"),
        default=SCOPE_WESTERN_AUSTRALIA,
        choices=SCOPES,
        help_text=_("In which legislation does this Gazettal apply?"), )

    # Conservation status
    category = models.ManyToManyField(
        ConservationCategory,
        blank=True,
        verbose_name=_("Conservation Categories"),
        help_text=_("The Conservation Categories can change during the approval process."
                    " Some combinations are valid, some are not."),
    )

    criteria = models.ManyToManyField(
        ConservationCriterion,
        blank=True,
        verbose_name=_("Conservation Criteria"),
        help_text=_("The Conservation Criteria form the reason "
                    "for the choice of conservation categories."),
    )

    # Approval status
    status = FSMIntegerField(
        choices=APPROVAL_STATUS,
        default=STATUS_PROPOSED,
        db_index=True,
        verbose_name=_("Approval status"),
        help_text=_("The approval status of the Gazettal."),
    )

    # Approval milestones
    proposed_on = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_("Proposed on"),
        help_text=_("The date and time this Gazettal was proposed on."),
    )

    gazetted_on = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_("Gazetted on"),
        help_text=_("The date and time this Gazettal was gazetted on."),
    )

    delisted_on = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_("De-listed on"),
        help_text=_("The date and time this Gazettal was de-listed, most likely superseded by another Gazettal."),
    )

    review_due = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_("Review due date"),
        help_text=_("The date and time this Gazettal should be reviewed."),
    )

    # Approval process log
    comments = models.TextField(
        blank=True, null=True,
        verbose_name=_("Comments"),
        help_text=_("Append comments on approval process as appropriate."),
    )

    # Cache fields
    category_cache = models.TextField(
        blank=True, null=True,
        verbose_name=_("Category list"),
        help_text=_("An auto-generated list of conservation categories."),
    )

    criteria_cache = models.TextField(
        blank=True, null=True,
        verbose_name=_("Criteria list"),
        help_text=_("An auto-generated list of conservation criteria."),
    )

    label_cache = models.TextField(
        blank=True, null=True,
        verbose_name=_("Gazettal label"),
        help_text=_("An auto-generated label for the Gazettal minus the Taxon."),
    )

    class Meta:
        """Class opts."""

        abstract = True

    def __str__(self):
        """The full name."""
        return unicode(self.pk)

    @property
    def build_category_cache(self):
        """Build a string of all attached categories."""
        return ", ".join([c.__str__() for c in self.category.all()])

    @property
    def build_criteria_cache(self):
        """Build a string of all attached criteria."""
        return ", ".join([c.code for c in self.criteria.all()])

    @property
    def build_label_cache(self):
        """Return the category and criteria cache."""
        return "{0} {1} {2}".format(
            self.get_scope_display(),
            self.build_category_cache,
            self.build_criteria_cache
        ).strip()

    @property
    def absolute_admin_url(self):
        """Return the absolute admin change URL."""
        return reverse('admin:{0}_{1}_change'.format(
            self._meta.app_label, self._meta.model_name), args=[self.pk])

    @property
    def absolute_admin_add_url(self):
        """Return the absolute admin add URL."""
        return reverse('admin:{0}_{1}_add'.format(
            self._meta.app_label, self._meta.model_name))

    @property
    def max_approval_level(self):
        """Return the highest required approval level of all categories."""
        return max([c.conservation_list.approval_level
                    for c in self.category.all()])

    # ------------------------------------------------------------------------#
    # Django-FSM transitions
    # recall_to_proposed = 0
    # STATUS_IN_EXPERT_REVIEW = 10
    # STATUS_IN_PUBLIC_REVIEW = 20
    # STATUS_IN_PANEL_REVIEW = 30
    # STATUS_IN_BM_REVIEW = 40
    # STATUS_IN_DIR_REVIEW = 50
    # STATUS_IN_DG_REVIEW = 60
    # STATUS_IN_MIN_REVIEW = 70
    # STATUS_GAZETTED = 80
    # STATUS_DELISTED = 90

    # ALL -> STATUS_PROPOSED -------------------------------------------------#
    def can_recall_to_proposed(self):
        """Allow always to reset to the initial status."""
        return True

    @fsm_log_by
    @transition(
        field=status,
        source=[STATUS_IN_EXPERT_REVIEW,
                STATUS_IN_PUBLIC_REVIEW,
                STATUS_IN_PANEL_REVIEW,
                STATUS_IN_BM_REVIEW,
                STATUS_IN_DIR_REVIEW,
                STATUS_IN_DG_REVIEW,
                STATUS_IN_MIN_REVIEW,
                STATUS_GAZETTED,
                STATUS_DELISTED],
        target=STATUS_PROPOSED,
        conditions=[can_recall_to_proposed],
        # permission='conservation.can_recall_to_proposed'
    )
    def recall_to_proposed(self):
        """Reset a new Gazettal to status "new" (proposed).

        This transition allows to reset any Gazettal to status "new"
        (before any endorsement) to start over freshly.
        This operation is equivalent to starting a new Gazettal.

        Source: all but STATUS_PROPOSED
        Target: STATUS_PROPOSED
        Permissions: staff
        Gatecheck: can_recall_to_proposed (pass)
        """
        logger.info("[Gazettal status] recall_to_proposed")

    # STATUS_PROPOSED -> STATUS_IN_EXPERT_REVIEW -----------------------------#
    def can_submit_for_expert_review(self):
        """Require if any categories are of min approval level APPROVAL_PANEL."""
        return self.max_approval_level >= ConservationList.APPROVAL_PANEL

    @fsm_log_by
    @transition(
        field=status,
        source=STATUS_PROPOSED,
        target=STATUS_IN_EXPERT_REVIEW,
        conditions=[can_submit_for_expert_review],
        # permission='conservation.can_submit_for_expert_review'
    )
    def submit_for_expert_review(self):
        """Submit a new Gazettal for expert review.

        Source: STATUS_PROPOSED
        Target: STATUS_IN_EXPERT_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires panel approval
        """
        logger.info("[Gazettal status] submit_for_expert_review")

    # PROPOSED / IN_EXPERT_REVIEW -> STATUS_IN_PUBLIC_REVIEW -----------------#
    def can_submit_for_public_review(self):
        """Only categories of max approval level APPROVAL_PANEL require this step."""
        return self.max_approval_level >= ConservationList.APPROVAL_PANEL

    @fsm_log_by
    @transition(
        field=status,
        source=[STATUS_PROPOSED, STATUS_IN_EXPERT_REVIEW],
        target=STATUS_IN_PUBLIC_REVIEW,
        conditions=[can_submit_for_public_review],
        # permission='conservation.can_submit_for_expert_review'
    )
    def submit_for_public_review(self):
        """Submit a new Gazettal for public review.

        Source: STATUS_PROPOSED, STATUS_IN_EXPERT_REVIEW
        Target: STATUS_IN_PUBLIC_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires panel approval
        """
        logger.info("[Gazettal status] submit_for_public_review")

    # STATUS_PROPOSED, STATUS_IN_EXPERT_REVIEW, STATUS_IN_PUBLIC_REVIEW ->
    # STATUS_IN_PANEL_REVIEW  ------------------------------------------------#
    def can_submit_for_panel_review(self):
        """Only categories of max approval level APPROVAL_PANEL require this step."""
        return self.max_approval_level >= ConservationList.APPROVAL_PANEL

    @fsm_log_by
    @transition(
        field=status,
        source=[STATUS_PROPOSED, STATUS_IN_EXPERT_REVIEW, STATUS_IN_PUBLIC_REVIEW],
        target=STATUS_IN_PANEL_REVIEW,
        conditions=[can_submit_for_panel_review],
        # permission='conservation.can_submit_for_panel_review'
    )
    def submit_for_panel_review(self):
        """Submit a new Gazettal for panel review.

        A proposed review can optionally go to an expert, to the public,
        or go directly for panel review.

        Source: STATUS_PROPOSED, STATUS_IN_EXPERT_REVIEW, STATUS_IN_PUBLIC_REVIEW
        Target: STATUS_IN_PANEL_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires panel approval
        """
        logger.info("[Gazettal status] submit_for_panel_review")

    # STATUS_IN_PANEL_REVIEW -> STATUS_IN_BM_REVIEW --------------------------#
    def can_submit_for_bm_review(self):
        """Only categories of approval level APPROVAL_MINISTER require this step."""
        return self.max_approval_level == ConservationList.APPROVAL_MINISTER

    @fsm_log_by
    @transition(
        field=status,
        source=STATUS_IN_PANEL_REVIEW,
        target=STATUS_IN_BM_REVIEW,
        conditions=[can_submit_for_panel_review],
        # permission='conservation.submit_for_bm_review'
    )
    def submit_for_bm_review(self):
        """Submit a new Gazettal for Branch Manager review once panel endorses.

        Source: STATUS_IN_PANEL_REVIEW
        Target: STATUS_IN_BM_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires ministerial approval
        """
        logger.info("[Gazettal status] submit_for_bm_review")

    # STATUS_IN_BM_REVIEW -> STATUS_IN_DIR_REVIEW ----------------------------#
    def can_submit_for_dir_review(self):
        """Only categories of approval level APPROVAL_MINISTER require this step."""
        return self.max_approval_level == ConservationList.APPROVAL_MINISTER

    @fsm_log_by
    @transition(
        field=status,
        source=STATUS_IN_BM_REVIEW,
        target=STATUS_IN_DIR_REVIEW,
        conditions=[can_submit_for_dir_review],
        # permission='conservation.can_submit_for_dir_review'
    )
    def submit_for_director_review(self):
        """Submit a new Gazettal for Dir BCS review once BM endorses.

        Source: STATUS_IN_BM_REVIEW
        Target: STATUS_IN_DIR_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires ministerial approval
        """
        logger.info("[Gazettal status] submit_for_director_review")

    # STATUS_IN_DIR_REVIEW -> STATUS_IN_DG_REVIEW ----------------------------#
    def can_submit_for_dg_review(self):
        """Only categories of approval level APPROVAL_MINISTER require this step."""
        return self.max_approval_level == ConservationList.APPROVAL_MINISTER

    @fsm_log_by
    @transition(
        field=status,
        source=STATUS_IN_DIR_REVIEW,
        target=STATUS_IN_DG_REVIEW,
        conditions=[can_submit_for_dg_review],
        # permission='conservation.can_submit_for_dg_review'
    )
    def submit_for_director_general_review(self):
        """Submit a new Gazettal for DG review once Director endorses.

        Source: STATUS_IN_DIR_REVIEW
        Target: STATUS_IN_DG_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires ministerial approval
        """
        logger.info("[Gazettal status] submit_for_director_general_review")

    # STATUS_IN_DG_REVIEW -> STATUS_IN_MIN_REVIEW ----------------------------#
    def can_submit_for_minister_review(self):
        """Only categories of approval level APPROVAL_MINISTER require this step."""
        return self.max_approval_level == ConservationList.APPROVAL_MINISTER

    @fsm_log_by
    @transition(
        field=status,
        source=STATUS_IN_DG_REVIEW,
        target=STATUS_IN_MIN_REVIEW,
        conditions=[can_submit_for_minister_review],
        # permission='conservation.can_submit_for_dg_review'
    )
    def submit_for_minister_review(self):
        """Submit a new Gazettal for DG review once Director endorses.

        Source: STATUS_IN_DG_REVIEW
        Target: STATUS_IN_MIN_REVIEW
        Permissions: curators
        Gatecheck: At least one category requires ministerial approval
        """
        logger.info("[Gazettal status] submit_for_minister_review")

    # ALL -> STATUS_GAZETTED -------------------------------------------------#
    def can_mark_gazetted(self):
        """Gatecheck for mark_gazetted."""
        return True

    # @fsm_log_by
    # @transition(
    #     field=status,
    #     source='*',
    #     target=STATUS_GAZETTED,
    #     conditions=[can_mark_gazetted],
    #     # permission='conservation.can_mark_gazetted'
    # )
    # def mark_gazetted(self):
    #     """Mark a conservation listing as gazetted.

    #     This transition allows any source status to fast-track any Gazettal.

    #     Source: all but STATUS_GAZETTED
    #     Target: STATUS_GAZETTED
    #     Permissions: curators
    #     Gatecheck: can_mark_gazetted (pass)
    #     """
    #     logger.info("[Gazettal status] you should override this method to "
    #                 "close other Tax/ComGazettals in same scope.")

    # STATUS_GAZETTED -> STATUS_DELISTED -------------------------------------#
    def can_mark_delisted(self):
        """Gatecheck for mark_delisted."""
        return True

    @fsm_log_by
    @transition(
        field=status,
        source=[STATUS_PROPOSED,
                STATUS_IN_EXPERT_REVIEW,
                STATUS_IN_PUBLIC_REVIEW,
                STATUS_IN_PANEL_REVIEW,
                STATUS_IN_BM_REVIEW,
                STATUS_IN_DIR_REVIEW,
                STATUS_IN_DG_REVIEW,
                STATUS_IN_MIN_REVIEW,
                STATUS_GAZETTED],
        target=STATUS_DELISTED,
        conditions=[can_mark_delisted],
        # permission='conservation.can_mark_delisted'
    )
    def mark_delisted(self):
        """Mark a conservation listing as de-listed.

        This can either happen if a new conservation listing is gazetted,
        or if a conservation listing is de-listed without a superseding new listing.

        Source: all
        Target: STATUS_DELISTED
        Permissions: curators
        Gatecheck: can_mark_delisted (pass)
        """
        logger.info("[Gazettal status] mark_inactive")

    # end Django-FSM
    # ------------------------------------------------------------------------#


@python_2_unicode_compatible
class TaxonGazettal(Gazettal):
    """The Gazettal of a ConservationCategory against a Taxon.

    There can only be one Gazettal per scope.
    Transition to "gazetted" shall close any other Gazettals of same scope.
    """

    taxon = models.ForeignKey(Taxon,
                              related_name="taxon_gazettal")

    def __str__(self):
        """The full name."""
        return "{0} {1} {2} {3}".format(
            self.get_scope_display(),
            self.taxon,
            self.category_cache,
            self.criteria_cache
        ).strip()

    class Meta:
        """Class opts."""

        verbose_name = "Taxon Gazettal"
        verbose_name_plural = "Taxon Gazettals"

    @fsm_log_by
    @transition(
        field='status',
        source=[Gazettal.STATUS_PROPOSED,
                Gazettal.STATUS_IN_EXPERT_REVIEW,
                Gazettal.STATUS_IN_PUBLIC_REVIEW,
                Gazettal.STATUS_IN_PANEL_REVIEW,
                Gazettal.STATUS_IN_BM_REVIEW,
                Gazettal.STATUS_IN_DIR_REVIEW,
                Gazettal.STATUS_IN_DG_REVIEW,
                Gazettal.STATUS_IN_MIN_REVIEW,
                Gazettal.STATUS_DELISTED],
        target=Gazettal.STATUS_GAZETTED,
        # conditions=[Gazettal.can_mark_gazetted],
        # permission='conservation.can_mark_gazetted'
    )
    def mark_gazetted(self):
        """Mark a conservation listing as gazetted.

        This transition allows any source status to fast-track any Gazettal.

        Source: all but STATUS_GAZETTED
        Target: STATUS_GAZETTED
        Permissions: curators
        Gatecheck: can_mark_gazetted (pass)
        """
        logger.info("[Taxon Gazettal] mark_gazetted should now mark older "
                    "Gazettals as de-listed.")
        [gazettal.mark_delisted() for gazettal in
         self.taxon.taxon_gazettal.filter(scope=self.scope).exclude(pk=self.pk)]


@python_2_unicode_compatible
class CommunityGazettal(Gazettal):
    """The Gazettal of a ConservationCategory against a Community."""

    community = models.ForeignKey(Community,
                                  related_name="community_gazettal")

    class Meta:
        """Class opts."""

        verbose_name = "Community Gazettal"
        verbose_name_plural = "Community Gazettals"

    def __str__(self):
        """The full name."""
        return "{0} {1} {2} {3}".format(
            self.get_scope_display(),
            self.community.code,
            self.category_cache,
            self.criteria_cache
        ).strip()

    @fsm_log_by
    @transition(
        field='status',
        source=[Gazettal.STATUS_PROPOSED,
                Gazettal.STATUS_IN_EXPERT_REVIEW,
                Gazettal.STATUS_IN_PUBLIC_REVIEW,
                Gazettal.STATUS_IN_PANEL_REVIEW,
                Gazettal.STATUS_IN_BM_REVIEW,
                Gazettal.STATUS_IN_DIR_REVIEW,
                Gazettal.STATUS_IN_DG_REVIEW,
                Gazettal.STATUS_IN_MIN_REVIEW,
                Gazettal.STATUS_DELISTED],
        target=Gazettal.STATUS_GAZETTED,
        # conditions=[Gazettal.can_mark_gazetted],
        # permission='conservation.can_mark_gazetted'
    )
    def mark_gazetted(self):
        """Mark a conservation listing as gazetted.

        This transition allows any source status to fast-track any Gazettal.

        Source: all but STATUS_GAZETTED
        Target: STATUS_GAZETTED
        Permissions: curators
        Gatecheck: can_mark_gazetted (pass)
        """
        logger.info("[Community Gazettal] De-list previous "
                    "Gazettals in same scope.")
        [gazettal.mark_delisted() for gazettal in
         self.community.community_gazettal.filter(scope=self.scope).exclude(pk=self.pk)]


@receiver(pre_save, sender=TaxonGazettal)
@receiver(pre_save, sender=CommunityGazettal)
def gazettal_caches(sender, instance, *args, **kwargs):
    """Gazettal: Cache expensive lookups."""
    if instance.pk:
        logger.info("[gazettal_caches] Updating cache fields.")
        instance.category_cache = instance.build_category_cache
        instance.criteria_cache = instance.build_criteria_cache
        instance.label_cache = instance.build_label_cache
    else:
        logger.info("[gazettal_caches] New Gazettal, re-save to populate caches.")