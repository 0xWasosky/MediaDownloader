__version__ = '1.0.0'
__author__ = '0xWasosky'
#IMPORT
import os

try: import requests
except ImportError:
    os.system('pip install requests')

try: import youtube_dl

except ImportError:
    os.system('pip install youtube_dl')

try: from pystyle import Colors

except ImportError:
    os.system('pip install pystyle')

#VAR
TITLE = f'{__author__} --> {__version__}'

Text_banner = f'''
███    ███ ███████ ██████  ██  █████  
████  ████ ██      ██   ██ ██ ██   ██ 
██ ████ ██ █████   ██   ██ ██ ███████ 
██  ██  ██ ██      ██   ██ ██ ██   ██ 
██      ██ ███████ ██████  ██ ██   ██

[1] > Download image
[2] > Download Youtube video

VERSION: {__version__}
'''

PURPLE = Colors.purple 
WHITE = Colors.white


#DEF
os.system(f'title {TITLE}')

def banner():
    print(PURPLE + Text_banner + WHITE)


#CLASSES
class RequestError(Exception): pass
class InvalidInput(Exception): pass

class Download:
    def __init__(self):
        
        self.command = input('$: ')

        if (self.command in ['1','img']):
            img_link = input('Img link: ')
            
            try:
                response = requests.get(img_link)
                if (response.status_code >= 200 <= 299):
                    img_file = open('Media.jpg','wb')
                    img_file.write(response.content)
                    img_file.close()
            except:
                raise RequestError("""
                Unfortunately there were some problems with sending the request. One of them could be that the link to the image is not allowed.
                Allowed link example: https://eximg.netlify.app/img.png

                "https://eximg.netlify.app"
                """)
        elif (self.command in ['2','youtube']):
            youtube_link = input('Video link: ')
            with youtube_dl.YoutubeDL() as video:
                video.download([youtube_link])

        else: raise InvalidInput('typeError: Invalid input retry.')

if __name__ == '__main__':
    banner()    
    Download()