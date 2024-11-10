"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from tickets import views
# viewsets
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('geusts',views.GuestViewSet)
router.register('movie',views.MovieViewSet)
router.register('reservation',views.ServationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('no_rest_from_model/',views.no_rest_from_model),
    
    path('FBV_list/',views.FBV_list),
    path('FBV_pk/<int:pk>',views.FBV_pk),
    
    path('Cbv_list/',views.Cbv_list.as_view()),
    path('Cbv_pk/<int:pk>',views.Cbv_pk.as_view()) ,
    
    path('Mixin_list/',views.Mixin_list.as_view()),
    path('mixin_pk/<int:pk>',views.mixin_pk.as_view()),
    
    path('Generic_list/',views.Generic_list.as_view()),
    path('Generic_pk/<int:pk>',views.Generic_pk.as_view()),
    # viewsets
    path('GuestViewSet/',include(router.urls)),
    path('MovieViewSet/',include(router.urls)),
    path('ServationViewSet/',include(router.urls))
]
