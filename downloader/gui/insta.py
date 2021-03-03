from kivy.uix.screenmanager import Screen
import os
import sys
import re
import requests
import urllib.request
import os
import subprocess as s


class InstaConfirm(Screen): 
    pass


class Insta_Image(Screen):

    def open_browser(self, url):
        opsys = sys.platform
        if 'win' in opsys:
            try:
                os.startfile(url)
            except:
                self.ids.label.text = 'Error.'
        if 'linux' in opsys:
            try:
                s.Popen(url)
            except FileNotFoundError:
                try:
                    s.Popen(['xdg-open', url])
                except:
                    self.ids.label.text = 'Error.'

    def prepare_urls(self, lines):
        return list({line.replace("\\u0026", "&") for line in lines})

    def get_response(self, url):
        r = requests.get(url)
        if r.status_code != 200:
            r = requests.get(url)
            if r.status_code != 200:
                r = requests.get(url)
                if r.status_code != 200:
                    r = requests.get(url)
                    if r.status_code != 200:
                        r = requests.get(url)
                        if r.status_code != 200:
                            r = requests.get(url)
                            if r.status_code != 200:
                                r = requests.get(url)
                                if r.status_code != 200:
                                    self.ids.label.text = 'Error.'
                                    # while doesn't work on kivy : (
        return r.text

    def download(self):
        img_url = self.ids.img_url.text
        html = self.get_response(img_url)
        try:
            img_matches = re.findall('"display_url":"([^"]+)"', html)
            img_url = self.prepare_urls(img_matches)
        except Exception:
            self.ids.error.text = ''
        self.ids.label.text = f'Detected Pictures: {len(img_url)}'
        if len(img_url) == 0:
            if 429 in html:
                self.ids.label.text = 'Too many requests!'
                self.ids.img_url.text = ''
            else:
                self.ids.label.text = '0 pictures detected...'
                self.ids.img_url.text = ''
        else:
            self.ids.label.text = 'Openning your browser'
            self.ids.img_url.text = ''
            if len(img_url) == 1:
                self.open_browser(img_url[0])
            else:
                for photo in range(0, len(img_url)):
                    self.open_browser(img_url[photo])


class Insta_Video(Screen):

    def get_response(self, url):
        r = requests.get(url)
        print(r)
        if r.status_code != 200:
            r = requests.get(url)
            if r.status_code != 200:
                r = requests.get(url)
                if r.status_code != 200:
                    r = requests.get(url)
                    if r.status_code != 200:
                        r = requests.get(url)
                        if r.status_code != 200:
                            r = requests.get(url)
                            if r.status_code != 200:
                                r = requests.get(url)
                                if r.status_code != 200:
                                    r = requests.get(url)
                                    if r.status_code != 200:
                                        r = requests.get(url)
                                        if r.status_code != 200:
                                            r = requests.get(url)
                                            if r.status_code != 200:
                                                r = requests.get(url)
                                                if r.status_code != 200:
                                                    r = requests.get(url)
                                                    if r.status_code != 200:
                                                        r = requests.get(url)
                                                        if r.status_code != 200:
                                                            self.ids.label.text = 'Error.'
                                    # while doesn't work on kivy : (
        return r.text

    def prepare_urls(self, lines):
        return list({line.replace("\\u0026", "&") for line in lines})

    def open_browser(self, url):
        opsys = sys.platform
        if 'win' in opsys:
            try:
                os.startfile(url)
            except:
                self.ids.label.text = 'Error.'
        if 'linux' in opsys:
            try:
                s.Popen(url)
            except FileNotFoundError:
                try:
                    s.Popen(['xdg-open', url])
                except:
                    self.ids.label.text = 'Error.'

    def download_video(self):
        video_url = self.ids.video_url.text
        html = self.get_response(video_url)
        try:
            vi_matches = re.findall('"video_url":"([^"]+)"', html)
            videos_url = self.prepare_urls(vi_matches)
            print(videos_url)
        except:
            self.ids.label.text = 'Error.'   
        if video_url:
            if len(videos_url) == 0:
                self.ids.label.text = '0 videos detected...'
                self.ids.video_url.text = ''
            else:
                self.ids.label.text = 'Openning your browser'
                if len(videos_url) == 1:
                    self.open_browser(video_url[0])
                else:
                    for video in range(0, len(video_url)):
                        self.open_browser(video_url[video])
