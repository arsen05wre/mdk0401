from datetime import date, timedelta
from django.core.management.base import BaseCommand
from apps.journal.models import Student, Subject, Grade, Attendance

class Command(BaseCommand):
    help = "Создать демонстрационные данные электронного журнала"
    def handle(self, *args, **options):
        subjects_data = [("Математика","Иванова М.А."),("История","Петров С.В."),("Информатика","Сидоров И.П."),("Русский язык","Смирнова Е.Н.")]
        subjects = {}
        for name, teacher in subjects_data:
            subjects[name], _ = Subject.objects.get_or_create(name=name, defaults={"teacher":teacher})
        students_data = [("Анна","Иванова","9А"),("Максим","Смирнов","9А"),("Алина","Кузнецова","9Б"),("Дмитрий","Попов","9Б"),("София","Соколова","9А")]
        for first, last, cls in students_data:
            student, _ = Student.objects.get_or_create(first_name=first,last_name=last,class_name=cls)
            for i, subject in enumerate(subjects.values()):
                Grade.objects.get_or_create(student=student,subject=subject,date=date.today()-timedelta(days=i+1),
                    defaults={"mark":[5,4,5,3,4][(i+len(last))%5],"comment":"Демонстрационная запись"})
                Attendance.objects.get_or_create(student=student,subject=subject,date=date.today()-timedelta(days=i+1),
                    defaults={"status":"absent" if (i+len(last))%7==0 else "present"})
        self.stdout.write(self.style.SUCCESS("Демонстрационные данные электронного журнала созданы."))
