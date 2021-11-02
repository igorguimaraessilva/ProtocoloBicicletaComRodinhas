import time
from datetime import datetime as dt

hostPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

wesites = ["www.youtube.com", "youtube.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Sorry Not Allowed...")
        with open(hostPath, 'r+') as file:
            content = file.read()
            for site in website:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(hostPath, 'r+') as file:
            content = file.redlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website):
                    file.write(line)
            file.truncate()
        print("Allowed access!")
    time.sleep(5)
