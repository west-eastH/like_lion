from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=100)
	studentId = models.IntegerField(primary_key=True)
	email = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	admission = models.DateField()

class Subject(models.Model):
	subjectName = models.CharField(max_length=100)
	subjectId = models.IntegerField(primary_key=True)
	open_date = models.DateField()

