"""
Pull data from web services

An API (Application Programming Interface)
like a waiter at a restaurant. 
You tell it what you want, and it brings you the data.

But APIs do more than just fetch information. 
They are the bridges that connect your code to other systems. With APIs, you can:
- Pull customer data from your CRM (Salesforce, HubSpot)
- Get order information from Shopify or WooCommerce
- Send messages through Slack or email services
- Use AI models from OpenAI or Anthropic

In the context of AI, APIs are essential. 
They let you connect AI capabilities to real business data and systems.

"""

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")

"""
JSON (JavaScript Object Notation) is just a way to structure data, 
similar to CSV or Excel files. While CSV stores data in rows and columns, 
JSON uses key-value pairs like Python dictionaries.
"""

# Homework: Find a temp of Tokyo, London, and Paris

import requests

def get_weather(latitude, longtitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longtitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temp for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp} °C")
print(f"London: {london_temp} °C")
print(f"Tokyo: {tokyo_temp} °C")
