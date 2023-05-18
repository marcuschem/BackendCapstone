from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from .views import IndexView, MenuItemView, SingleMenuItemView


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('menu', MenuItemView.as_view(), name="menu-list"),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

