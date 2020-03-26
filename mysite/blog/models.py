from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    numexp =models.SmallIntegerField() #models.ForeignKey('auth.User', on_delete=models.CASCADE)
    anio = models.SmallIntegerField() #models.CharField(max_length=200)
    quejoso = models.TextField()
    fecarc = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=3)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.numexp) + "/" + str(self.anio)
