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

    path("sponsorship/create", base_view.CreateSponsorshipView.as_view(), name="create_sponsorship"),
    path('sponsorship/update/<int:id>/', base_view.UpdateSponsorshipView.as_view(), name="update_sponsorship"),
    path('sponsorship/student_sponsors/<int:id>/', base_view.StudentSponsorsViews.as_view(), name="student-sponsors"),
    path('sponsorship/sponsor_students/<int:id>/', base_view.SponsorStudentsViews.as_view(), name="sponsor-studets"),


    path("dashboard/", base_view.DashboardData.as_view(), name="dashboard"),
    path("dashboard/students", base_view.DashboardLineStudent.as_view(), name="dashboard_student"),
    path("dashboard/sponsor", base_view.DashboardLineSponsor.as_view(), name="dashboard_sponsor"),
]