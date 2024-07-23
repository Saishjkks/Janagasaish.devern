import tkinter as tk
import requests

def get_weather():
    user_input = city_entry.get()
    api_key = "9f42c92a5ece57f04ea9c51d8727b056"
    try:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
        data = weather_data.json()

        if data['cod'] == '404':
            error_label.config(text="No data found for the entered city.", fg="red")
            result_label.config(text="")
        else:
            weather = data['weather'][0]['main']
            temp = round(data['main']['temp'])

            result_label.config(text=f"The weather in {user_input} is: {weather}\nThe temperature in {user_input} is: {temp}ºF")
            error_label.config(text="", fg="black")
    except Exception as e:
        error_label.config(text=str(e), fg="red")
        result_label.config(text="")


root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#D9E6F2")  


city_label = tk.Label(root, text="Enter city:", font=("Helvetica", 12), bg="#D9E6F2", fg="black")
city_label.pack(pady=10)  

city_entry = tk.Entry(root, font=("Helvetica", 12), width=25, bg="white", fg="black", insertbackground="black")
city_entry.pack(pady=10) 

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather, bg="#4CAF50", fg="black", activebackground="#4CAF50", activeforeground="black")
get_weather_button.pack(pady=20)  


result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#D9E6F2", fg="black")
result_label.pack(pady=10)  


error_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#D9E6F2", fg="red")
error_label.pack(pady=10)


root.mainloop()
