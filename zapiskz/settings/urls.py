"""zapiskz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from core.forms import TradeCard
from core.views import MainView, GetCardView, CollectionListView, AddCard, TradeNewCard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('button/', MainView.as_view(), name='button'),
    path('getcard', GetCardView.as_view(), name='getcard'),
    path('collections/', CollectionListView, name='collections'),
    path('addcard/', AddCard.as_view(), name='add_card'),
    path('tradecard/', TradeCard, name='trade_card'),
    path('tradenewcard/', TradeNewCard.as_view(), name='tradenewcard'),
]
