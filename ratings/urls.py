from django.urls import path
from .views import Rating_View, Rate_Page
urlpatterns = [
    path('rate/<int:pid>', Rate_Page.as_view(), name='description'),
    path('rate_item',Rating_View.as_view(),name = 'rate_item')
]
