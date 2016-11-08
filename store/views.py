from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from store.forms import FormBooks
# Create your views here.
class Home(TemplateView):
    template_name="index.html"

    def get(self,request, *args, **kwargs):
        form = FormBooks(request.POST)

        return render(request, self.template_name,{"content":form})
