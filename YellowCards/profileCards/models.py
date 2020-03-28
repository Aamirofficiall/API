from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="users")
    phone_numbers=models.CharField(max_length=30,choices=Numbers.objects.all(),default='home')
    address=models.TextField()
    website=models.URLField(null=True)
    position=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to='media/Profile/',null=True)
    


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    card_back=models.ImageField(upload_to='media/Card/')
    card_front=models.ImageField(upload_to='media/Card/',null=True)
    company=models.CharField(max_length=30)
    designation=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.TextField()
    website=models.URLField()
    fax_no=models.CharField(max_length=20,null=True)
    fb_link=models.URLField(null=True)
    twitter_link=models.URLField(null=True)
    linked_in_link=models.URLField(null=True)
    def __str__(self):
        return self.id
    

@receiver(post_save,sender=User)
def crete_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



