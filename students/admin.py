from django.contrib import admin
from .models.student import Student
from .models.group import Group
from .models.monthjournal import MonthJournal
from .models.exam import Exam


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(MonthJournal)
admin.site.register(Exam)
