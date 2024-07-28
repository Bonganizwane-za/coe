from django.urls import path
from . import views

urlpatterns = [
    path('flask_chatbot/', views.flask_proxy, name='flask_proxy'),
]