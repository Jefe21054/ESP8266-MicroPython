# boot.py -- run on boot-up
import network

# Replace the following with your WIFI Credentials
ssid = 'your_ssid'
password = 'your_password'

def do_connect():
    import network
    # Use network module to connect to local Wi-Fi
    # Create a new Wi-Fi station interface
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('Conectando...')
        # Activate the interface and connect to the Wi-Fi network
        wlan.active(True)
        wlan.connect(ssid, password)
        # Wait for the interface to obtain an IP address from the DHCP server
        while not wlan.isconnected():
            pass
    # Print the IP address assigned to the interface
    print('')
    print('Conexion con la Red %s establecida' % ssid)
    print('Conectado! Parametros de Red:', sta_if.ifconfig()) # Show the IP & other data from Wi-Fi

print("Conectandose a una red Wi-Fi...")
do_connect()