from rest_framework import serializers
from . models import *

'''
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
'''
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ConvenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convener
        fields = '__all__'

class ModuleCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleCourse
        fields = '__all__'

#class StudentAcademicModuleSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = StudentAcademicModule
   #     fields = ['STUDENT','ACADEMIC','MODULE']

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = '__all__'