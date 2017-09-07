from django.shortcuts import render, render_to_response
from .models import AlgoInfo
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
import requests
from algo.util.TrendFollowing import algo_result


class AlgoInfoCreate(CreateView):
    model = AlgoInfo
    fields = ['name', 'trade', 'ticker', 'signal']
    template_name = "algo/create.html"
    success_url = reverse_lazy("algo_list")


class AlgoInfoList(ListView):
    model = AlgoInfo
    fields = ['name', 'trade', 'ticker', 'signal']
    template_name = "algo/list.html"


def index(request):
    return render(request, 'algo/index.html')


def pnl_chart_view(request, algo_id=None):
    algo =  AlgoInfo.objects.get(id=algo_id)

    trigger = algo.signal if algo.signal else '2 days moving average larger than 5 days moving average'
    trade = algo.trade if algo.trade else 'buy 50 shares'

    url = 'https://api.iextrading.com/1.0/stock/{}/chart/2y'.format(algo.ticker)
    response = requests.get(url)
    data = response.json()
    prices = []

    for item in data:
        prices.append(item['high'])

    positions, pnl_data = algo_result(trigger, trade, prices)
    pnl_data_chart = []
    for idx, val in enumerate(positions):
        pnl_data_chart.append({'position':val,'PNL': pnl_data[idx]})


    return render(request, 'algo/chart.html', {
        #'data': data,
        'data':pnl_data_chart,
        # 'prices':prices,
        'name': algo.name
    })