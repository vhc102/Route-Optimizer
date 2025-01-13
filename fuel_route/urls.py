from django.urls import path

from fuel_route.views import FuelRouteView

urlpatterns = [
    path("fuel-route/", FuelRouteView.as_view(), name="fuel_route"),
]
