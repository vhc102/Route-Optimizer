import googlemaps
import csv
import requests
from django.conf import settings

gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)


def load_fuel_prices_from_csv(file_path):
    fuel_prices = {}

    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            state = row["State"]
            price = float(row["Retail Price"])
            if state not in fuel_prices:
                fuel_prices[state] = []
            fuel_prices[state].append(price)

    for state in fuel_prices:
        fuel_prices[state] = sum(fuel_prices[state]) / len(fuel_prices[state])

    return fuel_prices


def get_route_data(origin, destination):
    try:
        directions = gmaps.directions(
            origin=origin,
            destination=destination,
            mode="driving"
        )
        if not directions:
            raise ValueError("Route not found.")

        route = directions[0]["legs"][0]
        total_distance = route["distance"]["value"] / 1609.34  # Convert meters to miles
        steps = route["steps"]

        return {
            "total_distance": total_distance,
            "steps": [{"location": step["end_location"], "distance": step["distance"]["value"]} for step in steps],
        }
    except googlemaps.exceptions.ApiError:
        raise ValueError("Route not found.")


def calculate_fuel_cost(route_data, csv_file_path, mpg=10, max_range=500):
    fuel_prices = load_fuel_prices_from_csv(csv_file_path)
    total_distance = route_data["total_distance"]
    steps = route_data["steps"]

    stops = []
    remaining_range = max_range
    total_cost = 0

    for step in steps:
        distance = step["distance"] / 1609.34  # Convert meters to miles
        remaining_range -= distance

        if remaining_range <= 0:
            stop_location = step["location"]
            state = find_state_from_location(stop_location)
            fuel_price = fuel_prices.get(state, 3.5)  # Default to $3.5 if state not found
            cost = (max_range / mpg) * fuel_price
            total_cost += cost
            stops.append({"location": stop_location, "cost": cost})
            remaining_range = max_range

    if remaining_range < total_distance:
        remaining_distance = total_distance % max_range
        stop_location = steps[-1]["location"]
        state = find_state_from_location(stop_location)
        fuel_price = fuel_prices.get(state, 3.5)
        cost = (remaining_distance / mpg) * fuel_price
        total_cost += cost
        stops.append({"location": stop_location, "cost": cost})

    return {"stops": stops, "total_cost": total_cost}


def find_state_from_location(location):
    geocode_result = gmaps.reverse_geocode((location["lat"], location["lng"]))
    for result in geocode_result:
        for component in result["address_components"]:
            if "administrative_area_level_1" in component["types"]:
                return component["long_name"]
    return None


def get_gas_stations_nearby(lat, lng, radius=500, api_key=None):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "type": "gas_station",
        "key": api_key,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        raise Exception(f"Places API Error: {response.text}")


def find_gas_stations_along_route(route_data, radius=500):
    api_key = settings.GOOGLE_MAPS_API_KEY
    steps = route_data.get("steps", [])
    gas_stations = []

    for step in steps:
        location = step["location"]
        lat, lng = location["lat"], location["lng"]

        stations = get_gas_stations_nearby(lat, lng, radius, api_key)
        gas_stations.append({
            "location": location,
            "stations": stations,
        })

    return gas_stations
