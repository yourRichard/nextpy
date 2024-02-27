"""Welcome to Nextpy! This file outlines the steps to create a basic app."""

import nextpy as xt
import asyncio
import requests
from datetime import datetime
import time

API_KEY: str = open('API_KEY.txt','r').read()


style: dict = {
        "font_family":"Arial, Helvetica, sans-serif"
    }

class State(xt.State):
    """The app state."""
    city = ""
    country = ""
    location=""
    temp=""
    speed=""
    humidity=""
    img_src="/bg-main.avif"
    current_time = ""
    
    local_time = ""
    
    user_input = ""
    
    
    def get_input_value(self,user_input):
        self.user_input = user_input
        
    async def route_after_key_press(self):
        if self.user_input != "":
            await self.get_data_from_weather()

    async def constant_city(self,const_city):
        response = requests.get(get_weather(const_city))
        await asyncio.sleep(0.5)
        
        
        if response.status_code == 200:
            data = response.json()

            self.city = const_city
            self.country = data["sys"]["country"]
            self.temp = f"{int(data['main']['temp'])}°C"
            self.humidity = f"{int(data['main']['humidity'])}%"
            self.speed = f"{int(data['wind']['speed'])}km/hr"
            self.location = f"{self.city.capitalize()}"
            
    async def get_data_from_weather(self):
        __city__ = self.user_input
        response = requests.get(get_weather(__city__))
        await asyncio.sleep(0.5)
        
        time_object = time.localtime()
        local_time = time.strftime("%B %d %Y",time_object)
        self.local_time = local_time

        time_here = datetime.today().strftime("%H:%M- %p")
        self.current_time = time_here

        if response.status_code == 200:
            data = response.json()

            self.city = __city__
            self.country = str(data["sys"]["country"])
            self.temp = f"{int(data['main']['temp'])}°C"
            self.humidity = f"{int(data['main']['humidity'])}%"
            self.speed = f"{int(data['wind']['speed'])}km/hr"
            self.location = f"{self.city.capitalize()}"
            
            
            if str(data["sys"]["country"]) == "MM":
                self.img_src = "/mandalay.jpg"
            if str(data["sys"]["country"]) == "FR":
                self.img_src = "/paris.webp"
            if str(data["sys"]["country"]) == "PT":
                self.img_src = "/portugal.jpg"
            if str(data["sys"]["country"]) == "KR":
                self.img_src = "/korea.webp"
            if str(data["sys"]["country"]) == "IT":
                self.img_src = "/italy.jpg"
            if str(data["sys"]["country"]) == "IN":
                self.img_src = "/india.avif"
            if str(data["sys"]["country"]) == "TH":
                self.img_src = "/thailand.jpg"
            if str(data["sys"]["country"]) == "AR":
                self.img_src = "/argentina.avif"
            if str(data["sys"]["country"]) == "GB":
                self.img_src = "/england.jpg"
            if str(data["sys"]["country"]) == "DE":
                self.img_src = "/germany.avif"
                

   
            
    
def get_weather(city):
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}&units=metric"
    return BASE_URL


def index() -> xt.Component:
    return xt.container(
      xt.box(
        xt.box(
             xt.box(
             xt.text(
                 "weather.nextpy",
                 color="white",
                 font_weight="bold",
                 font_size="12px",
                 margin_left = "28px",
                 letter_spacing="2px"
             ),
             xt.image(
                 src=State.img_src,
                 width="340px",
                 height="220px",
                 position="absolute",
                 top="150px",
                 border="3px solid rgba(2,0,36,1)",   
                 margin_left="20px",
                 box_shadow="0px 4px 6px black",
             ),
             xt.container(
                 xt.text(
                     State.temp,
                     font_size="60px",
                     font_weight="bold",
                     color="white",
                     line_heigh='40px'
                 ),
                 xt.vstack(
                     xt.text(
                         State.location,
                         font_size="35px",
                         font_weight="bold",
                         margin_top="30px",
                         left="0px",
                         color="white",
                         line_height="14px"
                     ),
                     xt.text(
                         State.local_time,
                         color="white",
                                            
                     ),
                     width='120px',
                    margin_left="50px",
                 ),
                 xt.box(
                   xt.vstack(
                     xt.text(
                         State.country,
                         font_size="35px",
                         font_weight="bold",
                         margin_top="35px",
                         line_height="10px",
                         color="white"
                     ),
                     xt.text(
                         State.current_time,
                         color="white",
                     ),
                     margin_left = "35px",
                     width='120px',
                 ),
                 ),
                 display="flex",
                 justify_content="space-between",
                 width="100%",
                 margin_top="20rem",
             ),
          ),
          xt.box(
            xt.box(
             xt.input(
             value=State.user_input,
             on_change=State.get_input_value,
             color="#8fa5b3",
             placeholder="Enter location",
             border="1px solid #98e7ed"
          ), 
          xt.box(
              xt.icon(tag="search",color="black",margin_left="14px",margin_top="12px"),
              bg="white",
              height="40px",
              width="70px",
              margin_left="6px",
              cursor="pointer",
              border_radius="5px",
              on_click=lambda:State.route_after_key_press,
            ),
            display="flex",
            width="200px",
            mx="auto"
            ),
            xt.box(
                xt.box(
                    xt.text("Mandalay, MM"),
                    margin_top="30px",
                    color="#8fa5b3",
                    letter_spacing="2px",
                    cursor="pointer",
                    on_click=lambda:State.constant_city("Mandalay")
                ), 
                xt.box(
                    xt.text("Paris, FR"),
                    margin_top="30px",
                    color="#8fa5b3",
                    cursor="pointer",
                    letter_spacing="2px",
                    on_click=lambda:State.constant_city("Paris")
                ), 
                xt.box(
                    xt.text("Bangalore, IN"),
                    margin_top="30px",
                    color="#8fa5b3",
                    cursor="pointer",
                    letter_spacing="2px",
                    on_click=lambda:State.constant_city("Bangalore")
                ), 
                xt.box(
                    xt.text("London, UK"),
                    margin_top="30px",
                    color="#8fa5b3",
                    cursor="pointer",
                    letter_spacing="2px",
                    on_click=lambda:State.constant_city("London")
                ),
                margin_top="12px",
                border_bottom="1px solid #98e7ed",
                padding_bottom="25px"
            ),
            xt.box(
                xt.box(
                    xt.text("Weather details"),
                    margin_top="30px",
                    color="#ffffff",
                    letter_spacing="1px"
                ),
                xt.box(
                    xt.text("Humidity",color="#8fa5b3",letter_spacing="1px"),
                    xt.text(State.humidity,color="white",font_weight="bold"),
                    margin_top="30px",
                    display="flex",
                    justify_content="space-between"
                ),
             
                xt.box(
                    xt.text("Speed",color="#8fa5b3",letter_spacing="1px"),
                    xt.text(State.speed,color="white",font_weight="bold"),
                    margin_top="30px",
                    display="flex",
                    justify_content="space-between"
                ),
             
            ),
          ),
            margin_right="20px",
            display="flex",
            justify_content="space-between"
        ),
        bg= "linear-gradient(to right,rgba(163, 196, 237, 0.43) 0%,rgba(163, 196, 237, 0.43) 64%,#406a8a 64%,#406a8a 100%)",
        width="60%",
        height="550px",
        my="auto",
        mx="auto",
        border_radius = "15px",
        padding_top="50px",
        border="5px solid white",
        box_shadow = "0px 4px 6px black"
      ),
    bg="linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%)",
    height="100vh",
    max_width = "auto",
    padding_top="30px",
    )


# Add state and page to the app.
app = xt.App(style=style)
app.add_page(index)
app.compile()
