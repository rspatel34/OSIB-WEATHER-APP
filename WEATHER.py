#CODE BY PATEL RUDRA SHAILESHBHAI
#OASIS INFOBYTE PYTHON PROGRAMMING INTERNSHIP

#Importing Libraries
import requests
import argparse

#Integrating API
API_KEY = "a57f6bf10a25d4b21ae97582f0392507"  #API Key Using Open Weather
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  #URL

def get_weather(location):
 #API Request
  params = {
    "q": location,
    "appid": API_KEY,
    "units": "metric" 
  }
  response = requests.get(BASE_URL, params=params)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return None

def display_weather(weather_data):
#Displaying Weather Data
  if not weather_data:
    return

  city = weather_data["name"] 
  temp = weather_data["main"]["temp"]
  humidity = weather_data["main"]["humidity"]
  description = weather_data["weather"][0]["description"]

  print(f"Weather in {city}:")                     #Displays Weather of User's Input City
  print(f"  Temperature: {temp:.2f}°C")     #Displays Temperature of User's Input City
  print(f"  Humidity: {humidity}%")          #Displays Humidity of User's Input City
  print(f"  Description: {description}")      #Displays Description of User's Input City

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Get current weather information.")
  parser.add_argument("location", help="City name or ZIP code")
  args = parser.parse_args()

  weather_data = get_weather(args.location)
  display_weather(weather_data)
