from django.db import models

class Department(models.Model):
    DEPT_ID = models.CharField(max_length=7, primary_key=True)
    title = models.CharField(max_length=255, null=True)

class Course(models.Model):
    COURSE_ID = models.CharField(max_length=7, primary_key=True)
    title = models.CharField(max_length=255, null=True)
    modules = models.ManyToManyField('Module')

class Student(models.Model):
    URN = models.CharField(max_length=7, primary_key=True, default='0000000')
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    courses = models.ManyToManyField(Course)
    preference = models.CharField(max_length=50, choices=[
        ('none', 'none'),
        ('robotics', 'robotics'),
        ('robotics','robotics'),
        ('AI','AI'),('cyber security','cyber security'),
        ('web development','web development'),
        ('databases','databases'),
        ('software engineering','software engineering'),
        ('electronic engineering','electronic engineering'),
        ('programming','programming'),
        ('circuit design','circuit design'),
        ('game development','game development'),
        # Add other preferences
    ], null=True)
    assessments = models.ManyToManyField('Assessment', through='StudentMark')

class Academic(models.Model):
    URN = models.CharField(max_length=7, primary_key=True, default='0000000')
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.RESTRICT, null=True)
    preference = models.CharField(max_length=50, choices=[
        ('none', 'None'),
        ('robotics', 'Robotics'),
        ('AI', 'Artificial Intelligence'),
    ], null=True)

class Module(models.Model):
    MODULE_ID = models.CharField(max_length=7, default='', unique=True, help_text="Three letters followed by four integers, e.g., ABC1234")
    title = models.CharField(max_length=255, null=True)
    courses = models.ManyToManyField(Course)
    conveners = models.OneToOneField('Convener', on_delete=models.RESTRICT, null=True)
    assessments = models.ManyToManyField('Assessment')

class Convener(models.Model):
    URN = models.CharField(max_length=7, primary_key=True, default='0000000')
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    #MODULE = models.OneToOneField(Module, on_delete=models.SET_NULL, null=True, related_name='conveners')


class Assessment(models.Model):
    ASS_ID = models.CharField(max_length=7, primary_key=True, default='0000000')
    Total_Mark = models.IntegerField(null=True)
    Pass_Mark = models.IntegerField(null=True)
    Weighting = models.IntegerField(null=True)
    modules = models.ManyToManyField(Module)
    students = models.ManyToManyField(Student, through='StudentMark')

class StudentMark(models.Model):
    ASSESSMENT = models.ForeignKey(Assessment, on_delete=models.RESTRICT)
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    ACADEMIC = models.ForeignKey(Academic, on_delete=models.CASCADE)
    Mark = models.IntegerField(null=True)
