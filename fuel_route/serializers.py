from rest_framework import serializers
from .utils import get_route_data, calculate_fuel_cost, find_gas_stations_along_route
from django.conf import settings
import os


class RouteRequestSerializer(serializers.Serializer):
    start = serializers.CharField(required=True)
    finish = serializers.CharField(required=True)

    def validate(self, data):
        start = data.get("start")
        finish = data.get("finish")

        try:
            route_data = get_route_data(start, finish)
        except ValueError as e:
            raise serializers.ValidationError({"route": str(e)})

        data["route_data"] = route_data
        return data

    def calculate_details(self):
        route_data = self.validated_data.get("route_data")
        csv_file_path = os.path.join(settings.BASE_DIR, "fuel-prices-for-be-assessment.csv")

        fuel_cost_data = calculate_fuel_cost(route_data, csv_file_path)

        gas_stations = find_gas_stations_along_route(route_data)

        return {
            "route": route_data,
            "fuel_costs": fuel_cost_data,
            "gas_stations": gas_stations,
        }
