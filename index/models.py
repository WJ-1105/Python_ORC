from django.db import models
# Create your models here.
class image_to_json(models.Model):
    # id = models.AutoField(primary_key=True)
    movie_image = models.FileField(upload_to='image/', default='image/default.png')
    data = models.JSONField(default = {})

    def __str__(self):
        return self.id