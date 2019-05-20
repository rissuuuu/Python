import time
from datetime import datetime as dt

host_temp="hosts"
host_path="C:\\Users\\Rishav\\Documents\\hosts"
redirect="172.0.0.1"
website_list=["www.facebook.com","WWW.facebook.com","facebook.com","fb.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,16) <(dt.now()) < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("True")
        with open(host_path,'r+') as file:
            content=file.read()
            print(content)

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            lines=file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(100)