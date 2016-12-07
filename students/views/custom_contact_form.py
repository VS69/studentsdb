# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse

from collections import OrderedDict

from contact_form.forms import ContactForm
from contact_form.views import ContactFormView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from studentsdb.settings import ADMIN_EMAIL


class CustomContactForm(ContactForm):
    def __init__(self, request, *args, **kwargs):
        # call original initializator
        super(CustomContactForm, self).__init__(request=request,
                                                *args, **kwargs)

        fields_key = ['from_email', 'subject_template_name', 'message']
        self.fields = OrderedDict((field_name, self.fields[field_name])
                                  for field_name in fields_key)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('contact-form')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))

    from_email = forms.EmailField(
        label=u"Ваша e-mail адреса"
    )

    recipient_list = [ADMIN_EMAIL]

    subject_template_name = forms.CharField(
        label=u"Заголовок листа",
        max_length=128
    )

    message = forms.CharField(
        label=u"Текст повідомлення",
        max_length=2560,
        widget=forms.Textarea
    )


class CustomContactFormView(ContactFormView):
    recipient_list = [ADMIN_EMAIL]
    form_class = CustomContactForm
    template_name = 'contact_form/contact_form.html'

    def get_success_url(self):
        return reverse('contact_form_sent')

    def get_form_kwargs(self):
        kwargs = super(CustomContactFormView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(CustomContactFormView, self).form_valid(form)
