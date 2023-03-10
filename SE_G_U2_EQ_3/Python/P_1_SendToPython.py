import serial as s

arduino = None

arduino = s.Serial("COM3", baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline()
    #print/cadena ## imprime como...b'419\r\n'
    cadena = cadena.decode()
    #print(cadena) ##imprime como...
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r", "")
    print(cadena * 2) #<<------