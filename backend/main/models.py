from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Orphan(models.Model):
    #One to many relation (one user can have many items) which can be set with the foreign key model
    #cascade: on deleting the user, the task would also delete
    orphanage = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    child_image = models.ImageField(null=True,blank=True,upload_to="images/")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    age = models.CharField(max_length=2)
    joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['age']