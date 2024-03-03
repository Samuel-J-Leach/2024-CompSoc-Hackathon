from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Academic)
admin.site.register(Convener)
admin.site.register(Course)
#admin.site.register(Department)
admin.site.register(ModuleCourse)
admin.site.register(Assessment)
#admin.site.register(StudentAcademicModule)
admin.site.register(StudentMark)
