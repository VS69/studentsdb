# -*- coding: utf-8 -*-

from datetime import datetime
from PIL import Image

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

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
            # errors collection
            errors = {}

            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Імя є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = \
                        u"Введіть коректрий формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                if photo.size >= 2 * 1024 * 1024:
                    errors['photo'] = u"Файл дуже великий. Має бути < 2 Mb"
                else:
                    try:
                        Image.open(photo).verify()
                    except Exception:
                        errors['photo'] = u"Файл не є файлом зображення"
                    else:
                        data['photo'] = photo

            # if input data without errors:
            if not errors:
                # create student object
                student = Student(**data)

                # save it to database
                student.save()

                # redirect user to students list
                messages.info(request,
                              u'Студента %(first_name)s %(last_name)s успішно додано!' %
                              {'first_name': student.first_name,
                               'last_name': student.last_name},
                              )
                return HttpResponseRedirect(reverse('home'))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})

        # was form cancel button clicked?
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.info(request, u'Додавання студента скасовано!', )
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)
