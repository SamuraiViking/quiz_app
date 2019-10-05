from django.contrib import admin

from .models import Course, Quiz, Question, Choice

imported_models = [
    Course, 
    Quiz, 
    Question, 
    Choice
]

for model in imported_models:
    admin.site.register(model)
