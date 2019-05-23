from django.urls import path
from .views import *

urlpatterns = [
		path('' , wbz_all , name = 'wbz_all'),
]