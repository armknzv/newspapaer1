from django.urls import path
from .views import UserUpdateView, upgrade_me


urlpatterns = [
    path('account/', UserUpdateView.as_view()),
    path('upgrade/', upgrade_me, name='upgrade')
]
