from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from django.conf.urls import url 
router = DefaultRouter()
router.register('profile',UserView)

# router.register('profile',views.ProfileView)
router.register('register',views.UserView)
router.register('card',views.CardView)


urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.reg,name="register"),
    path('login/',views.login,name="login") ,
    path('logout/',views.Logout.as_view(),name="logout") ,
    path('card/delete/<int:pk>/',views.destroy)  ,
    path('card/update/<int:pk>/',views.update)  ,

    # ===============================================
  
    ]