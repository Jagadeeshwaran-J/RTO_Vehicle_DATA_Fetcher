import requests
import json

url = "https://rto-vehicle-information-india.p.rapidapi.com/getVehicleInfo"

payload = {
    "vehicle_no": "YOUR-VEHICLE-NO",
    "consent": "Y",
    "consent_text": "I hereby give my consent for Eccentric Labs API to fetch my information"
}
headers = {
    "x-rapidapi-key": "YOUR-rapidapi-key",
    "x-rapidapi-host": "rto-vehicle-information-india.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print('Vehicle Information Using RapidAPI')
print('----------------------------------')
print(response.json())

# Save result as JSON file
with open("vehicle_info.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, indent=4, ensure_ascii=False)

print("Response saved to vehicle_info.json")
