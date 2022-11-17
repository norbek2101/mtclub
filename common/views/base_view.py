import decimal
from common.models import Sponsor, Student, University, Sponsorship

from common.serializers.base_serializers import RegisterSponsorSerializer, ListSponsorsSerializer, DetailSponsorSerializer, \
    RegisterStudentSerializer, CreateUniversitySerializer, ListStudentsSerializer, \
    DetailStudentSerializer, UpdateStudentSerializer, SponsorshipSerializer, UpdateSponsorshipSerializer, \
    LineDashboardSponsorsSerializer, LineDashboardStudentsSerializer

from rest_framework import generics, permissions, parsers
from rest_framework.views import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('status', 'balance')
    search_fields = ('full_name', 'balance', 'created_at')


class DetailSponsorView(generics.RetrieveUpdateDestroyAPIView):
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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('type', 'university')
    search_fields = ('full_name', 'balance', 'created_at')


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


class UpdateStudentView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]
    lookup_field = 'id'

    


class CreateSponsorshipView(generics.CreateAPIView):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    pagination_class = CustomPagination
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request):
        try:
            sponsor = Sponsor.objects.get(id=request.data['sponsor'])
            student = Student.objects.get(id=request.data['student'])
            serializer = SponsorshipSerializer(data=request.data)
            valid = serializer.is_valid()
            if valid:
                serializer.save()
                amount = decimal.Decimal(serializer.data['amount'])
                if amount > sponsor.balance:
                    return Response({"amount": f"Kiritilgan summa sponsorning balansidan kichik bo'lishi kerak"})
                if amount + student.balance > student.contract:
                    return Response({'amount': "Talabaga ajratilayotgan summa kontrakt summasidan kichik bo'lishi kerak!"})

                sponsor.balance -= amount
                sponsor.spent_amount += amount
                student.balance += amount
                student.save()
                sponsor.save()
                return Response(serializer.data)
            else:
                return Response({"error":f"{serializer.errors}"})

        except Sponsor.DoesNotExist or Student.DoesNotExist:
            return Response({"error": f"{request.data['sponsor']} or {request.data['student']} is not found"})
        except Exception as e:
            return Response({"error": f"{e}"})

        finally:
            pass
                   



class UpdateSponsorshipView(generics.RetrieveUpdateDestroyAPIView):
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


class StudentSponsorsViews(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = ListSponsorsSerializer
    pagination_class = CustomPagination


    def get(self, request, id, format=None):
        """Talaba id si bo'yicha unga homiylik qilgan homiylar ro'yxatini qaytaradi"""
        sponsors = Sponsorship.objects.filter(student=id).values_list("sponsor")
        ls =  [list(i) for i in set(sponsors)]
        sponsor_ids = [i[0] for i in ls]
        res = []
        for i in sponsor_ids:
            dic = {}
            query = Sponsor.objects.get(id=i)
            dic['id'] = query.id
            dic['full_name'] = query.full_name
            dic['phone_number'] = query.phone_number
            dic['spent_amount'] = query.spent_amount
            dic['status'] = query.status
            dic['type'] = query.type
            dic['payment_type'] = query.payment_type
            dic['created_at'] = str(query.created_at)
            res.append(dic)
        return Response(res)


class SponsorStudentsViews(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = ListStudentsSerializer
    pagination_class = CustomPagination


    def get(self, request, id, format=None):
        """Homiy id si bo'yicha u homiylik qilgan talabalar ro'yxatini qaytaradi"""
        students = Sponsorship.objects.filter(sponsor=id).values_list("student")
        ls =  [list(i) for i in set(students)]
        student_ids = [i[0] for i in ls]
        res = []
        for i in student_ids:
            dic = {}
            query = Student.objects.get(id=i)
            dic['id'] = query.id
            dic['full_name'] = query.full_name
            dic['balance'] = query.balance
            dic['contract'] = query.contract
            dic['type'] = query.type
            dic['university'] = query.university.name
            dic['created_at'] = str(query.created_at)
            res.append(dic)
        return Response(res)