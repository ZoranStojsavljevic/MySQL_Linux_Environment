#!/usr/bin/python3

from datetime import datetime

now = datetime.now()
print ("--- now ---", now)
print ("--- str(now) ---", str(now))

dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
print("--- dt_string ---", dt_string)

dt_object = now.strftime('%Y-%m-%d %H:%M:%S')
print("--- dt_object ---", dt_object)
print("--- dt_object {}.format(dt_object) ---", dt_object)
