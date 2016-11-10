# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.student import Student
from ..models.group import Group
from ..util import paginate


# Views for students
def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    else:
        students = students.order_by('last_name')

    # apply pagination, 3 students per page
    context = paginate(students, 3, request, {}, var_name='students')

    return render(request, 'students/students_list.html', context)


def students_add(request):
    # was form posted?
    if request.method == 'POST':
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user
            errors = {}

            # if input data without errors:
            if not errors:
                # create student object
                student = Student(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    middle_name=request.POST['middle_name'],
                    birthday=request.POST['birthday'],
                    photo=request.FILES['photo'],
                    ticket=request.POST['ticket'],
                    student_group=Group.objects.get(pk=request.POST[
                        'student_group']),
                    notes=request.POST['notes'],
                )

                # save it to database
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(reverse('home'))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})

        # was form cancel button clicked?
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)
