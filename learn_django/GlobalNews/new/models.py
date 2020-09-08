from django.db import models as m
from django.contrib.auth.models import User
from django.utils.text import slugify

class New(m.Model):
    added_by = m.ForeignKey('Xəbərçi', User, on_delete=m.SET_NULL)
    title = m.CharField('Başlıq', max_length=100)
    image = m.ImageField(upload_to = '/pictures/')
    url = m.URLField('Link',default=None, null=True)
    slug = slugify(title)
    body = m.TextField('Xəbər')
    date_created = m.DateTimeField('Yaradılma tarixi', auto_now_add=True)


