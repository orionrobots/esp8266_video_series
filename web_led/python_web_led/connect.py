
# Turn off vendor messages
# import esp
# esp.osdebug(None)

def connect():
    import network
    import utime

    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.scan()

    nic.connect('SSID', 'KEY')

    print("Waiting for connection...")
    
    while not nic.isconnected():
        utime.sleep(0.1)
    print(nic.ifconfig())
