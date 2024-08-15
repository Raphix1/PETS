from django.db import models

# Create your models here.

class Cats(models.Model):
    chead = models.CharField(max_length=64, default='default')
    c_home = models.CharField(max_length=64)
    chometext = models.TextField()
    chometextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    c_eat = models.CharField(max_length=64)
    ceattext = models.TextField()
    ceattextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    c_med = models.CharField(max_length=64)
    cmedtext = models.TextField()
    cmedtextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    c_toy = models.CharField(max_length=64)
    ctoytext = models.TextField()
    ctoytextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    cimg = models.ImageField(upload_to='p_img', default='default_image.jpg')

class Dogs(models.Model):
    dhead = models.CharField(max_length=64, default='default')
    d_home = models.CharField(max_length=64)
    dhometext = models.TextField()
    dhometextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    d_eat = models.CharField(max_length=64)
    deattext = models.TextField()
    deattextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    d_med = models.CharField(max_length=64)
    dmedtext = models.TextField()
    dmedtextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    d_toy = models.CharField(max_length=64)
    dtoytext = models.TextField()
    dtoytextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    dimg = models.ImageField(upload_to='p_img', default='default_image.jpg')

class Hamsters(models.Model):
    hhead = models.CharField(max_length=64, default='default')
    h_home = models.CharField(max_length=64)
    hhometext = models.TextField()
    hhometextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    h_eat = models.CharField(max_length=64)
    heattext = models.TextField()
    heattextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    h_toy = models.CharField(max_length=64)
    htoytext = models.TextField()
    htoytextimg = models.ImageField(upload_to='p_img', default='default_image.jpg')
    himg = models.ImageField(upload_to='p_img', default='default_image.jpg')

