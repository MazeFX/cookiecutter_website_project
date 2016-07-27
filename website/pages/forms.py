# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: pages/forms.py
Creator: MazeFX
Date: 26-7-2016

Python Test docstring.
"""


from django import forms
from django.core.validators import EmailValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

EMPTY_ITEM_ERROR = 'Hey je moet wel invullen!'
EMAIL_FORMAT_ERROR = 'Vul een geldig email adres in.'


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label="Volledige naam",
        max_length=30,
        required=True,
        error_messages={'required': EMPTY_ITEM_ERROR},
    )

    email = forms.CharField(
        label="Email adres",
        max_length=30,
        required=True,
        error_messages={'required': EMPTY_ITEM_ERROR},
        validators=[EmailValidator(
            message=EMAIL_FORMAT_ERROR
        )]
    )

    subject = forms.CharField(
        label="Onderwerp",
        max_length=80,
        required=True,
        error_messages={'required': EMPTY_ITEM_ERROR},
    )

    message = forms.CharField(
        label="Bericht",
        required=True,
        error_messages={'required': EMPTY_ITEM_ERROR},
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ContactForm'
        self.helper.form_class = 'contact-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))
