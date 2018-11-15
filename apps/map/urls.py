from django.urls import path
from map import views

app_name = 'map'
urlpatterns = [
    path('map-view/', views.map_view, name='map_view'),
]
