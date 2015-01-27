# coding: utf-8
from datetime import date
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, ButtonHolder
from crispy_forms.bootstrap import StrictButton
from envelope.forms import BaseContactForm
from haystack.forms import FacetedSearchForm


class UserProfileForm(forms.Form):
    first_name = forms.CharField(label=_('first name'), required=True)
    last_name = forms.CharField(label=_('last name'), required=True)
    email = forms.CharField(label=_('email address'), required=True)
    old_password = forms.CharField(label=_('old password'),
                                   widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(label=_('new password'),
                                   widget=forms.PasswordInput, required=False)
    repeat_password = forms.CharField(label=_('repeat password'),
                                      widget=forms.PasswordInput, required=False)

    def clean_old_password(self):
        """Check old password is correct."""
        data = self.cleaned_data['old_password']
        if len(data) > 0:
            # Check old password
            from django.contrib.auth import authenticate
            user_check = authenticate(username=self.user.username, password=data)
            if user_check is None:
                raise forms.ValidationError(_("Old password is not correct"))
        return data

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()

        new_password = self.cleaned_data.get('new_password', None)
        repeat_password = self.cleaned_data.get('repeat_password', None)
        old_password = self.cleaned_data.get('old_password', None)

        if new_password:
            if new_password != repeat_password:
                raise forms.ValidationError(_("New and repeat passwords don't match"))

            if not old_password:
                raise forms.ValidationError(
                    _("You must indicate old password to change it"))

        return cleaned_data

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        submit_button = StrictButton(
            _('%s Save') % '<span class="glyphicon glyphicon-save"></span>',
            css_class='btn btn-primary',
            type='submit')
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            Fieldset(
                _('Change password (optional)'),
                'old_password',
                'new_password',
                'repeat_password',
            ),
            ButtonHolder(
                HTML('<div class="col-lg-3"></div>'),
                submit_button,
            )
        )
        self.user = kwargs.pop('user')
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.user.first_name
        self.fields['last_name'].initial = self.user.last_name
        self.fields['email'].initial = self.user.email


class WebContactForm(BaseContactForm):
    institution = forms.CharField(label=_('institution/association'), required=False)
    location = forms.CharField(label=_('location'), required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        submit_button = StrictButton(
            _('%s  Send message') % '<span class="glyphicon glyphicon-envelope white"></span>',
            css_class='btn btn-primary',
            type='submit')
        self.helper.layout = Layout(
            HTML("{% load envelope_tags %}{% antispam_fields %}"),
            'sender',
            'email',
            'institution',
            'location',
            Fieldset(
                _('Message'),
                'subject',
                'message'
            ),
            ButtonHolder(
                HTML('<div class="col-lg-3"></div>'),
                submit_button,
            )
        )
        super(WebContactForm, self).__init__(*args, **kwargs)
        if 'category' in self.fields:
            self.fields['category'].required = False

    # def get_context(self):
    #     raise AttributeError('Prova')
    #     return self.cleaned_data.copy()


class YearFacetedModelSearchForm(FacetedSearchForm):
    year = forms.IntegerField(required=False, widget=forms.HiddenInput)

    def search(self):
        sqs = super(YearFacetedModelSearchForm, self).search()

        sqs = sqs.date_facet(
            'pub_date',
            start_date=date(2000, 1, 1),
            end_date=date.today(),
            gap_by='year')

        if hasattr(self, 'cleaned_data') and self.cleaned_data['year']:
            year = self.cleaned_data['year']
            sqs = sqs.narrow("pub_date:[{d1} TO {d2}]".format(
                d1=date(year, 1, 1).isoformat(),
                d2=date(year + 1, 1, 1).isoformat()))
        return sqs
