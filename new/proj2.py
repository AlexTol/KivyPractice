import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button

class FirstKivy(App):
    def build(self):
        return Button(text = "Welcome to Toon Toon")

FirstKivy().run()