#!usr/bin/env python3
from datetime import datetime

with open("deployment.txt","w+") as file: #"w+" means the file will be overwritten each time
    file.write("This container was deployed at %s." %datetime.now())
    file.close