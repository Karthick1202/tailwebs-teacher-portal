from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Student
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            out=form.cleaned_data
            name=out['name']
            subject=out['subject']
            marks = out ['marks']
            student, created = Student.objects.get_or_create(name=name, subject=subject)
            if not created:
                student.marks += marks
            else:
                student.marks = marks
            student.save()
            return redirect('home')
        else:
            print('==form=',form.errors)
            messages.error(request,form.errors)
    return render(request, 'home.html', {'students': students, 'form': form})


@login_required
def add_or_update_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        marks = int(request.POST.get('marks'))

        student, created = Student.objects.get_or_create(name=name, subject=subject)

        if not created:
            student.marks += marks
        else:
            student.marks = marks
        student.save()

        return redirect('home')


@login_required
def update_student_ajax(request, pk):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=pk)
        student.name = request.POST.get('name')
        student.subject = request.POST.get('subject')
        student.marks = int(request.POST.get('marks'))
        student.save()
        return JsonResponse({'success': True})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('home')


def register_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the new staff member
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = StaffRegistrationForm()
    return render(request, 'register_staff.html', {'form': form})



class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = '/password_reset/done/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = '/reset/done/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

