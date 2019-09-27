from django.db import models
from django.urls import reverse

class Game(models.Model):
    SIZE_TYPE = [
        ('MB', 'MB'),
        ('GB', 'GB'),
    ]
    CATEGORY_TYPE = [
        ('action', 'Action'),
        ('fighting', 'Fighting'),
        ('strategy', 'Strategy'),
        ('horror', 'Horror'),
        ('intelligence', 'Intelligence'),
        ('straighten', 'Straighten'),
        ('old-games', 'Old Games'),
        ('adventures', 'Adventures'),
        ('racing-cars', 'Racing Cars'),
        ('reality-simulation', 'Reality Simulation'),
        ('sport', 'Sport'),
        ('light-entertaining', 'Light Entertaining'),
        ('fiction', 'fiction'),
    ]
    title = models.CharField(max_length=500, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CATEGORY_TYPE)
    description = models.CharField(max_length=30000, null=False, blank=False)
    cpu_l = models.CharField(max_length=200, null=False, blank=False)
    graphic_card_l = models.CharField(max_length=200, null=False, blank=False)
    ram_l = models.CharField(max_length=200, null=False, blank=False)
    cpu_h = models.CharField(max_length=200, null=False, blank=False)
    graphic_card_h = models.CharField(max_length=200, null=False, blank=False)
    ram_h = models.CharField(max_length=200, null=False, blank=False)
    size = models.IntegerField(default=0)
    size_type = models.CharField(max_length=3, null=False, blank=False, choices=SIZE_TYPE, default="MB")
    download_num = models.IntegerField(default=0)
    youtube_iframe = models.CharField(max_length=700, null=False, blank=False)
    download_link = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to='game_image', blank=True, null=True, default='default-profile-image.png')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={
            'pk':self.pk,
            'slug':self.slug
            })




        