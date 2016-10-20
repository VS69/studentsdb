# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for groups
def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'АТ-32',
         'captain': u'Іванов Іван'},
        {'id': 2,
         'name': u'АУ-34',
         'captain': u'Петров Петро'},
        {'id': 3,
         'name': u'АУ-35',
         'captain': u'Салітринський Володимир'},
    )
    return render(request, 'students/groups_list.html',
                  {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete group %s</h1>' % gid)
