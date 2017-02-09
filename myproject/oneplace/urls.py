from django.conf.urls import url

from . import views

app_name = 'oneplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^class/$', views.LessonView.as_view(), name='lesson'),
    url(r'^class/add/$', views.LessonCreate.as_view(), name='lesson_add'),
    url(r'^class/update/(?P<pk>[0-9]+)/$', views.LessonUpdate.as_view(), name='lesson_update'),
    url(r'^class/delete/(?P<pk>[0-9]+)/$', views.LessonDelete.as_view(), name='lesson_delete'),
    url(r'^student/$', views.StudentView.as_view(), name='student'),
    url(r'^student/add/$', views.StudentCreate.as_view(), name='student_add'),
    url(r'^student/update/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student_update'),
    url(r'^student/delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='student_delete'),
    url(r'^student/remove/(?P<studentpk>[0-9]+)/(?P<lessonpk>[0-9]+)$', views.StudentRemove, name='student_remove'),
    url(r'^instructor/$', views.InstructorView.as_view(), name='instructor'),
    url(r'^instructor/add/$', views.InstructorCreate.as_view(), name='instructor_add'),
    url(r'^instructor/delete/(?P<pk>[0-9]+)/$', views.InstructorUpdate.as_view(), name='instructor_update'),
    url(r'^instructor/update/(?P<pk>[0-9]+)/$', views.InstructorDelete.as_view(), name='instructor_delete'),
    url(r'^student/enroll/$', views.StudentEnrollCreate.as_view(), name='student_enroll'),
    url(r'^instructor/assign/$', views.InstructorAssignCreate.as_view(), name='instructor_assign'),
    url(r'^class/enrollment/(?P<pk>[0-9]+)/$', views.ClassEnrollment, name='class_enrollment')

    ]