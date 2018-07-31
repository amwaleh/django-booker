from django.conf.urls import url
from  assess import views

urlpatterns= [
    url(r'^$', views.Index.as_view(), name="books"),
    url(r'^categories/$', views.CategoriesView.as_view(), name="categories"),
    url(r'^search/$', views.Search.as_view(), name="search"),
    url(r'^search/(?P<pk>[0-9]+)/$', views.FetchBook.as_view(), name="book"),
    url(r'^books/(?P<pk>[0-9]+)/delete/$', views.DeleteBook.as_view(), name="delete_book"),

]