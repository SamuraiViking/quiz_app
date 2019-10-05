from django.db import models

class Course(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Associations 
    name = models.CharField(max_length=200)
    # functions
    def __str__(self):
        return self.name

class Quiz(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Attributes
    name = models.CharField(max_length=200, default='')
    # Assocations
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # functions
    def __str__(self):
        return self.name

class Question(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Attributes
    question_text = models.CharField(max_length=200, default='')
    answer_text = models.CharField(max_length=200, default='')
    is_multiple_choice = models.BooleanField(default=False)
    # Assocations
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    #functions
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Attributes
    answer_text = models.CharField(max_length=200, default='')
    is_answer = models.BooleanField(default=False)
    # Associations
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # functions
    def __str__(self):
        return answer_text
