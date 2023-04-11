# Import modules we'll need elsewhere
import time
from machine import Pin
import network
import socket

# Define network credentials
ssid = 'Wi-Fi SSID'
password = 'Wi-Fi Password'

# Use network module to connect to local Wi-Fi
# Create a new Wi-Fi station interface
wlan = network.WLAN(network.STA_IF)

# Activate the interface and connect to the Wi-Fi network
wlan.active(True)
wlan.connect(ssid, password)

# Wait for the interface to obtain an IP address from the DHCP server
while not wlan.isconnected():
    pass

# Print the IP address assigned to the interface
print('')
print('Conexion con la Red %s establecida' % ssid)
print(wlan.ifconfig()) # Show the IP & other data from Wi-Fi

# Outputs
cocina = machine.Pin(2, machine.Pin.OUT)
cafetera = machine.Pin(10, machine.Pin.OUT)

# Set up the webpage
def web_page():
    file = open('index.html','r')
    html = file.read()
    file.close()
    return html

# Handle requests
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))
tcp_socket.listen(3)
while True:
    conn, addr = tcp_socket.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)
    if request.find('/cafetera=on') == 6:
        print('Cafetera ON')
        cafetera.value(1)
    if request.find('/cafetera=off') == 6:
        print('Cafetera OFF')
        cafetera.value(0)
    if request.find('/cocina=on') == 6:
        print('Cafetera ON')
        cocina.value(0)
    if request.find('/cocina=off') == 6:
        print('Cafetera OFF')
        cocina.value(1)
    
    #Mostrar Página
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()