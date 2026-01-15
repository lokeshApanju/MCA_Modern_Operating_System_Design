import platform
import os
import socket

print("===== System Information =====")

# Operating System details
print("OS Name:", platform.system())
print("OS Version:", platform.release())
print("OS Full Version:", platform.version())

# Machine and Processor details
print("Machine Type:", platform.machine())
print("Processor:", platform.processor())

# Hostname and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP Address:", ip_address)

# Python version
print("Python Version:", platform.python_version())

# Current Working Directory
print("Current Directory:", os.getcwd()) 
