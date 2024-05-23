from models import Student
from models import Subject
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"


class SubjectSerializers(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = "__all__"