from .models import Profile,Card
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.authtoken.models import Token

class ProfileSer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','mobile_no','home_no','address','website','position','profile_pic',]

class UserSer(serializers.ModelSerializer):
    users=ProfileSer()
    class Meta:
        model=User
        fields=['id','username','email','password','users']
    
    def create(self, validated_data):
        data = validated_data.pop('users')
        account=User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        passwrod=self.validated_data['password']
        account.set_password(passwrod)
        account.save()
        print(data)
        mob=data['mobile_no']
        home=data['home_no']
        address=data['address']
        website=data['website']
        position=data['position']
        profile_pic=data['profile_pic']
        token=Token.objects.get(user=account).key
        data['token']=token
        Profile.objects.create(user=account, mobile_no=mob,home_no=home,address=address,website=website,position=position)
        return account

    def update(self, instance, validated_data):
        u=validated_data.pop('users')
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        instance.save()
        x=(Profile.objects.get(user=instance.id))
        x.mobile_no=u['mobile_no']
        x.home_no=u['home_no']
        x.address=u['address']
        x.website=u['website']
        x.position=u['position']
        x.profile_pic=u['profile_pic']
        x.save()
        return instance
           
class CardSer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields='__all__'




