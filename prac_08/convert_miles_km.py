"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesApp(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesApp().run()
