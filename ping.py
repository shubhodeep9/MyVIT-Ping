"""
This script pings every minute on myVIT api server on the route '/admin/stats'
and triggers notification when the server is not working
"""
#!/usr/bin/python
import time
import requests
from gi.repository import GObject
from gi.repository import Notify, GdkPixbuf

"""
The notifier class
"""
class NotifyClass(GObject.Object):
    def __init__(self):
        super(NotifyClass, self).__init__()
        Notify.init("MyVIT-Ping")

    def send_notification(self,title,text,icon=""):
        n = Notify.Notification.new(title,text)
        if icon != "":
            # Use GdkPixbuf to create the proper image type
            image = GdkPixbuf.Pixbuf.new_from_file(icon)
            # Use the GdkPixbuf image
            n.set_icon_from_pixbuf(image)
            n.set_image_from_pixbuf(image)
        n.show()

def ping():
    notification = NotifyClass()
    while True:
        r = requests.get('http://myffcs.in:8080/admin/stats')
        status = r.status_code
        if status == 200:
            data = r.json()
            notification.send_notification("MyVIT Running","Current users : "+str(data['current_users']),"myvit.jpg")
        else:
            notification.send_notification("MyVIT Server Message","Server is down [503]","myvit.jpg")
        time.sleep(60)

if __name__ == '__main__':
    ping()
