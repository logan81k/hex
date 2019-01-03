from django.conf.urls import url

from api import views

urlpatterns = [
    # url('', views.IndexView.as_view(), name='index'),
    url('^ex', views.ExceptionView.as_view(), name='ex'),
]
