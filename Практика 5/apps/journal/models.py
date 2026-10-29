from django.db import models

class Student(models.Model):
    first_name = models.CharField("Имя", max_length=80)
    last_name = models.CharField("Фамилия", max_length=80)
    class_name = models.CharField("Класс", max_length=10, default="9А")
    email = models.EmailField("Электронная почта", blank=True)
    class Meta:
        ordering = ["class_name", "last_name", "first_name"]
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.class_name})"

class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=100, unique=True)
    teacher = models.CharField("Учитель", max_length=120)
    class Meta:
        ordering = ["name"]
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
    def __str__(self):
        return self.name

class Grade(models.Model):
    MARK_CHOICES = [(2,"2"),(3,"3"),(4,"4"),(5,"5")]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades", verbose_name="Ученик")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="grades", verbose_name="Предмет")
    mark = models.PositiveSmallIntegerField("Оценка", choices=MARK_CHOICES)
    date = models.DateField("Дата")
    comment = models.CharField("Комментарий", max_length=250, blank=True)
    class Meta:
        ordering = ["-date", "student"]
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
    def __str__(self):
        return f"{self.student}: {self.subject} — {self.mark}"

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "present", "Присутствовал"
        ABSENT = "absent", "Отсутствовал"
        LATE = "late", "Опоздал"
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance", verbose_name="Ученик")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="attendance", verbose_name="Предмет")
    date = models.DateField("Дата")
    status = models.CharField("Посещаемость", max_length=10, choices=Status.choices, default=Status.PRESENT)
    class Meta:
        ordering = ["-date"]
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"
    def __str__(self):
        return f"{self.student} — {self.get_status_display()} ({self.date})"
