
from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from myapp import views
from myapp.views import *
from myapp.models import *

router = routers.DefaultRouter()

router.register(r'Student', views.StudentViewSet)
router.register(r'Module', views.ModuleViewSet)
router.register(r'Academic', views.AcademicViewSet)
router.register(r'Convener', views.ConvenerViewSet)
router.register(r'Course', views.CourseViewSet)
#router.register(r'Department', views.DepartmentViewSet)
router.register(r'ModuleCourse', views.ModuleCourseViewSet)
router.register(r'Assessment', views.AssessmentViewSet)
#router.register(r'StudentAcademicModule', views.StudentAcademicModuleViewSet)
router.register(r'StudentMark', views.StudentMarkViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/studentURN', get_column_values, name = "getURN"),
    path('api/preferences/', PreferenceValues.as_view(), name='preferences-api'),
    path('api/students/<int:student_id>/update_preference/', update_student_preference, name='update_student_preference'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path("api/<slug:slug>/", views.Student.URN(), name = "single Student")
    path('patch-endpoint/', views.your_patch_view, name='patch_endpoint'),
    path('markPatch-endpoint/', views.markPatchView, name='markPatch_endpoint')
]