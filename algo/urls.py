from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AlgoInfoList.as_view(), name='algo_list'),
    url(r'^create', views.AlgoInfoCreate.as_view(), name='algo_create'),
    url(r'^list', views.AlgoInfoList.as_view(), name='algo_list'),
    url(r'^chart/(?P<algo_id>\d+)/', views.pnl_chart_view, name='algo_chart'),
]
