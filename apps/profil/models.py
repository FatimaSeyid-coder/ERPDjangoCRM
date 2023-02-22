from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    Profile_image=models.ImageField(default='default-avatar.png',upload_to='users/',null=True,blank=True)
    
    def __str__(self):
       return '%s %s' % (self.user.first_name,self.user.last_name) 
   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.db import models
Type_CHOICES = [
        ('individu','individu'), 
        ('societe','societe')]
Titre_CHOICES = [
        ('Madame','Madame'), 
        ('Mademoiselle','Mademoiselle'),
        ('Monsieur','Monsieur')]
# Create your models here.
class client(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=500, blank=True)
    lastname = models.CharField(max_length=500, blank=True)
    post = models.CharField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    siteweb = models.CharField(max_length=500, blank=True)
    type = models.CharField(default='individu',max_length = 20,choices=Type_CHOICES)
    titre = models.CharField(default='Madame',max_length = 20,choices=Titre_CHOICES)
    etiquette = models.CharField(max_length=500, blank=True)
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
    
    
class contact(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    name = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=20)
    rue = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    codepostal = models.CharField(max_length=20)
    

class clientpiste(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=500, blank=True)
    lastname = models.CharField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
   
   
class message(models.Model):
    clientpiste = models.ForeignKey(clientpiste, on_delete=models.CASCADE)
    msg=models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)