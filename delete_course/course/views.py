from django.shortcuts import render, get_object_or_404, redirect
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def delete_course(request, course_code):
    course = get_object_or_404(Course, code=course_code) 
    if request.method == 'POST':
        course.delete() 
        return redirect('course_list')  
    return render(request, 'delete_course.html', {'course': course})
