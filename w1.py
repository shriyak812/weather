from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def get_weather(api_key, location, units='metric'):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': location,
        'units': units,
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        t.config(text=int(weather_data['main']['temp'] - 273.15), fg="#ee666d", font=("arial", 70, "bold"))
        c.config(text=(weather_data['weather'][0]['main'], "|", "FEELS", "LIKE", int(weather_data['main']['temp'] - 273.15), "°"))
        w.config(text=weather_data['wind']['speed'])
        h.config(text=weather_data['main']['humidity'])
        d.config(text=weather_data['weather'][0]['description'])
        p.config(text=weather_data['main']['pressure'])
    else:
        print("Unable to fetch weather data.")

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercieses")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # OpenWeatherMap API Key (replace with your own key)
    api_key = 'd1d6485232d6a13b0a62b17a23a6ba5d'

    # Allow users to choose between Celsius and Fahrenheit
    units = 'metric'  # Default to Celsius
    weather_data = get_weather(api_key, city, units)
    display_weather(weather_data)

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

temp = 0  # Global variable to store temperature

# Search box
Search_image = PhotoImage(file="C:/Users/Admin/Desktop/shriya/weather/search.png")
myimage = Label(image=Search_image)
myimage.place(x=50, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="C:/Users/Admin/Desktop/shriya/weather/Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="C:/Users/Admin/Desktop/shriya/weather/Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="C:/Users/Admin/Desktop/shriya/weather/Copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
