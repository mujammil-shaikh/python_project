import requests
import tkinter as tk
from tkinter import messagebox

# OpenWeatherMap API key (replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'e6cda75e0bd3f5a735ea21d51ed6abc9'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    print(data)  # Add this line to check the API response

    if data['cod'] == '404':
        messagebox.showerror("Error", "City not found.")
    elif 'weather' in data:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        messagebox.showinfo("Weather Information",
                            f"City: {city}\nWeather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    else:
        messagebox.showerror("Error", "Weather information not available. Please try again later.")

def show_weather():
    city = city_entry.get()
    if city:
        get_weather(city)
        city_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a city.")

# GUI
root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter a city:")
label.pack()

city_entry = tk.Entry(frame)
city_entry.pack()

button = tk.Button(frame, text="Get Weather", command=show_weather)
button.pack()

root.mainloop()
