"""walletvet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users.views import (
    UserViewSet,
    UserCreatedSet
)
from django.conf.urls.static import static
from django.conf import settings
from animal.views import (
    AnimalViewSet,
    BreedViewSet
)
from auth.views import CustomAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'register', UserCreatedSet)
router.register(r'animal', AnimalViewSet)
router.register(r'breed', BreedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', CustomAuthToken.as_view()),
    path('api/v1/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
