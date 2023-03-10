import sys
import serial as conecta
import random
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "Practica_3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.listapalabras = ['NATURALEZA','BOSQUE','DESIERTO',
                              'ANIMAL','PERRO','GATO','FAMILIA',
                              'DRAGON','GALLINA','SALTAMONTES',
                              'MANZANA','DURAZNO','CALENDARIO']
        self.abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.imagenes = ['Imagenes/1.png',
                         'Imagenes/2.png',
                         'Imagenes/3.png',
                         'Imagenes/4.png',
                         'Imagenes/5.png',
                         'Imagenes/6.png',
                         'Imagenes/7.png']

        # Área de los Signals
        self.btn_accion.clicked.connect(self.conexion)
        self.btn_iniciar.clicked.connect(self.juego)
        self.arduino = None
        self.letra = 0
        self.errores = 0
        self.lletra = "A"
        self.palabra = ""
        self.lpalabra = []
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

    # Área de los Slots
    def juego(self):
        self.btn_iniciar.setText("Reiniciar")
        n = random.randint(0,len(self.listapalabras))
        self.lpalabra = list(self.listapalabras[n])
        print(self.lpalabra)
        self.palabra = ["_"]*len(self.lpalabra)
        p = "   ".join(self.palabra)
        self.lbl_palabra.setText(p)
        self.errores = 0
        self.letra = 0
        self.lletra = self.abecedario[self.letra]
        self.lbl_letra.setText(self.lletra)
        self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.imagenes[self.errores]))

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    #leer
                    valor = self.arduino.readline().decode()
                    valor = valor.replace("\r","")
                    valor = valor.replace("\n","")
                    #print(valor)
                    if not valor == "":
                        #CADENA SERIALIZADA CON LOS DATOS DE LOS SENSORES
                        pase = True
                        if self.errores == 6:
                            pase = False
                        if pase:
                            if valor[1] == "1":
                                if self.letra < 26:
                                    self.letra += 1
                                else:
                                    self.letra = 0
                                self.lletra = self.abecedario[self.letra]
                                self.lbl_letra.setText(self.lletra)
                            if valor[3] == "1":
                                bandera = False
                                for i in range(len(self.lpalabra)):
                                    if self.lpalabra[i] == self.lletra:
                                        self.palabra[i] = self.lletra
                                        p = "   ".join(self.palabra)
                                        self.lbl_palabra.setText(p)
                                        bandera = True
                                if not bandera:
                                    self.errores += 1
                                    self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.imagenes[self.errores]))
                        else:
                            self.lbl_palabra.setText('P   E   R   D   I   S   T   E')

    def conexion(self):
        try:
            txt_btn = self.btn_accion.text()
            if txt_btn == "CONECTAR":  ##arduino == None
                self.txt_estado.setText("CONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                # puerto = self.txt_puerto.text()
                puerto = "COM" + self.txt_puerto.text()
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)
            elif txt_btn == "DESCONECTAR":
                self.txt_estado.setText("DESCONECTADO")
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.arduino.close()
            else:  # RECONECTAR
                self.txt_estado.setText("RECONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                self.segundoPlano.start(100)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
