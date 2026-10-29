from django.db.models import Avg, Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student, Subject, Grade, Attendance
from .serializers import StudentSerializer, SubjectSerializer, GradeSerializer, AttendanceSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ["first_name", "last_name", "class_name"]
    filterset_fields = ["class_name"]
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ["name", "teacher"]
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related("student", "subject").all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["student", "subject", "mark", "date"]
    ordering_fields = ["date", "mark"]
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related("student", "subject").all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["student", "subject", "status", "date"]

class SummaryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        grades = Grade.objects.all()
        return Response({
            "students": Student.objects.count(),
            "subjects": Subject.objects.count(),
            "grades": grades.count(),
            "average_mark": round(grades.aggregate(avg=Avg("mark"))["avg"] or 0, 2),
            "excellent": grades.filter(mark=5).count(),
            "absences": Attendance.objects.filter(status=Attendance.Status.ABSENT).count(),
            "recent_grades": GradeSerializer(grades.select_related("student","subject")[:10], many=True).data,
        })
