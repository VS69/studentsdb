# -*- coding: utf-8 -*-

from django.db import models


class Journal(models.Model):
    """Journal Model"""

    class Meta(object):
        verbose_name = u"Журнал"
        verbose_name_plural = u"Журнали"

    student = models.ForeignKey(
        'Student',
        verbose_name=u"Студент",
        blank=False,
        unique_for_month='date'
    )

    date = models.DateField(
        verbose_name=u"Дата",
        blank=False
    )

    def __unicode__(self):
        return u'%s: %d/%d' % (self.student.last_name, self.date.month,
                               self.date.year)
