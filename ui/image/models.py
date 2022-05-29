from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    # caption="a"
    image=models.ImageField(upload_to="img/")
    def __str__(self):
        return self.image