import csv
import time
import os
from collections import defaultdict
from pywifi import PyWiFi, const, Profile
from loadpoints import points
from mac_addresses import mac_addresses

    # Add more points as needed
    
point = points[17]  # Change this to the point you are collecting data for

data_file = "fingerprint_data6.csv"

wifi = PyWiFi()
iface = wifi.interfaces()[0]  # Get the first wireless interface

def scan():
    iface.scan()
    time.sleep(2)  # Wait for the scan to complete
    results = iface.scan_results()
    return results

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

row = defaultdict(list)

with open(data_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    header = ["id", "name", "x", "y"] + mac_addresses
    # writer.writerow(header)
    
    # collect data for certain time period
    
    for i in range(10):
        cells = scan()
        for cell in cells:
            if cell.bssid in mac_addresses:
                row[cell.bssid].append(cell.signal)
        time.sleep(0.25)
        
    # print(row)
    
    for mac_address in mac_addresses:
        if mac_address not in row:
            print(mac_address, "not found")
            row[mac_address].extend([-100] * 20)
        elif row[mac_address]:
            while len(row[mac_address]) < 20:
                row[mac_address].append(-100)
            
    
    for i in range(20):
        this_row = [point["id"], point["name"], point["x"], point["y"]]
        for mac_address in mac_addresses:
            this_row.append(row[mac_address][i])
            
        writer.writerow(this_row)
        
    print(f"Data collected for point {point['name']}, {this_row}")

print("Data collection complete. The data is saved in fingerprint_data6.csv.")
