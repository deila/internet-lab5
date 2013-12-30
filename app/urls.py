from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.books_index),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Books RESTful
    url(r'^app/books/$',                         views.books_index      ),
    url(r'^app/books/new/$',                     views.books_new        ),
    url(r'^app/books/create/$',                  views.books_create     ),
    url(r'^app/books/(?P<id>[^/]*)/$',           views.books_show       ),
    url(r'^app/books/(?P<id>[^/]*)/edit/$',      views.books_edit       ),
    url(r'^app/books/(?P<id>[^/]*)/update/$',    views.books_update     ),
    url(r'^app/books/(?P<id>[^/]*)/destroy/$',   views.books_destroy    ),
)
