from django.urls import path, include #안넣어도 되나?.. 
from .views import ReadAPI, WriteAPI #만드는 함수들 이름

urlpatterns = [ 

path("write/", WriteAPI),
path("read/", ReadAPI),

]
