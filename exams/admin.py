from django.contrib import admin
from .models import Exam, Question, Answer, Submission

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Submission)