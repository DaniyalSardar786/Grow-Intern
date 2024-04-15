from tkinter import *
import tkinter as tk
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from datetime import datetime
import pytz
import requests

window=Tk()
window.title("Weather App")
window.geometry("900x500+180+70")
window.resizable(False,False)

def get_weather():
    try:
        city=entry_field.get()
    
        geolocator = Nominatim(user_agent="main.py")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        localtime=datetime.now(home)
        current_time=localtime.strftime("%I:%M %p")
    
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        #fetching weather data from api
        api_key = '7b581cdc9ce7f694a73ff936a1f37fa6'
        url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        json_data=requests.get(url).json()
    
        condiition=json_data["weather"][0]["main"]
        feels_like=json_data['main']['feels_like']
        desc=json_data["weather"][0]["description"]
        tempr=json_data["main"]["temp"]
        press=json_data["main"]["pressure"]
        humidi=json_data["main"]["humidity"]
        wind_speed=json_data["wind"]["speed"]
    
        temp.config(text=str(tempr)+" °")
        clouds.config(text=f"{condiition} || Feels like {feels_like} °")
    
        wind.config(text=str(wind_speed)+"km\h")
        humidity.config(text=str(humidi)+"%")
        pressure.config(text=press)
        description.config(text=str(desc).capitalize())
    except:
        messagebox.showerror("Error","Invalid city name")

#search box
search_image=PhotoImage(file="search_image.png")
my_image=Label(image=search_image)
my_image.place(x=20,y=20)

entry_field=tk.Entry(window,width=17,font=("poppins",25,"bold"),bg="#404040",border=0,foreground="white")
entry_field.place(x=50,y=40)
entry_field.focus()

search_icon=PhotoImage(file="search_icon.png")
search_icon_label=Button(window,image=search_icon,bg="#404040",activebackground="#404040",border=0,cursor="hand2",command=get_weather)
search_icon_label.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="logo_image.png")
logo_image_label=Label(image=logo_image)
logo_image_label.place(x=170,y=100)

temp=Label(font=("arial",70,"bold"),fg="#ee666d")
temp.place(x=410,y=150)
clouds=Label(font=("arial",15,"bold"))
clouds.place(x=410,y=250)

#time
name=Label(font=("arial",15,"bold"))
name.place(x=45,y=100)
clock=Label(font=("Helvectia",20))
clock.place(x=45,y=130)

#bottom box
box_image=PhotoImage(file="box_image.png")
bottom_box_label=Label(image=box_image)
bottom_box_label.pack(side=BOTTOM,padx=5,pady=5)

#bottom box labels
label1=Label(window,text="WIND",font=("Helvectia",15,"bold"),bg="#1ab5ef",fg="white")
label1.place(x=120,y=400)

label2=Label(window,text="HUMIDITY",font=("Helvectia",15,"bold"),bg="#1ab5ef",fg="white")
label2.place(x=270,y=400)

label3=Label(window,text="DESCRIPTION",font=("Helvectia",15,"bold"),bg="#1ab5ef",fg="white")
label3.place(x=415,y=400)

label4=Label(window,text="PRESSURE",font=("Helvectia",15,"bold"),bg="#1ab5ef",fg="white")
label4.place(x=650,y=400)

wind=Label(window,text="....",font=("Helvectia",20,"bold"),bg="#1ab5ef",fg="black")
wind.place(x=120,y=430)

humidity=Label(window,text="....",font=("Helvectia",20,"bold"),bg="#1ab5ef",fg="black")
humidity.place(x=270,y=430)

description=Label(window,text="....",font=("Helvectia",20,"bold"),bg="#1ab5ef",fg="black")
description.place(x=415,y=430)

pressure=Label(window,text="....",font=("Helvectia",20,"bold"),bg="#1ab5ef",fg="black")
pressure.place(x=650,y=430)

window.mainloop()