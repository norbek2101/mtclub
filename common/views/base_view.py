from common.models import Sponsor, Student, University, Sponsorship

from common.serializers.base_serializers import RegisterSponsorSerializer, ListSponsorsSerializer, DetailSponsorSerializer, \
    UpdateSponsorSerializer, RegisterStudentSerializer, CreateUniversitySerializer, ListStudentsSerializer, \
    DetailStudentSerializer, UpdateStudentSerializer, SponsorshipSerializer, UpdateSponsorshipSerializer, \
    LineDashboardSponsorsSerializer, LineDashboardStudentsSerializer

from rest_framework import generics, permissions, parsers
from django_filters.rest_framework import DjangoFilterBackend

from core.custom_pagination import CustomPagination

class RegisterSponsorView(generics.ListCreateAPIView):
    serializer_class = RegisterSponsorSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]
    queryset = Sponsor.objects.all()
    pagination_class = CustomPagination


class ListSponsorsView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = ListSponsorsSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status', 'balance')
    search_fields = ('name',)


