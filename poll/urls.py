from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'pool-app'

router = DefaultRouter()

router.register(r'polls', views.PollViewSet, basename='polls')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh-token')

]

urlpatterns += router.urls
