from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from assess.form import FormBooks, FormCategories, FormSearch
from assess.models import Books, Categories
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import Http404


# Create your views here.


class Index(TemplateView):
    template_name = "assess.html"

    def get(self, request, *args, **kwargs):
        context = dict(
            search=FormSearch(),
            form=FormBooks(),
            form_action=reverse('assess:books'),
            result_form=Books.objects.all(),
            title='Add Books',
        )
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormBooks(request.POST)
        if form.is_valid():
            result = form.save()
            messages.info(request,  'book saved')
            context = dict(
                search=FormSearch(),
                result_form=[result],
            )
            return render(request, self.template_name, context)

        messages.error(request,  form.errors.as_text())
        return redirect(reverse('assess:books'))


class DeleteBook(TemplateView):
    template_name = "assess.html"

    def get(self, request, pk, *args, **kwargs):

        Books.objects.filter(id=pk).delete()

        messages.info(request, "Deleted")

        return redirect(reverse('assess:books'))


class CategoriesView(TemplateView):
    template_name = "assess.html"

    def get(self, request, *args, **kwargs):
        context = dict(
            form=FormCategories(),
            form_action=reverse('assess:categories'),
            title='categories',
            result_categories=Categories.objects.all(),
        )
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormCategories(request.POST)
        if form.is_valid():
            data = form.save()
            messages.info(request, 'saved {}'.format(data))
            return redirect(reverse('assess:books'))

        return redirect(reverse('assess:categories'))


class Search(TemplateView):
    template_name = "assess.html"

    def get(self, request, *args, **kwargs):
        context = dict(
            search=FormSearch(),
        )
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        query = request.POST.get('search')
        cat = request.POST.get('category')

        if cat == 'null':
            result = Books.objects.filter(title__icontains=query)
        else:
            result = Books.objects.filter(
                title__icontains=query, category__exact=cat)

        if result:
            context = dict(
                search=FormSearch(),
                result_form=result,
            )
            messages.info(request, 'here are the results')
            return render(request, self.template_name, context)
        messages.error(request, 'Nothing was found')
        return redirect(reverse('assess:search'))


class FetchBook(TemplateView):
    template_name = "assess.html"

    def get(self, request, pk, *args, **kwargs):

        try:
            result = Books.objects.get(pk=pk)
        except:
            messages.error(request, 'Nothing was found')
            return redirect(reverse('assess:search'))

        context = dict(
            search=FormSearch(),
            book_preview=result,
        )
        return render(request, self.template_name, context)
