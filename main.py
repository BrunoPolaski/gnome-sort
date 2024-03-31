import webview
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    
    url = os.getenv('REMOTE_HOST')
    url = url if url else 'http://localhost:8000/views/index.html'
    
    webview.create_window('Gnome Sort', url, width=1920, height=1080)
    webview.start()

