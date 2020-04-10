import requests
import threading
import logging
import time

def uptime_check():
    requests_log = logging.getLogger('urllib3')
    requests_log.setLevel(logging.ERROR)   
    fh = logging.FileHandler("requests.log")
    requests_log.addHandler(fh)

    try:
        # make sure uptime_check() is run with an interval of four times per second
        threading.Timer(0.25, uptime_check).start ()
        response = requests.get("http://web-app:5000/",timeout=30)
        if not response.raise_for_status():
            print("Successful connection,", "Time to Last Byte:", response.elapsed.total_seconds())
    except requests.exceptions.HTTPError as err:
        print(err)

uptime_check()
