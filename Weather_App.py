import requests
API_KEY = "your ap key in demo  646b14dee4d39b46e31092730"

def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["code"] != 200:
            print(f"woring: City '{city}' not found.")
            return
        temp = data['main']['temp']
        condition = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']

        print(f"\nWeather Report for {city.title()}")
        print(f"Temperature : {temp}°C")
        print(f"Condition   : {condition}")
        print(f"Humidity    : {humidity}%\n")

    except Exception as e:
        print(f"An error occurred: {e}")
# Main:
def main():
    print("Welcome to the Command-Line Weather App!\n")
    city_name = input("Enter your city name: ").strip()
    if city_name:
        fetch_weather(city_name)
    else:
        print("Please enter a valid city name.")
if __name__ == "__main__":
    main()