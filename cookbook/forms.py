from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext as _
from django import forms
from .models import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'category', 'keywords')

        labels = {
            'name': _('Name'),
            'category': _('Category'),
            'keywords': _('Keywords'),
        }

        help_texts = {
            'keywords': _('Ctrl+Click to select multiple keywords'),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', _('Save'), css_class='btn-primary'))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')

        labels = {
            'name': _('Name'),
            'description': _('Description'),
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', _('Save'), css_class='btn-primary'))


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ('name', 'description')

        labels = {
            'name': _('Name'),
            'description': _('Description'),
        }

    def __init__(self, *args, **kwargs):
        super(KeywordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', _('Save'), css_class='btn-primary'))


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'category', 'keywords','path')

        labels = {
            'name': _('Name'),
            'category': _('Category'),
            'keywords': _('Keywords'),
            'path': _('Path'),
        }

        help_texts = {
            'keywords': _('Ctrl+Click to select multiple keywords'),
        }

    def __init__(self, *args, **kwargs):
        super(EditRecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', _('Save'), css_class='btn-primary'))


class ImportForm(forms.Form):
    path = forms.CharField(label=_('Path'))

    def __init__(self, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('import', _('Import'), css_class='btn-primary'))


class BatchEditForm(forms.Form):
    search = forms.CharField(label=_('Search String'))
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('id'), required=False)
    keyword = forms.ModelMultipleChoiceField(queryset=Keyword.objects.all().order_by('id'), required=False)

    def __init__(self, *args, **kwargs):
        super(BatchEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('update', _('Update'), css_class='btn-primary'))