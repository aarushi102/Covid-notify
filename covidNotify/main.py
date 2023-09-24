from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\MyData\Business\code playground\covidNotify\icon.ico",
        timeout = 6
    )


def getData(url):
    r = requests.get(url)
    return r.text

