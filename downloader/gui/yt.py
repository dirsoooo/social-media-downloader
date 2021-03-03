from kivy.uix.screenmanager import Screen
from pytube import YouTube


class Yt(Screen):

    def download(self):
        try:
            url = self.ids.yt_url.text
            self.ids.error.text = 'Downloading...'
            ytd = YouTube(url).streams.first().download()
            self.ids.error.text = 'Download Sucessfull!'
            self.ids.yt_url.text = ''
        except Exception:
            self.ids.error.text = 'ERROR! Try again...'