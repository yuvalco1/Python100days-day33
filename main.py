from time import sleep

import requests
import datetime as dt
from datetime import timezone

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    print(response.status_code)
    print(response.text)
    data = response.json()
    print(data["iss_position"]["latitude"])
    print(data["iss_position"]["longitude"])
    return data["iss_position"]["latitude"], data["iss_position"]["longitude"]


my_lat = 31.980066
my_lng = 34.770934
parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0
}
### my position close to ISS Position #############
def iss_is_close():
    iss_lat, iss_lng = get_iss_position()
    if (abs(iss_lat - my_lat) < 0.05) and (abs(iss_lng - my_lng) < 0.05):
        return True
    else:
        return False



############# Sunrise and Sunset #############
def check_it():

    sun = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    sun.raise_for_status()
    sun_data = sun.json()
    sunset = sun_data["results"]["sunset"]
    sunrise = sun_data["results"]["sunrise"]
    sunset_time = sunset.split("T")[1].split(":")
    sunrise_time = sunrise.split("T")[1].split(":")
    time_now = str(dt.datetime.now(timezone.utc)).split(" ")[1].split(":")
    print("sunset_time", sunset_time[0]+":"+sunset_time[1] )
    print("sunrise_time", sunrise_time[0]+":"+sunrise_time[1] )
    print("time_now", time_now[0]+":"+time_now[1] )
    sunset_time_int = int(sunset_time[0])*60 + int(sunset_time[1])
    sunrise_time_int = int(sunrise_time[0])*60 + int(sunrise_time[1])
    time_now_int = int(time_now[0])*60 + int(time_now[1])

    # if it is after sunset and before sunrise (night time) and iss is close to me:
    if time_now_int >= sunset_time_int and time_now_int <= sunrise_time_int:
        if iss_is_close():
            print("It is night time and ISS is close to you, Go look for it in the sky")
        else:
            print(f"{dt.datetime.now()} bassa")
    else:
        print(f"{dt.datetime.now()} bassa")

while True:
    check_it()
    sleep(10)

################### Kanya Quote ###################
from tkinter import Tk, Canvas, PhotoImage, Button

#
# def get_quote():
#     qresponse = requests.get(url="http://api.kanye.rest")  #  response.raise_for_status()
#     qresponse.raise_for_status()
#     dataq = qresponse.json()
#     quote = dataq["quote"]
#     canvas.itemconfig(quote_text, text=quote)
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# get_quote()
#
# window.mainloop()