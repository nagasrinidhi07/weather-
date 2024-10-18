from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_key = 'weather.key'
file_a = ConfigParser()
file_a.read(api_key)
api_key = file_a['api_key']['key']

def weather_find(city):
 final = requests.get(url_api.format(city,api_key))
 if final:
      json_file = final.json()
      city = json_file['name']
      country_name = json_file['sys']['country']
      k_temp = json_file['main']['temp']
      c_temp = k_temp - 273.15
      f_temp = (k_temp - 273.15)*9/5+32
      weather_display = json_file['weather'][0]['main']
      result = (city,country_name,c_temp,f_temp,weather_display)
      
      return result
 else:
         return None       
def print_weather():
    city = search_city.get() 
    weather = weather_find(city)       
    if weather:
     location_entry['text'] = "{}, {}".format(weather[0], weather[1])
     temp_entry['text'] = '{:.2f} c,{:.2f} f'.format(weather[2], weather[3]) 
     weather_entry['text'] = weather[4]
 

    else:
     messagebox.showerror('Error', 'please enter a valid city name Cannot find city')
     
root = Tk()
root.title("Weather App")
root.config(bg="lightblue")
root.geometry("800x400")

search_city = StringVar()
enter_city = Entry(root, textvariable=search_city,fg="black", font=("arial","35","bold"))
enter_city.pack()


search_btn = Button(root, text="Search Weather",width=20, bg="red",fg="white", font=("arial", 30, "bold"),command = print_weather)
search_btn.pack()

location_entry = Label(root, text="",fg="black", font=("arial",40, "bold"),bg="lightblue")
location_entry.pack()


temp_entry = Label(root, text='',fg="black", font=("arial",40, "bold"),bg="lightblue")
temp_entry.pack()

weather_entry = Label(root, text='',fg="black", font=("arial",40, "bold"),bg="lightblue")
weather_entry.pack()

root.mainloop()