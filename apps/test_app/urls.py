from django.urls import path
from test_app import views

app_name = 'test_app'
urlpatterns = [
    path('test-page/', views.test_page, name='test_page'),
]
