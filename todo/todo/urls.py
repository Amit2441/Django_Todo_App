from django.contrib import admin
from django.urls import path,include
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('additem/', views.additem),
    path('deleteitem/<int:todo_id>/',views.deleteitem)


]
