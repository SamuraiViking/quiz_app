from django.urls import path
from .views import CoursesIndex, CourseDetail, QuizDetail

urlpatterns = [
    path('courses/', CoursesIndex, name='coursesIndex'),
    path('courses/<int:course_id>/', CourseDetail, name='courseDetail'),
    path('quizzes/<int:quiz_id>/', QuizDetail, name='quizDetail')
]