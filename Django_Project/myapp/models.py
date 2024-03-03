from django.db import models

class Course(models.Model):
    COURSE_ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True)

class Student(models.Model):
    URN = models.CharField(max_length=7, primary_key=True, default='0000000')
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
    URN = models.CharField(max_length=7, primary_key=True, default='0000000')
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
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
    ], null=True)

class Module(models.Model):
    MODULE_ID = models.CharField(max_length=7, default='', primary_key=True, help_text="Three letters followed by four integers, e.g., ABC1234")
    title = models.CharField(max_length=255, null=True)

class Convener(models.Model):
    URN = models.CharField(max_length=7, primary_key=True, default='0000000')
    FName = models.CharField(max_length=255, null=True)
    LName = models.CharField(max_length=255, null=True)
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')

class ModuleCourse(models.Model):
    ID = models.IntegerField(primary_key=True, default = 0)
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE, default = '')

class Assessment(models.Model):
    ASS_ID = models.IntegerField(primary_key=True, default = 0)
    Total_Mark = models.IntegerField(null=False, default = 100)
    Pass_Mark = models.IntegerField(null=False, default = 40)
    Weighting = models.IntegerField(null=True)
    MODULE = models.ForeignKey(Module, on_delete=models.RESTRICT, default = '')

class StudentMark(models.Model):
    MARK_ID = models.IntegerField(primary_key=True, default = 0)
    ASSESSMENT = models.ForeignKey(Assessment, on_delete=models.RESTRICT, default = '',)
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE, default = '')
    ACADEMIC = models.ForeignKey(Academic, on_delete=models.CASCADE, null = True)
    Mark = models.IntegerField(null=True)    
