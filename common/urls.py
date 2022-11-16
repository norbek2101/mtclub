from django.urls import path
from common.views import base_view

urlpatterns = [
    path("register/", base_view.RegisterSponsorView.as_view(), name="register_sponsor"),
    path("sponsors/", base_view.ListSponsorsView.as_view(), name="sponsors"),
]