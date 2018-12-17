from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core import serializers
from django.http import Http404
from .models import RSSFeedModel
from .settings import FILTERS, CURRENCIES_TO_SCRAPE
import datetime


class CurrencyView(View):

    def get(self, request):
        query_dict = self.get_filters(**dict(request.GET))
        try:
            filtered_data = RSSFeedModel.objects.filter(**query_dict).defer()
            filtered_data.order_by('date')
        except Exception:
            raise Http404("Currency Data with given input not found {}".format(query_dict))
        data = serializers.serialize("json", filtered_data)
        return HttpResponse(data, content_type='application/json')

    def get_filters(self, **kwargs):
        incorrect_filter = []
        filtered_params = dict()
        for query_param, value in kwargs.items():
            if query_param in FILTERS:
                if query_param == 'date':
                    # validate data
                    try:
                        datetime.datetime.strptime(value[0], "%Y-%m-%d")
                    except ValueError as err:
                            raise err

                    filtered_params['date__range'] = [value[0]+'T00:00:00Z', value[0]+'T23:59:59Z']

                elif query_param == 'target':
                    if value[0] in CURRENCIES_TO_SCRAPE:
                        filtered_params[query_param] = value[0]
                    else:
                        raise ValueError("Unallowed target currency passed: {}".format(value[0]))
                else:
                    filtered_params[query_param] = value[0]
            else:
                incorrect_filter.append(query_param)

        if len(kwargs) == 0:
            print("No Filters Applied")
            return {}

        if len(incorrect_filter) > 0:
            print("Filters Incorrect: {}".format(incorrect_filter))

        return filtered_params
