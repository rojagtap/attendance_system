from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import *
import datetime


def index(request):
    return render(request, 'attendance/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('attendance:home')
            else:
                return render(request, 'attendance/login.html', {'error_message': 'Your account is not active.'})
        else:
            return render(request, 'attendance/login.html', {'error_message': 'Invalid login'})
    return render(request, 'attendance/login.html')


def logout_user(request):
    logout(request)
    return redirect('attendance:login_user')


def home(request):
    if not request.user.is_authenticated:
        return redirect('attendance:login_user')

    get_defaulters(request)
    subjects = request.user.subject.all().values()

    for subject in subjects:
        subject['where'] = request.user.subject.where.all().values()

    return render(request, 'attendance/home.html', {'subjects': subjects})


def add(request, subject, where):
    if request.method == "POST":
        lecture = Lecture()
        lecture.faculty = request.user
        lecture.subject = get_object_or_404(Subject, pk=subject)
        lecture.where = get_object_or_404(Class, pk=where)
        lecture.date = datetime.datetime.strptime(request.POST.get("date"), "%Y-%m-%d").date()
        lecture.time_from = int(request.POST.get("time_from"))
        lecture.time_to = int(request.POST.get("time_to"))

        attendance = request.POST.get("attendance")
        attendance = list(map(int, attendance.split(',')))
        excluded = request.POST.get("excluded")
        lecture.save()

        if not excluded:
            all = Student.objects.all()
            attendance_excluded = list()
            for a in all:
                if a.roll not in attendance:
                    attendance_excluded.append(a.roll)

            student = get_list_or_404(Student, roll__in=attendance_excluded)
        else:
            student = get_list_or_404(Student, roll__in=attendance)

        print(student)
        for s in student:
            lecture.student.add(s)
        lecture.save()
        return redirect('attendance:home')

    return render(request, "attendance/add.html")


def get_defaulters(request):
    classes = Class.objects.all()
    attendance = []
    students = {}

    for clas in classes:
        temp1 = [0] * clas.strength
        temp2 = {}
        for subject in clas.subject_set.all():
            temp2[subject.pk] = temp1[:]

        students[clas.pk] = temp2.copy()

    for clas in classes:
        for subject in clas.subject_set.all():
            attendance.append(Lecture.objects.filter(where__name=clas.name, subject__exact=subject))

    for att in attendance:
        lec_count = len(att)
        for query in att:
            for student in query.student.all():
                students[query.where.pk][query.subject.pk][student.roll - 1] += 1

    print(students)