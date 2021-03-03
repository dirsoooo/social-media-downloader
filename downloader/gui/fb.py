from kivy.uix.screenmanager import Screen
import os
import re
import requests
import urllib.request
import os
import subprocess as s


class Fb(Screen):
    def download_video(self, video_url, name):
        try:
            url = re.search('hd_src:"(.+?)"', video_url)[1]
            self.ids.error.text = 'HD Video'
        except:
            try:
                url = re.search('sd_src:"(.+?)"', video_url)[1]
                self.ids.error.text = '480p Video'
            except:
                self.ids.error.text = 'Error'
        self.ids.error.text = 'Downloading your video...'
        try:
            urllib.request.urlretrieve(url, f'{name}.mp4')
            self.ids.error.text = 'Download Sucessfull!'
            self.ids.fb_url.text = ''
            self.ids.name_video.text = ''
        except:
            self.ids.error.text = 'Download Error'

    def get_response(self, url):
        r = requests.get(url)
        while r.status_code != 200:
            r = requests.get(url)
        return r.text

    def download(self):
        url = self.ids.fb_url.text
        name = self.ids.name_video.text
        try:
            html = self.get_response(url)
            self.download_video(html, name)
        except:
            self.ids.error.text = 'Fields empty!'
