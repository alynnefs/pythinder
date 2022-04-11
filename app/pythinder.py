from kivymd.app import MDApp
from kivy.lang.builder import Builder

class Pomodoro(MDFloatLayout):
    timer_string = StringProperty('25:00')
