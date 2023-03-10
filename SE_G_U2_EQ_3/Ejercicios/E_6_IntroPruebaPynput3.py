import sys
import serial as conecta
from pynput.keyboard import Controller
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E_6_IntroPruebaPynput.ui"  # Nombre del archivo aquí.
controlador = Controller()
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_accion.clicked.connect(self.conexion)
        self.arduino = None
        self.palabra = ""
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)
    # Área de los Slots
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
                        if valor[1] == "1":
                            controlador.press("A")

                        if valor[3] == "1":
                            controlador.press("B")
                        controlador.release("B")
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
