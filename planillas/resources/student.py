from planillas.resources.academicMethod import AcademicMethod
from planillas.resources.semester import Semester

__author__ = 'Emilio-Emilio'
from django.db import models
from rest_framework import viewsets, views, serializers
from planillas.resources.specialty import Specialty
from planillas.resources.academicUnit import AcademicUnit

PARALLEL_CHOICES = (
    ('A', 'Paralelo A'),
    ('B', 'Paralelo B'),
    ('C', 'Paralelo C'),
    ('D', 'Paralelo D'),
    ('E', 'Paralelo E'),
    ('F', 'Paralelo F'),
    ('G', 'Paralelo G'),
    ('H', 'Paralelo H'),
    ('I', 'Paralelo I'),
    ('J', 'Paralelo J'),
    ('K', 'Paralelo K'),
    ('L', 'Paralelo L'),
    ('M', 'Paralelo M'),
    ('N', 'Paralelo N'),
    ('O', 'Paralelo O'),
    ('P', 'Paralelo P'),
    ('Q', 'Paralelo Q'),
    ('R', 'Paralelo R'),
    ('S', 'Paralelo S'),
    ('T', 'Paralelo T'),
    ('U', 'Paralelo U'),
    ('V', 'Paralelo V'),
    ('W', 'Paralelo W'),
    ('X', 'Paralelo X'),
    ('Y', 'Paralelo Y'),
    ('Z', 'Paralelo Z'),
)


class Student(models.Model):
    semester = models.ForeignKey(Semester, default=1)
    parallel = models.CharField(max_length=2, default='A', choices=PARALLEL_CHOICES)
    specialty = models.ForeignKey(Specialty)
    academicUnit = models.ForeignKey(AcademicUnit)
    academicMethod = models.ForeignKey(AcademicMethod, default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.semester

    class Meta:
        ordering = ['id']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id', 'semester', 'parallel', 'specialty', 'academicUnit', 'academicMethod', 'created_at', 'updated_at')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
