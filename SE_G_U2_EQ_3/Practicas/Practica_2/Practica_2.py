import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Practica_2.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_conectar.clicked.connect(self.conexion)
        self.btn_ingresar.clicked.connect(self.ingresar)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_verificar.clicked.connect(self.verificar)
        self.btn_ingresar.setEnabled(False)
        self.btn_iniciar.setEnabled(False)
        self.txt_palabraAdivinar.setEnabled(False)
        self.btn_verificar.setEnabled(False)
        self.txt_palabraDetectada.setEnabled(False)
        self.txt_estado.setStyleSheet("background-color: lightgrey")
        self.arduino = None
        self.palabra = ""
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.encenderLeds)

    # Área de los Slots

    def conexion(self):
        try:
            if not self.txt_puerto.text() == "":
                txt_btn = self.btn_conectar.text()
                if txt_btn == "CONECTAR":  ##arduino == None
                    self.txt_estado.setText("CONECTADO")
                    self.btn_conectar.setText("DESCONECTAR")
                    puerto = "COM" + self.txt_puerto.text()
                    self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                    self.btn_ingresar.setEnabled(True)
                    self.btn_iniciar.setEnabled(True)
                    self.txt_palabraAdivinar.setEnabled(True)
                    self.txt_estado.setStyleSheet("background-color: lime")
                elif txt_btn == "DESCONECTAR":
                    self.txt_estado.setText("DESCONECTADO")
                    self.btn_conectar.setText("RECONECTAR")
                    self.segundoPlano.stop()
                    self.arduino.close()
                    self.btn_ingresar.setEnabled(False)
                    self.btn_iniciar.setEnabled(False)
                    self.txt_palabraAdivinar.setEnabled(False)
                    self.txt_estado.setStyleSheet("background-color: red")
                else:  # RECONECTAR
                    self.txt_estado.setText("RECONECTADO")
                    self.btn_conectar.setText("DESCONECTAR")
                    self.arduino.open()
                    self.btn_ingresar.setEnabled(True)
                    self.btn_iniciar.setEnabled(True)
                    self.txt_palabraAdivinar.setEnabled(True)
                    self.txt_estado.setStyleSheet("background-color: lime")
        except Exception as error:
            print(error)

    def encenderLeds(self):
        ascci = "E+" + str(len(self.palabra) + 1) + "+"
        for letra in self.palabra:
            ascci += str(ord(letra))+"+"
        ascci += "0+C"
        self.arduino.write(ascci.encode())
        variable = self.arduino.readline().decode()
        variable = variable.replace("\r", "")
        variable = variable.replace("\n", "")
        print(variable)
        if variable=="dato>>0":
            self.segundoPlano.stop()
            print("se detuvo")

    def iniciar(self):
        try:
            if not self.arduino == None:
                if self.arduino.isOpen:
                    if not self.palabra == "":
                        self.segundoPlano.start(10)
                        self.btn_verificar.setEnabled(True)
                        self.txt_palabraDetectada.setEnabled(True)
        except Exception as error:
            print(error)

    def ingresar(self):
        try:
            if not self.arduino == None and self.arduino.isOpen():
                if not self.txt_palabraAdivinar.text() == "":
                    self.palabra = self.txt_palabraAdivinar.text()
                    self.txt_palabraAdivinar.setText("******")
        except Exception as error:
            print(error)

    def verificar(self):
        try:
            if not self.txt_palabraDetectada.text() == "":
                if self.txt_palabraDetectada.text() == self.palabra:
                    self.lbl_resultado.setStyleSheet("background-color: lime")
                    self.lbl_resultado.setText("CORRECTO")
                    print("igual")
                else:
                    self.lbl_resultado.setStyleSheet("background-color: red")
                    self.lbl_resultado.setText("INCORRECTO")
                    print("no es igual")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
