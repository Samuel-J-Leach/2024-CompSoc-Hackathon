from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from . models import *
from . serializer import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# Views use models
# Create get(self, request) and post(self, request)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Get, Post
    def get(self,request):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PreferenceValues(APIView):
    def get(self,request, *args, **kwargs):
        # Define all possible preferences
        all_preferences = [
            'none',
            'robotics',
            'AI',
            'cyber security',
            'web development',
            'databases',
            'software engineering',
            'electronic engineering',
            'programming',
            'circuit design',
            'game development',
            # Add other preferences
        ]

        # Return the list of all preferences
        return JsonResponse({'preferences': all_preferences})

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AcademicViewSet(viewsets.ModelViewSet):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Get, Post
    def get(self,request):
        data = Academic.objects.all()
        serializer = AcademicSerializer(data, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = AcademicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConvenerViewSet(viewsets.ModelViewSet):
    queryset = Convener.objects.all()
    serializer_class = ConvenerSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

'''
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
'''
    
class ModuleCourseViewSet(viewsets.ModelViewSet):
    queryset = ModuleCourse.objects.all()
    serializer_class = ModuleCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

#class StudentAcademicModuleViewSet(viewsets.ModelViewSet):
 #   queryset = StudentAcademicModule.objects.all()
  #  serializer_class = StudentAcademicModuleSerializer
   # permission_classes = [permissions.IsAuthenticated]

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer
    permission_classes = [permissions.IsAuthenticated]

def update_student_preference(request, student_id):
    if request.method == 'PATCH':
        try:
            student = Student.objects.get(id=student_id)
            data = json.loads(request.body)
            student.preferences = data.get('preference', student.preferences)
            student.save()
            return JsonResponse({'message': 'Preference updated successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def get_column_values(request):
    # Query all values of the column into an array
    column_values_array = Student.objects.values_list('URN', flat=True)
    
    # Convert the queryset to a list
    column_values_list = list(column_values_array)
    
    # Return the data as JSON response
    return JsonResponse({'URN_values': column_values_list})

@csrf_exempt  #CSRF protection is disabled for this view
def your_patch_view(request):
    if request.method == 'PATCH':
        try:
            patch_data = json.loads(request.body.decode('utf-8'))  # Decode the bytes and parse JSON
            # Now patch_data is a Python dictionary containing the content of the PATCH request
            '''for i in Student.objects.all():
                if i.URN == patch_data["URN"]:
                    i.preference = patch_data["preference"]
                    return JsonResponse({'message': 'IDFK if this will be printed', 'patch_data': patch_data}, status=200)
            Student.save(i)'''
            record = Student.objects.get(pk=patch_data['URN'])
            record.preference = patch_data['preference']
            record.save()
            return JsonResponse({'message': 'PATCH request received', 'patch_data': patch_data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def markPatchView(request):
    if request.method == 'PATCH':
        try:
            patch_data = json.loads(request.body.decode('utf-8'))  # Decode the bytes and parse JSON
            print("patch_data:", patch_data)
            # Now patch_data is a Python dictionary containing the content of the PATCH request
            '''for i in Student.objects.all():
                if i.URN == patch_data["URN"]:
                    i.preference = patch_data["preference"]
                    return JsonResponse({'message': 'IDFK if this will be printed', 'patch_data': patch_data}, status=200)
            Student.save(i)'''
            record = StudentMark.objects.get(pk=patch_data['MARK_ID'])
            record.Mark = patch_data['Mark']
            record.save()
            return JsonResponse({'message': 'PATCH request received', 'patch_data': patch_data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)