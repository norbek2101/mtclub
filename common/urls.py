from django.urls import path
from common.views import base_view

urlpatterns = [
    path("register/", base_view.RegisterSponsorView.as_view(), name="register_sponsor"),
    path("sponsors/", base_view.ListSponsorsView.as_view(), name="sponsors"),
    path('detail/<int:id>/', base_view.DetailSponsorView.as_view(), name="detail_sponsor"),

    path("university/create/", base_view.CreateUniversityView.as_view(), name="create_university"),
    
]