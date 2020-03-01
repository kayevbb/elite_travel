from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Pole(models.Model):
    title = models.CharField(max_length=255, verbose_name='Город')
    body = models.TextField(verbose_name='Информация о туре')
    avatar = models.ImageField(upload_to='', verbose_name='Фото')
    photo = models.ImageField(upload_to='', verbose_name='Фото')
    avatar3 = models.ImageField(upload_to='', verbose_name='Фото')
    date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=20, verbose_name='Цена')
    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pole_detail', args=[str(self.id)])


class PoleImage(models.Model):
    image = models.ImageField(upload_to='media/')
    pole = models.ForeignKey(Pole, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.pole.title

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)


class Comment(models.Model):
    article = models.ForeignKey(
        Pole,
        on_delete=models.CASCADE,
        related_name = 'comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('pole_list')


class Reservation(models.Model):
    table = models.ForeignKey('Pole', on_delete=models.CASCADE)
    party = models.CharField(max_length=255)
    spot = models.CharField(max_length=255)
    status = models.BooleanField(default=True)


