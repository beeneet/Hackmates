from django.conf.urls import url
from hmates import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^upcoming/', views.Upcoming_hacks, name='upcoming')


]