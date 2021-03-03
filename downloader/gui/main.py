from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from yt import Yt
from fb import Fb
from insta import InstaConfirm, Insta_Image, Insta_Video
from kivy.config import Config


class Manager(ScreenManager):
    pass


class Menu(Screen):
    pass


class MainApp(App):
    title = 'Downloader'

    def build(self):  # Start
        return Manager()


if __name__ == "__main__":
    Config.set('kivy', 'window_icon', './logo/logo-p.png')
    MainApp().run()
