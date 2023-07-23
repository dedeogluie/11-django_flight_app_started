
from django.urls import path
from .views import FlightListCreate ,RezervationListCreate,PassengerListCreate,FlightUptadeDelete ,PassengerUptadeDelete,FlightListView

# Three modules for swagger:


urlpatterns = [
    path('flight/',FlightListCreate.as_view()),
    path ('rezervasyon/', RezervationListCreate.as_view()),
    path('passenger/' , PassengerListCreate.as_view()),
    path('flight/<str:flight>/', FlightUptadeDelete.as_view()),
    path('passenger/<int:pk>/', PassengerUptadeDelete.as_view()),
    path('flights/', FlightListView.as_view()),
]