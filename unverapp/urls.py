
from django.urls import path

from unverapp.views import Studentlar,Curslar

urlpatterns = [
    path('stu/',Studentlar ),
    path('cur/',Curslar)

]