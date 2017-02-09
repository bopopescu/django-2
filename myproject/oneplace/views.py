from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from oneplace.models import Instructor, Student, Lesson, Lesson_level, Student_in_lesson, Instructor_in_lesson
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	return render(request, 'oneplace/index.html')


class LessonView(generic.ListView):
    template_name = 'oneplace/lesson.html'
    context_object_name ='lesson_all'
    def get_queryset(self):
        return Lesson.objects.all().order_by('start_time')

class StudentView(generic.ListView):
    template_name = 'oneplace/student.html'
    context_object_name ='student_Info'
    
    studentCount = Student.objects.all().count()

    
    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context.update({'studentCount': self.studentCount})
        return context

class LessonCreate(CreateView):
	model = Lesson
	fields = ['class_name','class_description','class_capacity', 'start_time','end_time', 'level']


class LessonUpdate(UpdateView):
	model = Lesson
	fields = ['class_name','class_description','class_capacity', 'start_time','end_time', 'level']


class StudentCreate(CreateView):
	model = Student
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'student_picture']


class StudentUpdate(UpdateView):
	model = Student
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'student_picture']


class StudentDelete(DeleteView):
	model = Student
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'student_picture']	
	success_url = reverse_lazy('oneplace:student')


class InstructorView(generic.ListView):
    template_name = 'oneplace/instructor.html'
    context_object_name ='instructor_Info'
    
    instructorCount = Instructor.objects.all().count()

    
    def get_queryset(self):
        return Instructor.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InstructorView, self).get_context_data(**kwargs)
        context.update({'instructorCount': self.instructorCount})
        return context

class InstructorCreate(CreateView):
	model = Instructor
	fields = ['first_name', 'last_name', 'address','state', 'city', 'zipcode', 'cell_phone', 'instructor_picture']


class InstructorUpdate(UpdateView):
	model = Instructor
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'instructor_picture']


class InstructorDelete(DeleteView):
	model = Instructor
	fields = ['first_name', 'last_name', 'address', 'state', 'city', 'zipcode', 'cell_phone', 'instructor_picture']	
	success_url = reverse_lazy('oneplace:instructor')


class StudentEnrollCreate(CreateView):
	model = Student_in_lesson
	fields = ['student', 'lesson']


class InstructorAssignCreate(CreateView):
	model = Instructor_in_lesson
	fields = ['instructor', 'lesson']


class LessonDelete(DeleteView):    
    model = Lesson
    success_url = reverse_lazy('oneplace:lesson')

def ClassEnrollment(request, pk): 
    lesson = Lesson.objects.get(pk=pk)
    student_in_lesson = lesson.student_members.all()
    instructor_assign_lesson = lesson.instructor_members.all()
    student_Count = lesson.student_members.all().count()
    context = {'lesson': lesson, 
               'student_Info': student_in_lesson, 
               'instructor_Info': instructor_assign_lesson,
               'student_Count': student_Count } 
    return render(request, 'oneplace/class_enrollment.html', context)

def StudentRemove(request, studentpk, lessonpk):
	student_delete=Student_in_lesson.objects.get(student=studentpk, lesson=lessonpk)
	student_delete.delete()
	return ClassEnrollment(request, lessonpk)