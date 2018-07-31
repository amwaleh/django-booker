from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.shortcuts import render,reverse
from django.urls import reverse
from library.forms import FormBooks
from library.models import Books, Authors
# Create your views here.
class Home(TemplateView):
    '''
    Handles the home page

    '''
    template_name="index.html"

    def get(self,request, *args, **kwargs):
        form = FormBooks(request.POST)
        return render(request, self.template_name,{"form":form, "action":reverse('index')})

    def post(self,request, *args, **kwargs):
        form = FormBooks(request.POST)
        if form.is_valid():

            result = form.save()
            content={
            "title":"Authors",
            "action": reverse('index'),
            "content": Authors.objects.all(),
            "form":form
            }
            return render(request, self.template_name,content)
        return redirect(reverse('index'))
