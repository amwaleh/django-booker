from django import forms
from assess.models import Books, Categories


class FormSearch(forms.Form):
     CATEGORIES =[('null','')]
     CATEGORIES.append(Categories.objects.values_list('id','Category')[1])
     search=forms.CharField(label="Search", max_length=64)
     category=forms.ChoiceField(label="category", choices=CATEGORIES)

class FormBooks(forms.ModelForm):

    class Meta:
        model = Books
        fields = "__all__"


class FormCategories( forms.ModelForm):

    class Meta:
        model = Categories
        fields = '__all__'




