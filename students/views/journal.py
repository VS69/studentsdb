# -*- coding: utf-8 -*-

from django.shortcuts import render
from ..models.journal import Journal


# Views for journal
def journal_edit(request):
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
    return render(request, 'students/journal.html', {'students': students})
