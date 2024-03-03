from django.db import models

class Department(models.Model):
    DEPT_ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True)

class Course(models.Model):
    COURSE_ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True)

class Student(models.Model):
    URN = models.IntegerField(primary_key=True, default = 0)
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    preference = models.CharField(max_length=50, choices=[
        ('none','none'),
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

class Academic(models.Model):
    URN = models.IntegerField(primary_key=True, default = 0)
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.RESTRICT, null=True)
    preference = models.CharField(max_length=50, choices=[
        ('none', 'None'),
        ('robotics', 'Robotics'),
        ('AI', 'Artificial Intelligence'),
    ], null=True)

class Module(models.Model):
    MODULE_ID = models.IntegerField(default = '')
    title = models.CharField(max_length=255, null=True)

class Convener(models.Model):
    URN = models.IntegerField(primary_key=True, default = 0)
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')

class ModuleCourse(models.Model):
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE, default = '')

class StudentAcademicModule(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE, default = '')
    ACADEMIC = models.ForeignKey(Academic, on_delete=models.CASCADE, default = '')
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')

class Assessment(models.Model):
    ASS_ID = models.IntegerField(primary_key=True, default = 0)
    Total_Mark = models.IntegerField(null=True)
    Pass_Mark = models.IntegerField(null=True)
    Weighting = models.IntegerField(null=True)
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')

class StudentMark(models.Model):
    ASSESSMENT = models.ForeignKey(Assessment, on_delete=models.RESTRICT, default = '')
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE, default = '')
    ACADEMIC = models.ForeignKey(Academic, on_delete=models.CASCADE, default = '')
    Mark = models.IntegerField(null=True)
