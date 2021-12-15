from django.contrib import admin
from django.urls import path
from Todo.views import home, del_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', home, name="home"),
    path('todo/<int:son>/', del_list, name='del_list')
]
