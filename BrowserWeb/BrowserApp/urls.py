from tkinter.font import names

from django.urls import path
from .views import signup_views,success_views
urlpatterns = [
    path('signup/', signup_views),
    path('success', success_views),
]