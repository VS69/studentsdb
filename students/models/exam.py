# -*- coding: utf-8 -*-

from django.db import models


class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name = u"Екзамен"
        verbose_name_plural = u"Екзамени"

    teaching = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Предмет"
    )

    date = models.DateTimeField(
        verbose_name=u"Дата та час проведення",
        blank=False
    )

    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач"
    )

    group = models.OneToOneField(
        'Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    def __unicode__(self):
        return u'%s (%s)' % (self.teaching, self.group.title)
