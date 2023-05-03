from django.db import models
from core.models import BaseModel, User, Student


# Create your models here.


class Semester(BaseModel):
    start_date = models.DateField("Start")
    end_date = models.DateField("End")

    def __str__(self):
        return f"{self.start_date.year}-{self.end_date.year}"


class Course(BaseModel):
    name = models.CharField("Name", max_length=30)
    prof = models.ForeignKey(User, models.RESTRICT, null=True, blank=True, related_name='prof_courses')
    students = models.ManyToManyField(Student, related_name='student_courses',
                                      through='StudentCourse')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        assert not self.prof or self.prof.groups.get(name__exact='Professor')
        super().save(force_insert, force_update, using, update_fields)


class StudentCourse(BaseModel):
    student = models.ForeignKey(Student, models.RESTRICT)
    course = models.ForeignKey(Course, models.RESTRICT)
    exam = models.OneToOneField('edu.Exam', models.CASCADE)


class Exam(BaseModel):
    final_mark = models.IntegerField("Final mark")

