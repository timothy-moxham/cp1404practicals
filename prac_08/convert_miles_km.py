"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        result = self.get_valid_number() * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        result = self.get_valid_number() + change
        self.root.ids.input_number.text = str(result)
        self.handle_convert(result)

    def get_valid_number(self):
        try:
            return float(self.root.ids.input_number.text)
        except ValueError:
            return 0


ConvertMilesApp().run()
