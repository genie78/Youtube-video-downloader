import subprocess
import platform
from time import sleep
try :
    from pytube import YouTube
    from pytube.exceptions import RegexMatchError
except ModuleNotFoundError:
    print("[!] Could not find pytube lib.")
    sleep(3)
    print("[*] Installing pytube lib...")
    sleep(3)
    subprocess.call("pip install pytube",shell=True)
    print("[*] Done.")
    sleep(3)
    from pytube import YouTube
    from pytube.exceptions import RegexMatchError

logo = '''
       __     __         _         _                       
       \ \   / /        | |       | |                      
        \ \_/ /__  _   _| |_ _   _| |__   ___              
         \   / _ \| | | | __| | | | '_ \ / _ \             
          | | (_) | |_| | |_| |_| | |_) |  __/             
  _____   |_|\___/ \__,_|\__|\__,_|_.__/ \___| _           
 |  __ \                    | |               | |          
 | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                         
'''
my_sys = platform.system()

if my_sys == "Windows":
    subprocess.call("cls",shell=True)
elif my_sys == "Linux":
    subprocess.call("clear", shell=True)
print(logo)
def downloadVideo():
    
    try:
        my_url = input("[+] Please paste in the URL of the video you want to download: ")
        yt = YouTube(url=my_url)
        video = yt.streams.filter(res="360p").first()
        while True:
            location = input("[+] Please specify the directory you want to save the video to: ")
            if type(location) == str:
                video.download(location)
                print("[*] Video downloaded successfuly.")
                break
            else:
                print("[-] Please enter a vaid location.")
        
    except RegexMatchError :
        print("\n[-] Please enter correct link.")
        downloadVideo()

    except KeyboardInterrupt :
        print("\n[-] Exiting from Yotube downloader tool.")
  
downloadVideo()
