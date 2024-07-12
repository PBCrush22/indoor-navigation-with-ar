import csv
import time
import os
from pywifi import PyWiFi, const, Profile

reference_points = [
    {"id": 1, "name": "Point 1", "lat": 3.063812, "long": 101.600382},
    {"id": 2, "name": "Point 2", "lat": 3.063822, "long": 101.600392},
    # Add more points as needed
]

list1 = [
    "70:b3:17:6e:99:4d",
    "70:b3:17:29:bb:6d",
    "70:b3:17:6e:a4:02",
    "70:b3:17:2a:8a:02",
    "70:b3:17:3b:33:62",
    "70:b3:17:6e:83:0d",
    "70:b3:17:6e:99:42",
    "70:b3:17:6e:99:ed",
    "70:b3:17:6e:66:42",
    "70:b3:17:6e:a5:4d",
    "70:b3:17:6e:99:e2",
    "70:b3:17:6e:54:ed",
    "70:b3:17:42:ca:c2",
    "70:b3:17:69:ce:62",
    "70:b3:17:3c:1d:82",
    "70:b3:17:70:8b:8d",
    "70:b3:17:29:bb:62",
    "70:b3:17:4e:93:0d",
    "70:b3:17:6e:83:02",
    "70:b3:17:6e:a5:c2",
    "70:b3:17:70:9a:62",
    "70:b3:17:3c:1d:8d",
    "70:b3:17:70:9a:6d",
    "70:b3:17:6e:83:cd",
    "70:b3:17:57:b2:e2",
    "70:b3:17:6e:a8:42",
    "70:b3:17:6e:a4:82",
    "70:b3:17:57:dd:02",
    "70:b3:17:42:ca:cd",
    "70:b3:17:4e:13:22",
    "70:b3:17:70:97:8d",
    "70:b3:17:70:97:82",
    "70:b3:17:6e:83:c2",
    "70:b3:17:70:77:4d",
    "70:b3:17:4d:d7:42",
    "78:bc:1a:d2:4e:4d",
    "70:b3:17:57:dd:0d",
    "70:b3:17:57:b2:ed",
    "70:b3:17:70:97:8d",
    "70:b3:17:70:8c:c2",
    "78:bc:1a:d2:60:02",
    "70:b3:17:6e:98:4d",
    "70:b3:17:6e:98:e2",
    "70:b3:17:6e:a5:e2",
    "70:b3:17:6e:83:0d",
    "70:b3:17:4e:e3:4d",
    "70:b3:17:6e:a4:82",
    "70:b3:17:70:97:82",
    "70:b3:17:70:8b:8d",
    "70:b3:17:6e:98:ed",
    "70:b3:17:6d:1c:c2",
    "70:b3:17:70:99:ed",
    "70:b3:17:6e:a4:02",
    "70:b3:17:70:75:e2",
    "70:b3:17:6e:54:ed",
    "70:b3:17:6e:68:82",
    "70:b3:17:59:04:a2",
    "70:b3:17:70:75:ed",
    "70:b3:17:70:77:4d",
    "70:b3:17:6e:a4:8d",
    "70:b3:17:70:8b:82",
    "70:b3:17:6e:68:8d",
    "70:b3:17:6e:98:42",
    "70:b3:17:70:9a:4d",
    "70:b3:17:4e:e3:42",
    "70:b3:17:6e:83:0d",
    "70:b3:17:70:8c:cd",
    "70:b3:17:6e:98:4d",
    "70:b3:17:70:75:ed",
    "70:b3:17:4e:e3:4d",
    "70:b3:17:6e:68:8d",
    "70:b3:17:70:8b:8d",
    "70:b3:17:6e:98:ed",
    "70:b3:17:70:99:ed",
    "70:b3:17:70:8e:ed",
    "70:b3:17:6e:a6:82",
    "70:b3:17:6e:98:e2",
    "70:b3:17:6e:a5:ad",
    "70:b3:17:6e:a4:82",
    "70:b3:17:70:8c:c2",
    "70:b3:17:6e:68:82",
    "70:b3:17:6e:a6:e2",
    "78:bc:1a:d2:60:02",
    "70:b3:17:70:97:8d",
    "70:b3:17:59:04:a2",
    "70:b3:17:59:04:ad",
    "70:b3:17:70:97:82",
    "70:b3:17:70:75:e2",
    "70:b3:17:70:77:4d",
    "70:b3:17:70:8b:82",
     "70:b3:17:70:9a:62",
    "70:b3:17:6e:a5:42",
    "70:b3:17:6e:66:4d",
    "70:b3:17:6d:22:02",
    "70:b3:17:70:8c:a2",
    "70:b3:17:6e:a4:02",
    "70:b3:17:6e:a4:8d",
    "70:b3:17:6e:a5:4d",
    "70:b3:17:6e:98:e2",
    "70:b3:17:70:97:ed",
    "78:bc:1a:d2:60:02",
    "70:b3:17:6e:a6:62",
    "70:b3:17:6e:66:42",
    "70:b3:17:6e:54:ed",
    "74:88:bb:4f:20:a2",
    "70:b3:17:70:8b:8d",
    "70:b3:17:70:75:ed",
    "70:b3:17:6e:83:0d",
    "70:b3:17:6e:83:02",
    "70:b3:17:70:8b:82",
    "70:b3:17:57:af:62",
    "70:b3:17:6e:a7:42",
    "70:b3:17:6e:a4:a2",
    "70:b3:17:70:75:e2",
    "70:b3:17:4e:98:02",
    "74:88:bb:4f:57:c2",
    "70:b3:17:6e:a6:6d",
    "74:88:bb:4f:57:cd",
    "70:b3:17:6e:99:e2",
    "70:b3:17:6e:68:6d",
    "70:b3:17:70:97:e2",
    "70:b3:17:70:97:82",
    "78:bc:1a:d2:4a:82",
    "70:b3:17:6e:a4:22",
    "70:b3:17:4e:e3:4d",
    "74:88:bb:31:7f:22",
    "70:b3:17:6e:83:cd",
    "70:b3:17:6e:a7:0d",
    "78:bc:1a:d2:60:0d",
    "70:b3:17:70:77:42",
    "70:b3:17:70:97:8d",
    "70:b3:17:2a:7f:42",
    "70:b3:17:6e:68:4d",
    "70:b3:17:69:ce:e2",
    "70:b3:17:3b:b2:ed",
    "70:b3:17:6e:a4:82",
    "70:b3:17:6e:99:ed",
    "70:b3:17:6e:68:8d",
    "70:b3:17:6e:68:82",
    "70:b3:17:6e:a6:c2",
    "70:b3:17:6e:a8:42",
    "70:b3:17:70:77:4d",
    "70:b3:17:70:9a:62",
    "70:b3:17:6e:a5:42",
    "70:b3:17:6e:66:4d",
    "70:b3:17:6d:22:02",
    "70:b3:17:70:8c:a2",
    "70:b3:17:6e:a4:02",
    "70:b3:17:6e:a4:8d",
    "70:b3:17:6e:a5:4d",
    "70:b3:17:6e:98:e2",
    "70:b3:17:70:97:ed",
    "78:bc:1a:d2:60:02",
    "70:b3:17:6e:a6:62",
    "70:b3:17:6e:66:42",
    "70:b3:17:6e:54:ed",
    "74:88:bb:4f:20:a2",
    "70:b3:17:70:8b:8d",
    "70:b3:17:70:75:ed",
    "70:b3:17:6e:83:0d",
    "70:b3:17:6e:83:02",
    "70:b3:17:70:8b:82",
    "70:b3:17:57:af:62",
    "70:b3:17:6e:a7:42",
    "70:b3:17:6e:a4:a2",
    "70:b3:17:70:75:e2",
    "70:b3:17:4e:98:02",
    "74:88:bb:4f:57:c2",
    "70:b3:17:6e:a6:6d",
    "74:88:bb:4f:57:cd",
    "70:b3:17:6e:99:e2",
    "70:b3:17:6e:68:6d",
    "70:b3:17:70:97:e2",
    "70:b3:17:70:97:82",
    "78:bc:1a:d2:4a:82",
    "70:b3:17:6e:a4:22",
    "70:b3:17:4e:e3:4d",
    "74:88:bb:31:7f:22",
    "70:b3:17:6e:83:cd",
    "70:b3:17:6e:a7:0d",
    "78:bc:1a:d2:60:0d",
    "70:b3:17:70:77:42",
    "70:b3:17:70:97:8d",
    "70:b3:17:2a:7f:42",
    "70:b3:17:6e:68:4d",
    "70:b3:17:69:ce:e2",
    "70:b3:17:3b:b2:ed",
    "70:b3:17:6e:a4:82",
    "70:b3:17:6e:99:ed",
    "70:b3:17:6e:68:8d",
    "70:b3:17:6e:68:82",
    "70:b3:17:6e:a6:c2",
    "70:b3:17:6e:a8:42",
    "70:b3:17:70:77:4d",
    "70:b3:17:6e:a5:42",
    "70:b3:17:6e:66:4d",
    "70:b3:17:6e:a5:4d",
    "70:b3:17:57:ad:8d",
    "70:b3:17:6e:99:4d",
    "70:b3:17:6e:a6:62",
    "70:b3:17:6e:66:42",
    "70:b3:17:6e:83:0d",
    "70:b3:17:6e:a8:42",
    "70:b3:17:6e:a6:6d",
    "70:b3:17:70:8b:cd",
    "70:b3:17:6e:54:4d",
    "70:b3:17:3c:1d:8d",
    "70:b3:17:69:fa:62",
    "70:b3:17:57:b3:ed",
    "70:b3:17:70:76:82",
    "70:b3:17:6e:99:ed",
    "70:b3:17:6e:54:42",
    "70:b3:17:6e:83:cd",
    "70:b3:17:6e:a6:c2",
    "70:b3:17:70:76:8d",
    "70:b3:17:70:77:4d",
    "70:b3:17:6e:a8:4d",
    '70:b3:17:70:97:02',
    '70:b3:17:70:97:02',
    '70:b3:17:70:97:02',
    '70:b3:17:70:97:02',
        '70:b3:17:6e:a7:4d',
    '74:88:bb:4a:ce:62',
    '70:b3:17:57:b3:2d',
    '70:b3:17:6e:a4:0d',
    '70:b3:17:57:af:6d',
    '70:b3:17:70:9c:cd',
    '74:88:bb:31:7f:2d',
    '70:b3:17:6e:a7:4d',
    '74:88:bb:4a:ce:62',
    '70:b3:17:57:b3:2d',
    '70:b3:17:6e:a4:0d',
    '70:b3:17:57:af:6d',
    '70:b3:17:70:9c:cd',
    '74:88:bb:31:7f:2d',
    '70:b3:17:6e:a7:4d',
    '74:88:bb:4a:ce:62',
    '70:b3:17:57:b3:2d',
    '70:b3:17:6e:a4:0d',
    '70:b3:17:57:af:6d',
    '70:b3:17:70:9c:cd',
    '74:88:bb:31:7f:2d',
        '70:b3:17:6e:a4:ad',
    '70:b3:17:58:2e:0d',
    '70:b3:17:6e:68:0d',
    '74:88:bb:4a:b5:02',
    '74:88:bb:4f:20:ad',
    '70:b3:17:70:8c:ad',
    '70:b3:17:6e:a4:ad',
    '70:b3:17:58:2e:0d',
    '70:b3:17:6e:68:0d',
    '74:88:bb:4a:b5:02',
    '74:88:bb:4f:20:ad',
    '70:b3:17:70:8c:ad',
    '70:b3:17:6e:a4:ad',
    '70:b3:17:58:2e:0d',
    '70:b3:17:6e:68:0d',
    '74:88:bb:4a:b5:02',
    '74:88:bb:4f:20:ad',
    '70:b3:17:70:8c:ad',
    '70:b3:17:6e:a4:ad',
    '70:b3:17:58:2e:0d',
    '70:b3:17:6e:68:0d',
    '74:88:bb:4a:b5:02',
    '74:88:bb:4f:20:ad',
    '70:b3:17:70:8c:ad'
]

data_file = "fingerprint_data.csv"

wifi = PyWiFi()
iface = wifi.interfaces()[0]  # Get the first wireless interface

def scan():
    iface.scan()
    time.sleep(2)  # Wait for the scan to complete
    results = iface.scan_results()
    return results

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# with open(data_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["id", "name", "lat", "long", "ssid", "bssid", "rssi", "time"])
new = []
for point in reference_points:
    cells = scan()
    for cell in cells:
        if cell.ssid == "eduroam":
            new.append(cell.bssid)
            
print(new)

print("---")
for x in new:
    x = x[:-1]
    if x not in list1:
        print(x)
