from django.shortcuts import render
from django.http import HttpResponse

# Views for students
def students_list(request):
    return render(request, 'students/students_list.html', {})

def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)

# Views for groups
def groups_list(request):
    return HttpResponse('<h1>Groups listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete group %s</h1>' % gid)