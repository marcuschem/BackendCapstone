from django.urls import path
from .views import IndexView


urlpatterns = [
    # index page
    path('', IndexView.as_view(), name="index"),
]
