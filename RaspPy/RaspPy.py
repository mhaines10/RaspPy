
import requests
import re
from bs4 import BeautifulSoup
import lxml
import cv2
import time
from io import BytesIO
from PIL import Image


def acquireImg():
    while True:
        page = requests.get('http://45.76.30.200:5000')
        soup = BeautifulSoup(page.content,'lxml')
        imgPath = soup.find('img')['src']
        fullPath = '{}{}'.format('http://45.76.30.200:5000',imgPath)
        filename = r'C:\Users\matth\Pictures\currImg'
        resp = requests.get(fullPath)
        img = Image.open(BytesIO(resp.content))
        img.show() 
        time.sleep(20)  

acquireImg()