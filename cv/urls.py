from django.urls import path
from cv.views import initCv

urlpatterns = [
    path('', initCv, name='cv'),
]