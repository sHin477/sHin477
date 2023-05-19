#!//usr/bin/python3
import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

target = input(str("Podaj IP\Domene: "))

print("-" * 50)
print("Skanowanie Celu: " + target)
print("Skanowanie rozpoczete: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        rezultat = s.connect_ex((target,port))
        if rezultat == 0:
            print("[*] Port {} otwarty".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Wychodze z Programu!!!!")
    sys.exit()
except socket.gaierror:
    print("\n Nazwa Hosta nieprawidlowa!!!!")
    sys.exit()
except socket.error:
    print("\n Server nie odpowiada!!!!")