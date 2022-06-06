"""permission URL Configuration

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
from django.urls import path, include
from api1 import views
from rest_framework.routers import DefaultRouter

# router  object
router = DefaultRouter()

#router.register('Employee', views.EmployeeViewSet, basename='employee')
router.register('student', views.StudentDjangoPModelViewSet,
                basename='Student')
router.register('studentp', views.StudentDjangoModelViewSet,
                basename='studentp')
router.register('studentIs', views.StudentModelViewSet,
                basename='StudentIs')
router.register('studentread', views.StudentReadModelViewSet,
                basename='Studentread')
router.register('studentadmin', views.StudentAdminModelViewSet,
                basename='Studentadmin ')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
