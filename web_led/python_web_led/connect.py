
# Turn off vendor messages
# import esp
# esp.osdebug(None)

def connect():
    import network
    import utime

    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.scan()
    nic.connect('VM0455243', 'Rj9wnjygvDpj')
    # nic.connect('HUAWEI_Honor8_ECB1', '23ba0766')

    print("Waiting for connection...")
    
    while not nic.isconnected():
        utime.sleep(0.1)
    print(nic.ifconfig())
