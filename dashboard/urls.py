from django.urls import path
from .views import *

urlpatterns = [
    path('get_transaction', get_transaction),
    path('login', loginAPI.as_view()),
    path('', TransactionAPI.as_view())
]
