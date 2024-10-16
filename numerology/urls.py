from django.urls import path
from .views import NumerologyBulkCreateView
from numerology import views


urlpatterns = [
    path('api/', NumerologyBulkCreateView.as_view()),
    path('',views.home)
 
]










  