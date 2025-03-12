import tkinter as tk
import requests
import time

def getWeather():
    city = textField.get()
    api_key = "5ab208f490f20f946471b2292e2ecd00"  # Replace with your OpenWeatherMap API key
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    json_data = requests.get(api).json()

    if json_data["cod"] != "404":
        main_info = json_data["weather"][0]["main"]
        temp = int(json_data["main"]["temp"] - 273.15)
        min_temp = int(json_data["main"]["temp_min"] - 273.15)
        max_temp = int(json_data["main"]["temp_max"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind_speed = json_data["wind"]["speed"]
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data["sys"]["sunrise"] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data["sys"]["sunset"] - 21600))

        final_info = f"{main_info}\n{temp}°C"
        final_data = (f"\nMin Temp: {min_temp}°C\n"
                      f"Max Temp: {max_temp}°C\n"
                      f"Pressure: {pressure}\n"
                      f"Humidity: {humidity}\n"
                      f"Wind Speed: {wind_speed}\n"
                      f"Sunrise: {sunrise}\n"
                      f"Sunset: {sunset}")

        label1.config(text=final_info, foreground="white", bg="#8C001A")
        label2.config(text=final_data, foreground="white", bg="#8C001A")
    else:
        label1.config(text="City not found", foreground="white", bg="#8C001A")
        label2.config(text="", foreground="white", bg="#8C001A")

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.configure(bg='#8C001A')
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

label3 = tk.Label(canvas, borderwidth=4, font=f)
label3.pack()
switch = "\n" + "Enter your city:" + "\n"
label3.config(text=switch, foreground="white", bg="#8C001A")

textField = tk.Entry(canvas, justify='center', width=20, font=t, foreground="white")
textField.configure(bg="#C04000", insertbackground='black')
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', lambda event=None: getWeather())

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
