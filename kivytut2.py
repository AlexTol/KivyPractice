import kivy

from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):

    def build(self):
        #we reference text from another file
        #note if your class is 'HelloKivy or HelloKivyApp, the .kv file should be named hellokivy.kv
        return Label()

helloKivy = HelloKivy()

helloKivy.run()