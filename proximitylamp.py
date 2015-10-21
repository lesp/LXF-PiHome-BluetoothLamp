import bluetooth
from energenie import switch_on, switch_off
import time


#print(nearby_devices[0])
try:
    while True:
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=False, flush_cache=True, lookup_class=False)
        if "4C:74:03:67:C9:6E" in nearby_devices:
            print("LIGHT ON")
            switch_on()
            status = ON
            nearby_devices = []
        else:
            print("LIGHT OFF")
            switch_off()
        time.sleep(5)
except KeyboardInterrupt:
    print("Exit")
    
    
