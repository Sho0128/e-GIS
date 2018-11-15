from django.db import models


class TestModel(models.Model):
    name = models.CharField('名前', max_length=255)
    value = models.IntegerField('値', blank=True, default=0)

    def __str__(self):
        return self.name
