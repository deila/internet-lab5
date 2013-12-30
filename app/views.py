from models import *
from django.shortcuts import render, redirect
from django.core.context_processors import csrf


def renderable(template):
  def fun_wrapper(fun):
    def wrapper(request, *args, **kwargs):
      data, content_type = fun(request, *args, **kwargs)
      data.update(csrf(request))
      return render(request, template + '.html', data, content_type=content_type)
    return wrapper
  return fun_wrapper


def redirectable(fun):
  def wrapper(request, *args, **kwargs):
    to = fun(request, *args, **kwargs)
    return redirect(to)
  return wrapper


@renderable('books/index')
def books_index(request):
  return [{ 'books': list(Book.objects.all()[:10]) }, 'text/html']


@renderable('books/new')
def books_new(request):
  return [{ 'form': BookForm() }, 'text/html']


@redirectable
def books_create(request):
  book = BookForm(request.POST)
  return book.save()


@renderable('books/show')
def books_show(request, id=None):
  return [{ 'book': Book.objects.get(pk=id) }, 'text/html']


@renderable('books/edit')
def books_edit(request, id=None):
  pass


@redirectable
def books_update(request, id=None):
  pass # redirect here


@redirectable
def books_destroy(request, id=None):
  pass # redirect here


