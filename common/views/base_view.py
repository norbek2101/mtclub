from common.models import Sponsor, Student, University, Sponsorship

from common.serializers.base_serializers import RegisterSponsorSerializer, ListSponsorsSerializer, DetailSponsorSerializer, \
    RegisterStudentSerializer, CreateUniversitySerializer, ListStudentsSerializer, \
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


class DetailSponsorView(generics.RetrieveDestroyAPIView, generics.GenericAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = DetailSponsorSerializer
    parser_classes = [parsers.MultiPartParser]
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CreateUniversityView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = CreateUniversitySerializer
    pagination_class = CustomPagination

    permission_classes = [permissions.IsAuthenticated]
