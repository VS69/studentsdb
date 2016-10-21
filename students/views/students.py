# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Володимир',
         'last_name': u'Салітринський',
         'ticket': 235,
         'image': 'img/st01.jpg'},
        {'id': 2,
         'first_name': u'Іван',
         'last_name': u'Іванов',
         'ticket': 2123,
         'image': 'img/st02.jpg'},
        {'id': 3,
         'first_name': u'Петро',
         'last_name': u'Петров',
         'ticket': 1536,
         'image': 'img/st03.jpg'},
    )
    return render(request, 'students/students_list.html',
                  {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)