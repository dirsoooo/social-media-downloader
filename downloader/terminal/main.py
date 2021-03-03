try:
    import os
    import sys
    import re
    import requests
    import urllib.request
    import os
    import subprocess as s
    from time import sleep
    from pytube import YouTube
except Exception as error:
    print(f'[-] Modules missing! {error}')
    sleep(2)
    sys.exit(1)


def printASCII():
    print("""                       
   ___                  __             __      
  / _ \___ _    _____  / /__  ___ ____/ /__ ____
 / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/
/____/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/     
   __  ___         __         
  /  |/  /__ ____ / /____ ____
 / /|_/ / _ `(_-</ __/ -_) __/
/_/  /_/\_,_/___/\__/\__/_/   
                                                                             
                        By Dirso
    """)


def printASCIIFace():
    print("""
   ___              _                 _                  
  / __\_ _  ___ ___| |__   ___   ___ | | __              
 / _\/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /              
/ / | (_| | (_|  __/ |_) | (_) | (_) |   <               
\/   \__,_|\___\___|_.__/ \___/ \___/|_|\_\              
                                                         
    ___                    _                 _           
   /   \_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  / /\ / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 / /_// (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
/___,' \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                         
                                                
    """)


def printASCIIInsta():
    print("""     
 _             _                                  
| |._ _  ___ _| |_ ___  ___  _ _  ___ ._ _ _      
| || ' |<_-<  | | <_> |/ . || '_><_> || ' ' |     
|_||_|_|/__/  |_| <___|\_. ||_|  <___||_|_|_|     
                       <___'                      
 ___                   _              _           
| . \ ___  _ _ _ ._ _ | | ___  ___  _| | ___  _ _ 
| | |/ . \| | | || ' || |/ . \<_> |/ . |/ ._>| '_>
|___/\___/|__/_/ |_|_||_|\___/<___|\___|\___.|_|  
                                                  
                                                
    """)


def printASCIIYT():
    print("""
  _                  ______     _                            
 (_|   |            (_) |      | |                           
   |   |  __            |      | |   _                       
   |   | /  \_|   |   _ ||   | |/ \_|/                       
    \_/|/\__/  \_/|_/(_/  \_/|_/\_/ |__/                     
      /|                                                     
   ___\|                       _                             
  (|   \                      | |               |            
   |    | __           _  _   | |  __   __,   __|   _   ,_   
  _|    |/  \_|  |  |_/ |/ |  |/  /  \_/  |  /  |  |/  /  |  
 (/\___/ \__/  \/ \/    |  |_/|__/\__/ \_/|_/\_/|_/|__/   |_/
                                                             
                                                             
    """)


def readInt(text):
    while True:
        try:
            word = int(input(text))
        except:
            print("[-] Please type numbers only!\n")
            sleep(1)
            continue
        else:
            if word > 3 or word < 1:
                print("[-] Please type only 1, 2 or 3!\n")
            else:
                return word


def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text


def photo_video():
    while True:
        try:
            word = int(input('1 for PHOTO, 2 for VIDEO\n> '))
        except:
            print("[-] Please type numbers only!\n")
            sleep(1)
            continue
        else:
            if word > 2 or word < 1:
                print("[-] Please type only 1 or 2!\n")
            else:
                return word


def prepare_urls(lines):
    return list({line.replace("\\u0026", "&") for line in lines})


def download_video(video_url, name):
    try:
        url = re.search('hd_src:"(.+?)"', video_url)[1]
        sleep(1)
        print('HD Video! (720p)')
    except:
        try:
            url = re.search('sd_src:"(.+?)"', video_url)[1]
            print(url)
            sleep(1)
            print('Low Quality Video :( (480p)')
        except:
            print('ERROR :(', 'red')
            sleep(2)
            sys.exit(2)
    print('Downloading your video...')
    try:
        urllib.request.urlretrieve(url, f'{name}.mp4')
        print('[+] Download Sucessfull!')
    except:
        print('[-] Download Error :(')
        sleep(2)
        sys.exit(1)

def open_browser(url):
    opsys = sys.platform
    if 'win' in opsys:
        try:
            os.startfile(url)
        except:
            return 'Error.'
    if 'linux' in opsys:
        try:
            s.Popen(url)
        except FileNotFoundError:
            try:
                s.Popen(['xdg-open', url])
            except:
                return 'Error'


def main():
    printASCII()
    print("""What do you want to do?
    
                1) Facebook
                2) Instagram
                3) Youtube""")
    option = readInt('> ')
    if option == 1:
        printASCIIFace()
        print('Type video URL ')
        link = str(input('> '))
        html = get_response(link)
        name = str(input('Type a name for your video: '))
        download_video(html, name)
    if option == 2:
        printASCIIInsta()
        vp = photo_video()
        if vp == 1:
            print('Type photo URL: ')
            link = str(input('> '))
            html = get_response(link)
            try:
                img_matches = re.findall('"display_url":"([^"]+)"', html)
                img_url = prepare_urls(img_matches)
            except:
                print('[-] Error!')
                sleep(2)
                sys.exit(1)
            print("\n[+] Detected Pictures: \n{0}".format('\n'.join(img_url)))
            sleep(1)
            if len(img_url) == 0:
                print(0)
                print("[-] Error")
                sleep(2)
                sys.exit(1)
            else:
                print('\n[+] Openning your borowser...')
                if len(img_url) == 1:
                    open_browser(img_url[0])
                else:
                    for photo in range(0, len(img_url)):
                        open_browser(img_url[photo])
        if vp == 2:
            print('Type video URL ')
            link = str(input('> '))
            html = get_response(link)
            try:
                vi_matches = re.findall('"video_url":"([^"]+)"', html)
                video_url = prepare_urls(vi_matches)
            except:
                print("[-] Error!")    
            if video_url:
                print("[+] Detected Videos: \n{0}".format('\n'.join(video_url)))
                if len(video_url) == 0:
                    print(0)
                    print("[-] Error")
                    sleep(2)
                    sys.exit(1)
                else:
                    print('\n[+] Openning your borowser...')
                    if len(video_url) == 1:
                        open_browser(video_url[0])
                    else:
                        for video in range(0, len(video_url)):
                            open_browser(video_url[video])
    if option == 3:
        printASCIIYT()
        print('Type video URL ')
        link = str(input('> '))
        sleep(1)
        try:
            print('[+] Downloading your video...')
            ytd = YouTube(link).streams.first().download()
            print('[+] Download Sucessfull!')
        except Exception:
            print('[-] Error')
            sleep(2)
            sys.exit(1)
if __name__ == "__main__":
    main()
