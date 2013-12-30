from django.db import models
from django.forms import ModelForm
from django.contrib import admin


class Book(models.Model):
  author = models.CharField(max_length=255)
  pub_year = models.IntegerField()
  pub_org = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=4096)

  def get_absolute_url(self):
    return self.absolute_url

  def __unicode__(self):
    return self.title

  @property
  def absolute_url(self):
    return '/app/books/' + str(self.id) + '/'


class BookForm(ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'author', 'pub_year', 'pub_org', 'description']


admin.site.register(Book)

