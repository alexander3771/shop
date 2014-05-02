# coding: utf-8
from django.db import models
from django.conf import settings
import random
from mptt.models import TreeForeignKey, MPTTModel
from tinymce import models as tinymce_models

def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    filename = str(n1) + '_' + str(n2) + '_' + str(n3) + '.jpg'
    return u'%s/%s' % (settings.IMAGE_UPLOAD_DIR, filename)

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=150, default='', blank=True, verbose_name='Категория')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(max_length=200, default='', blank=True, verbose_name='Заголовок', blank=True)
    meta_desc = models.CharField(max_length=200, default='', blank=True, verbose_name='Мета описание', blank=True)
    meta_key = models.CharField(max_length=200, default='', blank=True, verbose_name='Ключевые слова', blank=True)
    slug = models.CharField(max_length=250, default='', blank=True, verbose_name='Урл', blank=True)
    image = models.ImageField(upload_to=make_upload_path, default='', verbose_name='Изображение', blank=True)
    published = models.BooleanField(verbose_name='Опубликован')
    ordering = models.IntegerField(verbose_name='Порядок сортировки', default=0, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Изображение'
    pic.allow_tags = True

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, default='', blank=True, verbose_name='Категория')
    category = models.ManyToManyField(Category, related_name='cat')
    title = models.CharField(max_length=200, default='', blank=True, verbose_name='Заголовок', blank=True)
    meta_desc = models.CharField(max_length=200, default='', blank=True, verbose_name='Мета описание', blank=True)
    meta_key = models.CharField(max_length=200, default='', blank=True, verbose_name='Ключевые слова', blank=True)
    slug = models.CharField(max_length=250, default='', blank=True, verbose_name='Урл', blank=True)
    image = models.ImageField(upload_to=make_upload_path, default='', verbose_name='Изображение', blank=True)
    short_text = tinymce_models.HTMLField(blank=True, verbose_name='Краткое описание')
    full_text = tinymce_models.HTMLField(blank=True, verbose_name='Полное описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена', blank=True, null=True)
    published = models.BooleanField(verbose_name='Опубликован')
    ordering = models.IntegerField(verbose_name='Порядок сортировки', default=0, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Изображение'
    pic.allow_tags = True

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    class MPTTMeta:
        order_insertion_by = ['name']

class ProductImages(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True)
    image = models.ImageField(upload_to=make_upload_path, default='', verbose_name='Изображение', blank=True)

    def __unicode__(self):
        return self.image

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Изображение'
    pic.allow_tags = True

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'

    class MPTTMeta:
        order_insertion_by = ['name']























