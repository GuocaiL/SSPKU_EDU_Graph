"""PKUKnowledgeBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import recogentity
from . import settings
from . import search_view
from django.conf.urls.static import static


urlpatterns = [

    path(r'', recogentity.recogentity.index_view),
    path('recogentity.recog_entity', recogentity.recogentity.recog_entity),
    path('search_entity',search_view.search_entity),
    path('search_relation',search_view.search_relation),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

