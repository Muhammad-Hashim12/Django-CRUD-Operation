from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('show/',show,name='show'),
    path('delete/',delete,name='delete'),
    path('edit/',edit,name='edit'),
    path('recordedited/',recordedited,name='recordedited')
]

