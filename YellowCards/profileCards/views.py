from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .ser import UserSer,CardSer
from .models import Profile,Card
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from  .ser import UserSer,ProfileSer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,SAFE_METHODS,BasePermission

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS



class CardView(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSer
    permission_classes=[IsAuthenticated]


@api_view(['PUT'])
@permission_classes((IsAuthenticated),)
def update(self, request, pk=None):
        obj=Card.objects.get(pk=pk)
        if obj.user==request.user:
            Response(data={'message':'your are not allowed to update'},status=status.HTTP_404_NOT_FOUND)
       
        if request.method=='PUT':
            ser=CardSer(obj,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(data=ser.data,status=status.HTTP_200_OK)
            return Response(data={'message':' data was not correct '})
        return Response(data={'error':"upser updattion fiald"})

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def destroy(request, pk=None):
        try: 
            card=Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user=request.user
        if card.user!=user:
            return Response({'response':"You don't have permission to delete that"})
        
        if request.method=='DELETE':
            operation=card.delete()
            data={}
            if operation:
                data['success']='Deleted Successfully'
            else:
                data['failure']="delete failed"
            return Response(data=data)
    
   
class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSer




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    
    if  user is None:
        return Response({'error': 'Invalid something wrong heheheh Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


from django.contrib.auth import logout
from rest_framework.views import APIView
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def reg(request):
    
    if request.method=='POST':
        data={}
        ser=UserSer(data=request.data)
        if ser.is_valid():
            account=ser.save()
            data['response']="successfule created"
        else:
            ser.errors
        return Response(data)    
