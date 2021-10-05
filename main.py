import time
import cProfile
from kivy.app import App
from kivy.lang import builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.config import Config

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '100')

builder.Builder.load_file("style.kv")

the_time = ''
the_day = ''


class AppLayout(FloatLayout):
    display_time = StringProperty("Time")
    display_day = StringProperty("Date")

    def __init__(self):
        super().__init__()
        self.currentHour = []
        self.update()

    def update(self, *args):
        current_time = list(time.asctime())
        self.display_time = str(str(current_time[11]) + str(current_time[12]) + " : " + str(current_time[14]) +
                                str(current_time[15]))
        self.display_day = str(str(current_time[0]) + str(current_time[1]) + str(current_time[2]) + " " +
                               str(current_time[4]) + str(current_time[5] + str(current_time[6]) + " " +
                                                          str(current_time[8]) + str(current_time[9]) + " " +
                                                          str(current_time[20]) + str(current_time[21]) +
                                                          str(current_time[22]) + str(current_time[23])))


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.profile = cProfile.Profile()

    def on_start(self):
        self.profile.enable()

    def on_stop(self):
        self.profile.disable()
        self.profile.dump_stats('MyApp.profile')

    def build(self):
        self.title = 'Savvi Clock'
        self.icon = 'logo.ico'
        crude_clock = AppLayout()
        Clock.schedule_interval(crude_clock.update, 1)
        return crude_clock


if __name__ == '__main__':
    MyApp().run()
