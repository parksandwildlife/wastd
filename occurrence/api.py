from django.apps import apps
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters import FilterSet

from shared.api import BatchUpsertViewSet, MyGeoJsonPagination
from wastd.users.models import User

from taxonomy.models import Community, Taxon
from occurrence import serializers
from occurrence.models import (
    AreaEncounter,
    TaxonAreaEncounter,
    EncounterType,
    CommunityAreaEncounter,
    Landform,
    RockType,
    SoilType,
    SoilColour,
    Drainage,
    SurveyMethod,
    SoilCondition,
    CountAccuracy,
    CountMethod,
    CountSubject,
    PlantCondition,
    DetectionMethod,
    Confidence,
    ReproductiveMaturity,
    AnimalHealth,
    AnimalSex,
    CauseOfDeath,
    SecondarySigns,
    SampleType,
    SampleDestination,
    PermitType,
    ObservationGroup,
)


class OccurrenceAreaEncounterFilter(FilterSet):
    """Occurrence AreaEncounter filter.
    """
    class Meta:
        model = AreaEncounter
        fields = {
            "area_type": ["exact", "in"],
            "accuracy": ["exact", "gt", "lt"],
            "code": ["exact", "icontains", "in"],
            "label": ["exact", "icontains", "in"],
            "name": ["exact", "icontains", "in"],
            "description": ["exact", "icontains", "in"],
            "northern_extent": ["exact", "gt", "lt"],
            "source": ["exact", "in"],
            "source_id": ["exact", "in"],
        }


class OccurrenceAreaPolyViewSet(BatchUpsertViewSet):
    """Occurrence Area viewset.
    """
    model = AreaEncounter
    queryset = AreaEncounter.objects.all()
    serializer_class = serializers.OccurrenceAreaEncounterPolySerializer
    filter_class = OccurrenceAreaEncounterFilter
    pagination_class = MyGeoJsonPagination
    uid_fields = ("source", "source_id")


class OccurrenceAreaPointViewSet(OccurrenceAreaPolyViewSet):
    """Occurrence Area Point view set."""
    serializer_class = serializers.OccurrenceAreaEncounterPointSerializer


class OccurrenceTaxonAreaEncounterFilter(FilterSet):
    """Occurrence TaxonAreaEncounter filter.
    """
    class Meta:
        model = TaxonAreaEncounter
        fields = {
            "area_type": ["exact", "in"],
            "accuracy": ["exact", "gt", "lt"],
            "code": ["exact", "icontains", "in"],
            "label": ["exact", "icontains", "in"],
            "name": ["exact", "icontains", "in"],
            "description": ["exact", "icontains", "in"],
            "northern_extent": ["exact", "gt", "lt"],
            "source": ["exact", "in"],
            "source_id": ["exact", "in"],
            "encounter_type": ["exact", "in"],
        }


class OccurrenceTaxonAreaEncounterPolyViewSet(BatchUpsertViewSet):
    """TaxonEncounter polygon view set.
    """
    model = TaxonAreaEncounter
    queryset = TaxonAreaEncounter.objects.all().prefetch_related("taxon")
    serializer_class = serializers.OccurrenceTaxonAreaEncounterPolySerializer
    filter_class = OccurrenceTaxonAreaEncounterFilter
    pagination_class = MyGeoJsonPagination
    uid_fields = ("source", "source_id")

    def resolve_fks(self, data):
        """Resolve FKs from PK to object."""
        data["taxon"] = Taxon.objects.get(name_id=data["taxon"])
        data["encountered_by"] = User.objects.get(pk=data["encountered_by"])
        data["encounter_type"] = EncounterType.objects.get(pk=data["encounter_type"])
        return data


class OccurrenceTaxonAreaEncounterPointViewSet(OccurrenceTaxonAreaEncounterPolyViewSet):
    """TaxonEncounter point view set.
    """
    serializer_class = serializers.OccurrenceTaxonAreaEncounterPointSerializer


class OccurrenceCommunityAreaEncounterFilter(FilterSet):
    """Occurrence CommunityAreaEncounter filter.
    """
    class Meta:
        model = CommunityAreaEncounter
        fields = {
            "area_type": ["exact", "in"],
            "accuracy": ["exact", "gt", "lt"],
            "code": ["exact", "icontains", "in"],
            "label": ["exact", "icontains", "in"],
            "name": ["exact", "icontains", "in"],
            "description": ["exact", "icontains", "in"],
            "northern_extent": ["exact", "gt", "lt"],
            "source": ["exact", "in"],
            "source_id": ["exact", "in"],
        }


class OccurrenceCommunityAreaEncounterPolyViewSet(BatchUpsertViewSet):
    """Occurrence CommunityAreaEncounter view set.
    """
    model = CommunityAreaEncounter
    queryset = CommunityAreaEncounter.objects.all().prefetch_related("community")
    serializer_class = serializers.OccurrenceCommunityAreaEncounterPolySerializer
    filter_class = OccurrenceCommunityAreaEncounterFilter
    pagination_class = MyGeoJsonPagination
    uid_fields = ("source", "source_id")

    def resolve_fks(self, data):
        """Resolve FKs from PK to object."""
        try:
            data["community"] = Community.objects.get(code=data["community"])
        except Exception as e:
            print("Exception {0}: community {1} not known,".format(e, data["community"]))
        data["encountered_by"] = User.objects.get(pk=data["encountered_by"])
        data["encounter_type"] = EncounterType.objects.get(pk=data["encounter_type"])
        return data


class OccurrenceCommunityAreaEncounterPointViewSet(OccurrenceCommunityAreaEncounterPolyViewSet):
    """Occurrence CommunityAreaEncounter view set."""

    serializer_class = serializers.OccurrenceCommunityAreaEncounterPointSerializer


class LandformViewSet(BatchUpsertViewSet):
    """View set for Landform.
    """
    model = Landform
    queryset = Landform.objects.all()
    serializer_class = serializers.LandformSerializer
    uid_fields = ("pk",)


class RockTypeViewSet(BatchUpsertViewSet):
    """View set for RockType."""

    queryset = RockType.objects.all()
    serializer_class = serializers.RockTypeSerializer
    uid_fields = ("pk",)
    model = RockType


class SoilTypeViewSet(BatchUpsertViewSet):
    """View set for SoilType."""

    queryset = SoilType.objects.all()
    serializer_class = serializers.SoilTypeSerializer
    uid_fields = ("pk",)
    model = SoilType


class SoilColourViewSet(BatchUpsertViewSet):
    """View set for SoilColour."""

    queryset = SoilColour.objects.all()
    serializer_class = serializers.SoilColourSerializer
    uid_fields = ("pk",)
    model = SoilColour


class DrainageViewSet(BatchUpsertViewSet):
    """View set for Drainage."""

    queryset = Drainage.objects.all()
    serializer_class = serializers.DrainageSerializer
    uid_fields = ("pk",)
    model = Drainage


class SurveyMethodViewSet(BatchUpsertViewSet):
    """View set for SurveyMethod."""

    queryset = SurveyMethod.objects.all()
    serializer_class = serializers.SurveyMethodSerializer
    uid_fields = ("pk",)
    model = SurveyMethod


class SoilConditionViewSet(BatchUpsertViewSet):
    """View set for SoilCondition."""

    queryset = SoilCondition.objects.all()
    serializer_class = serializers.SoilConditionSerializer
    uid_fields = ("pk",)
    model = SoilCondition


class CountAccuracyViewSet(BatchUpsertViewSet):
    """View set for CountAccuracy."""

    queryset = CountAccuracy.objects.all()
    serializer_class = serializers.CountAccuracySerializer
    uid_fields = ("pk",)
    model = CountAccuracy


class CountMethodViewSet(BatchUpsertViewSet):
    """View set for CountMethod."""

    queryset = CountMethod.objects.all()
    serializer_class = serializers.CountMethodSerializer
    uid_fields = ("pk",)
    model = CountMethod


class CountSubjectViewSet(BatchUpsertViewSet):
    """View set for CountSubject."""

    queryset = CountSubject.objects.all()
    serializer_class = serializers.CountSubjectSerializer
    uid_fields = ("pk",)
    model = CountSubject


class PlantConditionViewSet(BatchUpsertViewSet):
    """View set for PlantCondition."""

    queryset = PlantCondition.objects.all()
    serializer_class = serializers.PlantConditionSerializer
    uid_fields = ("pk",)
    model = PlantCondition


class DetectionMethodViewSet(BatchUpsertViewSet):
    """View set for DetectionMethod."""

    queryset = DetectionMethod.objects.all()
    serializer_class = serializers.DetectionMethodSerializer
    uid_fields = ("pk",)
    model = DetectionMethod


class ConfidenceViewSet(BatchUpsertViewSet):
    """View set for Confidence."""

    queryset = Confidence.objects.all()
    serializer_class = serializers.ConfidenceSerializer
    uid_fields = ("pk",)
    model = Confidence


class ReproductiveMaturityViewSet(BatchUpsertViewSet):
    """View set for ReproductiveMaturity."""

    queryset = ReproductiveMaturity.objects.all()
    serializer_class = serializers.ReproductiveMaturitySerializer
    uid_fields = ("pk",)
    model = ReproductiveMaturity


class AnimalHealthViewSet(BatchUpsertViewSet):
    """View set for Drainage."""

    queryset = AnimalHealth.objects.all()
    serializer_class = serializers.AnimalHealthSerializer
    uid_fields = ("pk",)
    model = AnimalHealth


class AnimalSexViewSet(BatchUpsertViewSet):
    """View set for Drainage."""

    queryset = AnimalSex.objects.all()
    serializer_class = serializers.AnimalSexSerializer
    uid_fields = ("pk",)
    model = AnimalSex


class CauseOfDeathViewSet(BatchUpsertViewSet):
    """View set for CauseOfDeath."""

    queryset = CauseOfDeath.objects.all()
    serializer_class = serializers.CauseOfDeathSerializer
    uid_fields = ("pk",)
    model = CauseOfDeath


class SecondarySignsViewSet(BatchUpsertViewSet):
    """View set for SecondarySigns."""

    queryset = SecondarySigns.objects.all()
    serializer_class = serializers.SecondarySignsSerializer
    uid_fields = ("pk",)
    model = SecondarySigns


class SampleTypeViewSet(BatchUpsertViewSet):
    """View set for SampleType."""

    queryset = SampleType.objects.all()
    serializer_class = serializers.SampleTypeSerializer
    uid_fields = ("pk",)
    model = SampleType


class SampleDestinationViewSet(BatchUpsertViewSet):
    """View set for SampleDestination."""

    queryset = SampleDestination.objects.all()
    serializer_class = serializers.SampleDestinationSerializer
    uid_fields = ("pk",)
    model = SampleDestination


class PermitTypeViewSet(BatchUpsertViewSet):
    """View set for PermitType."""

    queryset = PermitType.objects.all()
    serializer_class = serializers.PermitTypeSerializer
    uid_fields = ("pk",)
    model = PermitType


class ObservationGroupViewSet(ModelViewSet):
    """ObservationGroup models.

    Filter the Observations to a specific type with the parameter `obstype`:

    * [FileAttachment](/api/1/occ-observation/?obstype=FileAttachment)
    * [AreaAssessment](/api/1/occ-observation/?obstype=AreaAssessment)
    * [HabitatComposition](/api/1/occ-observation/?obstype=HabitatComposition)
    * [HabitatCondition](/api/1/occ-observation/?obstype=HabitatCondition)
    * [VegetationClassification](/api/1/occ-observation/?obstype=VegetationClassification)
    * [FireHistory](/api/1/occ-observation/?obstype=FireHistory)
    * [PlantCount](/api/1/occ-observation/?obstype=PlantCount)
    * [AssociatedSpecies](/api/1/occ-observation/?obstype=AssociatedSpecies)
    * [PhysicalSample](/api/1/occ-observation/?obstype=PhysicalSample)
    * [AnimalObservation](/api/1/occ-observation/?obstype=AnimalObservation)
    """
    serializer_class = serializers.ObservationGroupPolymorphicSerializer

    class Meta:
        model = ObservationGroup

    def get_queryset(self):
        """Filter queryset to the model specified by request parameter "obstype"."""
        model_name = self.request.query_params.get('obstype', None)
        if model_name is not None:
            return apps.get_model("occurrence", model_name).objects.all()
        else:
            return ObservationGroup.objects.all()
