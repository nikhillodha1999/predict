import requests

def get_taluka_from_coordinates(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    data = response.json()
    address = data.get("address", {})
    taluka = address.get("town") or address.get("city") or address.get("village") or address.get("hamlet")
    return taluka

# Example coordinates (latitude and longitude)
latitude = 18.7299647
longitude = 73.6699581

taluka = get_taluka_from_coordinates(latitude, longitude)
print("Taluka:", taluka)


