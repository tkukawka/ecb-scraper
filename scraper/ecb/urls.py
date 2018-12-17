from django.urls import path

from . import views
from .settings import SCRAPE_INTERVAL
from .tasks import start_background_scraper

start_background_scraper(interval=SCRAPE_INTERVAL)

urlpatterns = [
    path('feed/currency/', views.CurrencyView.as_view(), name='currency_feed'),
]

