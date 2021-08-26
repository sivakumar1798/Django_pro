from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myview, name='myview'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('Insertrecord/',views.Insertrecord, name='Insertrecord'),
     path('show/',views.show, name='show'),

]