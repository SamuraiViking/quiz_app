from django.shortcuts import render, get_object_or_404
from .models import Course, Quiz

def CoursesIndex(request):
    courses = Course.objects.all()
    context = { 'courses': courses }
    return render(request, 'quizzes/coursesIndex.html', context)

def CourseDetail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = course.quiz_set.all()
    context = {
        'quizzes': quizzes,
        'course' : course,
    }
    return render(request, 'quizzes/coursesDetail.html', context)

def QuizDetail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    context = {
        'quiz' : quiz,
        'questions' : questions,
    }
    return render(request, 'quizzes/quizDetail.html', context)



# Create your views here.
