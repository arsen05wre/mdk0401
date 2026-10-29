from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.journal.views import StudentViewSet, SubjectViewSet, GradeViewSet, AttendanceViewSet, SummaryView
router = DefaultRouter()
router.register("students", StudentViewSet)
router.register("subjects", SubjectViewSet)
router.register("grades", GradeViewSet)
router.register("attendance", AttendanceViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/summary/", SummaryView.as_view(), name="summary"),
    path("api-auth/", include("rest_framework.urls")),
]
