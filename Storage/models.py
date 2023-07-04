from django.db import models
from django.urls import reverse
from time import time

class Discipline(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Название дисциплины")
    info = models.TextField(blank=True, db_index=True, verbose_name="Информация о дисциплине")
    is_published = models.BooleanField(default=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return reverse('disc_detail_url', kwargs={'id': self.id})

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Дисциплины'
        verbose_name_plural = 'Дисциплины'

class File(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name="Название файла")
    info = models.TextField(blank=True, db_index=True, verbose_name="Информация о файле")
    time_upload = models.DateTimeField(auto_now=True)
    discipline_id = models.ForeignKey(Discipline, on_delete = models.CASCADE, null=True, verbose_name="Дисциплина")
    upload = models.FileField(upload_to='upload_files/', verbose_name="Загрузить файл")
    
    slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name="URL")
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = 'f-' + str(int(time()))
        super().save(*args, **kwargs)  

    def get_absolute_url(self):
        return reverse('detail_file_url', kwargs={'id': self.id, 'slug': self.slug})

    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return f'{self.title}'
    
    def delete(self, *args, **kwargs):
        self.upload.delete()
        super().delete(*args, **kwargs)

