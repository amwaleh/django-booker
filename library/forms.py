from django import forms
from library.models import Authors, Publishers, Books

class FormBooks(forms.ModelForm):
    class Meta:
        model = Authors
        fields='__all__'

class FormPublishers(forms.ModelForm):
    class Meta:
        model = Publishers
        fields='__all__'
