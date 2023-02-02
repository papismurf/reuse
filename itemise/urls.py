from django.urls import path

from itemise import views

urlpatterns = [
    path("bill_json/", views.bill_json),
]
