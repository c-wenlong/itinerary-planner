import googlemaps
import streamlit as st
from shapely.geometry import Point
from geopy.distance import geodesic
from datetime import datetime

GOOGLE_MAPS_API_KEY = st.secrets["MAPS"]["GOOGLE_MAPS_API_KEY"]


class GoogleMapsService:
    def init(self, home: Point | str, work: Point | str):
        self.client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
        self.HOME = self.address_to_coordinates(home) if type(home) == "str" else home
        self.WORK = self.address_to_coordinates(work) if type(work) == "str" else work

    def get_directions(self, origin, destination, mode="transit"):
        # Request directions via public transit
        now = datetime.now()
        directions_result = self.client.directions(
            origin, destination, mode=mode, departure_time=now
        )
        return directions_result

    def validate_address(self, address: str):
        addressvalidation_result = self.client.addressvalidation(
            [address], region="SG", language="en"
        )
        return addressvalidation_result

    # Usage in your Streamlit app
    def main():
        st.title("Location Search")

        selected_place = google_place_search()

        if selected_place:
            st.write("Selected Location:")
            st.write(f"Name: {selected_place['name']}")
            st.write(f"Address: {selected_place['formatted_address']}")
            st.write(f"Coordinates: ({selected_place['lat']}, {selected_place['lng']})")

    def address_to_coordinates(self, address: str) -> Point:
        geocode_result = self.client.geocode(address)
        x = geocode_result[0]["geometry"]["location"]["lat"]
        y = geocode_result[0]["geometry"]["location"]["lng"]
        return Point(x, y)

    def coordinates_to_address(self, point: Point) -> str:
        reverse_geocode_result = self.client.reverse_geocode((point.x, point.y))
        return reverse_geocode_result[0]["formatted_address"]

    def distance_between_points(point_a: Point, point_b: Point, decimal=2) -> float:
        point_a = (point_a.x, point_a.y)
        point_b = (point_b.x, point_b.y)
        distance = geodesic(point_a, point_b)
        return round(distance.kilometers, decimal)

    def sg_st_test(self):
        sg = self.address_to_coordinates("Singapore")
        st = self.address_to_coordinates("Stockholm")
        print(self.distance_between_points(sg, st))

    def ubi_simei_test(self):
        ubi = self.address_to_coordinates("357 Ubi Rd 3, Singapore 404357")
        simei = self.address_to_coordinates("162 Simei Rd, Singapore 520162")
        print(self.distance_between_points(ubi, simei))
