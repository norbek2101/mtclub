from rest_framework import serializers
from common.models import Sponsor, Student, University, Sponsorship


class RegisterSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'balance', 'organization', 'type', 'payment_type')

    
    def validate(self, attrs):
        if attrs['type'] == "yuridik_shaxs":
            try:
                org = attrs['organization']
            except:
                raise serializers.ValidationError({
                    'organization': "Siz yuridik_shaxs ekansiz, kompaniya yoki tashkilot nomini kiritishingiz kerak"
                })
        return attrs

    
class ListSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'balance', 'spent_amount', 'created_at', 'status', 'type', 'payment_type')


class DetailSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'balance', 'status', 'organization', 'type', 'payment_type')


class CreateUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university', 'type', 'contract')


class ListStudentsSerializer(serializers.ModelSerializer):
    university = CreateUniversitySerializer()

    class Meta:
        model = Student
        fields = ('full_name', 'type', 'university', 'balance', 'contract')


class SponsorshipSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['amount'] > attrs['sponsor'].balance:
            raise serializers.ValidationError({
                'amount': "Kiritilgan summa sponsorning balansidan kichik bo'lishi kerak"
            })

        if attrs['amount'] + attrs['student'].balance > attrs['student'].contract:
            raise serializers.ValidationError({
                'amount': "Talabaga ajratilayotgan summa kontrakt summasidan kichik bo'lishi kerak!"
            })

        return attrs

    class Meta:
        model = Sponsorship
        fields = ('sponsor', 'student', 'amount')


class UpdateSponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = ('sponsor', 'student', 'amount')


class DetailSponsorshipSerializer(serializers.ModelSerializer):
    sponsor = ListSponsorsSerializer()

    class Meta:
        model = Sponsorship
        fields = ('sponsor', 'amount')


class DetailStudentSerializer(serializers.ModelSerializer):
    university = CreateUniversitySerializer()
    sponsors = DetailSponsorshipSerializer(many=True)

    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university', 'type', 'balance', 'contract', 'sponsors')


class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university', 'contract')


class LineDashboardStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'created_at')


class LineDashboardSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('full_name', 'created_at')
