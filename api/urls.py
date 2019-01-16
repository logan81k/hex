from django.urls import path

from api import views

urlpatterns = [
    # url('', views.IndexView.as_view(), name='index'),
    # path('ex', views.ExceptionView.as_view(), name='ex'),
    path('blocks/<int:number>', views.BlocksView.as_view(), name='blocks'),
    path('tx/<str:tx_hash>', views.TransactionsView.as_view(), name='tx'),
]
