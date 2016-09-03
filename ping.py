"""
This script pings every minute on myVIT api server on the route '/admin/stats'
and triggers notification when the server is not working
"""
import time
import requests
import gi
from gi.repository import GObject
gi.require_version('Notify', '0.7')
from gi.repository import Notify

"""
The notifier class
"""
class NotifyClass(GObject.Object):
    def __init__(self):
        super(NotifyClass, self).__init__()
        Notify.init("MyVIT-Ping")

    def send_notification(self,title,text,icon=""):
        n = Notify.Notification.new(title,text,icon)
        n.show()

def ping():
    notification = NotifyClass()
    while True:
        try:
            requests.get('http://localhost:8080/admin/stats')
        except Exception as e:
            notification.send_notification("MyVIT Server Message",str(type(e).__name__))
        time.sleep(60)

if __name__ == '__main__':
    ping()
