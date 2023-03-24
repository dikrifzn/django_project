from django.db import models

# Create your models here.
class Data(models.Model):
    judul = models.CharField(max_length=25) #--> varchar
    #(max_length=20, blank=True, null=True)
    content = models.TextField() # --> text
    waktu = models.DateTimeField(auto_now_add=True) # --> date
    email = models.EmailField(default='nama@web.com') # --> email --> varchar

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)