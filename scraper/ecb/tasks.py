import feedparser
from .settings import CURRENCIES_TO_SCRAPE
from .models import RSSFeedModel
from django.db.utils import IntegrityError
import time
import threading


def fetch_rss_feeds(interval=60*60):
    while True:
        for currency in CURRENCIES_TO_SCRAPE:
            d = feedparser.parse('https://www.ecb.europa.eu/rss/fxref-{}.html'.format(currency.lower()))
            save_data(d['entries'])
        time.sleep(interval)  # run thread every minute


def save_data(entries_list):
    for entry in entries_list:
        try:
            record_model = RSSFeedModel(
                target=entry["cb_targetcurrency"],
                date=entry["updated"],
                link=entry["link"],
                exchange_rate=entry["cb_exchangerate"].replace('\n', ' '),
                title=entry["title"],
                summary=entry["summary"]
            )
            record_model.save()
        except IntegrityError as e:
            print("Record exists, skipping: {}".format(entry['link']))


def start_background_scraper(interval):
    t = threading.Thread(target=fetch_rss_feeds, args=[interval], kwargs={})
    t.setDaemon(True)
    t.start()