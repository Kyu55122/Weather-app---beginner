import sys
import requests
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                                 QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class Weather(QWidget): # class means blueprint (In this case, the weather app interface)
    def __init__(self): # the setup - automatically runs when the object is created
        super().__init__()
        self.setWindowTitle("WeatherApp") # used to represent the object created from the class
        self.initUI()
      #  THE CODE OF LINE UNDER THIS WAS FOR TESTING PURPOSES
      #  self.text = QLineEdit(self   
      #  self.text.move(100, 70)
      #  self.text.resize(300, 300)
      #  self.text.setFont(QFont("Times New Roman", 15))
      #  self.text.setAlignment(Qt.AlignCenter)

      #  self.text.setStyleSheet("""
      #      background-color: rgb(33, 25, 105);
        #     color: rgb(254, 254, 254);
       # """)
    def initUI(self):
        self.resize(400, 400)
        self.setStyleSheet("""
        background-color: rgb(40, 90, 136);
        """)
        self.city_input = QLineEdit(self)
        self.city_input.move(100,80)
        self.city_input.resize(200,30)
        self.city_input.setFont(QFont("Times New Roman", 20))
        self.city_input.setStyleSheet("""
        background-color: rgb(255, 255, 255);
        """)

        self.search_push = QPushButton(self)
        self.search_push.setText("Search")
        self.search_push.move(160,120)
        self.search_push.setStyleSheet("""
        background-color: rgb(255, 255, 255);
        """)
        self.search_push.clicked.connect(self.search)



        self.temp_show = QLabel(self)
        self.temp_show.setText("Temperature")
        self.temp_show.move(2, 190)
        self.temp_show.setFont(QFont("Times New Roman",15))

        self.temp_ans = QLabel(self)
        self.temp_ans.setText("Waiting...")
        self.temp_ans.resize(350, 50)
        self.temp_ans.setFont(QFont("Times New Roman",15))
        self.temp_ans.move(2, 220)
        self.temp_ans.setStyleSheet("""
        color: rgb(211, 211, 211);
        """)

        self.city_name = QLabel(self)
        self.city_name.setText("Enter City")
        self.city_name.setFont(QFont("Times New Roman", 20))
        self.city_name.move(140, 30)

        self.description_show = QLabel(self)
        self.description_show.setText("Description")
        self.description_show.resize(600, 22)
        self.description_show.setFont(QFont("Times New Roman",15))
        self.description_show.move(5, 285)

        self.description_ans = QLabel(self)
        self.description_ans.setText("Waiting...")
        self.description_ans.resize(350, 40)
        self.description_ans.setFont(QFont("Times New Roman",15))
        self.description_ans.move(5, 320)
        self.description_ans.setStyleSheet("""
        color: rgb(211, 211, 211);
        """)


    def search(self):
        city = self.city_input.text() # stored input
        API_KEY = "#PUT API KEY HERE"

        if city == "":
            self.description_ans.setText("Waiting...")
            self.temp_ans.setText("Waiting...")

        else:
            url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"


            response = requests.get(url)
            print(response.status_code)

            if response.status_code == 404:
                self.description_ans.setText("Waiting...")
                self.temp_ans.setText("Waiting...")


            else:
                data = response.json()

                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]

                celsuis = temperature - 273.15
                fahrenheit = (celsuis * 9/5) + 32
                fahrenheit = int(round(fahrenheit))

                self.temp_ans.setText(f"{fahrenheit}°F")
                self.description_ans.setText(f"{description.capitalize()}\nHumidity {humidity}%")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = Weather() # This is the object
    weather_app.show()
    sys.exit(app.exec_())
