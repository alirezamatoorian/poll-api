from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'pool-app'

router = DefaultRouter()

router.register(r'polls', views.PollViewSet, basename='polls')

urlpatterns = [

]

urlpatterns += router.urls
