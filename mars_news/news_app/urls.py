from django.urls import path
from .views import login_view, register, main_page, register_view

urlpatterns = [
    path('', view = main_page),
    path('login/', view=login_view, name='login'),
    path('register/', view=register_view, name='register'),
]



