#!/usr/bin/python3

import pyfiglet
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

from shutil import which

import os


ip_address = input("Tu wpisz IP: ")

print(f"Skanowanie {ip_address}, To moze troche potrwac...")
command = "nmap -F -Pn -sV --stats-every 1s " + ip_address
nmap_output = os.popen(command).read()
print(nmap_output)
with open("wynik_skanu.txt", "w+") as f:
  f.write(nmap_output)

print("Skanowanie ukonczone!");