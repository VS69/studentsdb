# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models.exam import Exam
from ..util import paginate


# Views for exams
def exams_list(request):
    exams = Exam.objects.all()

    # try to order exams list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'date', 'group'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
    else:
        exams = exams.order_by('id')

    # apply pagination, 2 exams per page
    context = paginate(exams, 2, request, {}, var_name='exams')

    return render(request, 'students/exams_list.html', context)


def exams_add(request):
    return HttpResponse('<h1>Exam add form</h1>')


def exams_edit(request, eid):
    return HttpResponse('<h1>Edit exam %s</h1>' % eid)


def exams_delete(request, eid):
    return HttpResponse('<h1>Delete exam %s</h1>' % eid)
