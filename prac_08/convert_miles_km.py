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

    def handle_convert(self, value):
        result = float(value) * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        result = float(self.root.ids.input_number.text) + change
        self.root.ids.input_number.text = str(result)
        self.handle_convert(result)


ConvertMilesApp().run()
