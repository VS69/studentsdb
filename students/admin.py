from django.contrib import admin
from .models.student import Student
from .models.group import Group
from .models.monthjournal import MonthJournal


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(MonthJournal)
