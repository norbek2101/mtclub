from common.models import Sponsor, Student, University, Sponsorship

from common.serializers.base_serializers import RegisterSponsorSerializer, ListSponsorsSerializer, DetailSponsorSerializer, \
    RegisterStudentSerializer, CreateUniversitySerializer, ListStudentsSerializer, \
    DetailStudentSerializer, UpdateStudentSerializer, SponsorshipSerializer, UpdateSponsorshipSerializer, \
    LineDashboardSponsorsSerializer, LineDashboardStudentsSerializer

from rest_framework import generics, permissions, parsers
from rest_framework.views import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
from core.custom_pagination import CustomPagination

class RegisterSponsorView(generics.CreateAPIView):
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


class RegisterStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = RegisterStudentSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]

    permission_classes = [permissions.IsAuthenticated]


class ListStudentsView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentsSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('type', 'university')
    search_fields = ('name',)


class DetailStudentView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = DetailStudentSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


class UpdateStudentView(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CreateSponsorshipView(generics.CreateAPIView):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]


class UpdateSponsorshipView(generics.RetrieveDestroyAPIView, generics.GenericAPIView):
    queryset = Sponsorship.objects.all()
    serializer_class = UpdateSponsorshipSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DashboardData(generics.ListAPIView):
    serializer_class = UpdateSponsorshipSerializer
    pagination_class = CustomPagination

    def get(self, request, format=None):
        try:
            total_spent = Sponsor.objects.aggregate(total_sponsors_spent=models.Sum('spent_amount'))
            total_contract = Student.objects.aggregate(total_contract=models.Sum('contract'))

            total_spent = total_spent['total_sponsors_spent']
            total_contract = total_contract['total_contract']

            required_amount = total_contract - total_spent

            return Response({'total_sponsors_spent': total_spent,
                            'total_contract': total_contract,
                            'required_amount': required_amount})
        except TypeError:
            return Response({"error": f"total_contract --- is None or total_contract--- is None"})


class DashboardLineStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = LineDashboardStudentsSerializer
    pagination_class = CustomPagination


class DashboardLineSponsor(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = LineDashboardSponsorsSerializer
    pagination_class = CustomPagination
