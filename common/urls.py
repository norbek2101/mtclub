from django.urls import path, include
from common.views import base_view

urlpatterns = [
    path("register/", base_view.RegisterSponsorView.as_view(), name="register_sponsor"),
    path('login/', include('dj_rest_auth.urls')),
    path("sponsors/", base_view.ListSponsorsView.as_view(), name="sponsors"),
    path('sponsors/detail/<int:id>/', base_view.DetailSponsorView.as_view(), name="detail_sponsor"),

    path("university/create/", base_view.CreateUniversityView.as_view(), name="create_university"),

    path("student/register/", base_view.RegisterStudentView.as_view(), name="register_student"),
    path("students/", base_view.ListStudentsView.as_view(), name="students"),
    path('student/<int:id>/', base_view.DetailStudentView.as_view(), name="detail_student"),
    path('student/update/<int:id>/', base_view.UpdateStudentView.as_view(), name="update_student"),
]