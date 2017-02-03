
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Instructor(models.Model):
	instructor_alt_id = models.CharField(max_length=50, null=True, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank=True, null=True)
	zip_code = models.CharField(max_length=10, blank=True, null=True)
	state = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	cell_phone = models.CharField(max_length=20, default='###-###-####', null=True)
	instructor_picture = models.FileField(null=True)
    
	def __str__(self):
		return 'Instructor ID: ' + self.student_id + ' - ' + str(self.first_name)  + ' ' + str(self.last_name)

	class Meta:
		db_table = 'instructor'

class Student(models.Model):
	student_alt_id = models.CharField(max_length=50, null=True, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank=True, null=True)
	zip_code = models.CharField(max_length=10, blank=True, null=True)
	state = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	cell_phone = models.CharField(max_length=20, default='###-###-####', null=True)
	student_picture = models.FileField(null=True)

	def __str__(self):
		return 'Student ID: ' + self.student_id + ' - ' + str(self.first_name)  + ' ' + str(self.last_name)


	class Meta:
		db_table = 'student'


class Lesson(models.Model):
	class_alt_id = models.CharField(max_length=50, null=True, unique=True)
	class_name = models.CharField(max_length=60)
	class_description = models.TextField(max_length=500)
	class_capacity = models.IntegerField(blank=True, null=True)
	start_time = models.DateTimeField(blank=True, null=True)
	end_time = models.DateTimeField(blank=True, null=True)
	level = models.ForeignKey('LessonLevel', on_delete=models.CASCADE, blank=True, null=True)
	student_members = models.ManyToManyField(Student, through='student_in_lesson')
	instructor_members = models.ManyToManyField(Instructor, through='instructor_in_lesson')

	def __str__(self):
         return self.class_alt_id + ' - ' + self.class_name
	
	def get_absolute_url(self):
		return reverse('nonprofit:lesson')

	class Meta:
		db_table = 'lesson'


class LessonLevel(models.Model):
    level_name = models.CharField(max_length=50)
    level_description = models.TextField(max_length=500, blank=True, null=True)
	
    def __str__(self):
         return self.level_id + ' - ' + self.level_name

    class Meta:
        db_table = 'lesson_level'


class Student_in_lesson(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	enrollment_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

	def __str__(self):
		return str(self.student) + ' - ' + str(self.lesson)  + ' - ' + str(self.enrollment_date)

	class Meta:
		db_table = 'student_in_lesson'
		unique_together = (('student', 'lesson'),)

class Instructor_in_lesson(models.Model):
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	enrollment_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

	def __str__(self):
		return str(self.instructor) + ' - ' + str(self.lesson)  + ' - ' + str(self.enrollment_date)

	class Meta:
		db_table = 'instructor_in_lesson'
		unique_together = (('instructor', 'lesson'),)
