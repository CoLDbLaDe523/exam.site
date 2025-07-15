from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Exam, Submission


def index(request):
    exams = Exam.objects.all()
    return render(request, 'exams/index.html', {'exams': exams})


@login_required
def take_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    return render(request, 'exams/take_exam.html', {'exam': exam})


@login_required
def submit_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    questions = exam.questions.all()
    correct = 0
    total = questions.count()

    if request.method != 'POST':
        return redirect('take_exam', pk=pk)

    for question in questions:
        selected_answer_id = request.POST.get(str(question.id))
        if selected_answer_id:
            selected_is_correct = question.answers.filter(id=selected_answer_id, is_correct=True).exists()
            if selected_is_correct:
                correct += 1

    score = round((correct / total) * 100, 2) if total > 0 else 0
    Submission.objects.create(user=request.user, exam=exam, score=score)
    messages.success(request, f'Экзамен сдан! Результат: {score}%')
    return redirect('results')


@login_required
def my_results(request):
    submissions = Submission.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'exams/results.html', {'submissions': submissions})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})