import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Practica_1.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.idDato =0
        # Área de los Signals
        self.btn_accion.clicked.connect(self.conexion)
        self.btn_visual.clicked.connect(self.visualizacion)
        self.arduino = None
        self.visual=True
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

    # Área de los Slots

    def conexion(self):
        try:
            if not self.txt_puerto.text() =="":
                txt_btn = self.btn_accion.text()
                if txt_btn == "CONECTAR": ##arduino == None
                    self.txt_estado.setText("CONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    #puerto = self.txt_puerto.text()
                    puerto = "COM" + self.txt_puerto.text()
                    self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                    self.segundoPlano.start(100)
                elif txt_btn == "DESCONECTAR":
                    self.txt_estado.setText("DESCONECTADO")
                    self.btn_accion.setText("RECONECTAR")
                    self.segundoPlano.stop()
                    self.arduino.close()
                else: #RECONECTAR
                    self.txt_estado.setText("RECONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    self.arduino.open()
                    self.segundoPlano.start(500)
        except Exception as error:
            print(error)
        #self.arduino.isOpen()

    def control(self):
        try:

            if not self.arduino == None:
                if self.arduino.isOpen:
                    variable = self.arduino.readline().decode()
                    variable = variable.replace("\r","")
                    variable = variable.replace("\n","")
                    if not variable =="":
                        self.archivo = open("datos.csv", "a")
                        if self.visual:
                            self.lw_datos.addItem(variable)
                            self.lw_datos.setCurrentRow(self.lw_datos.count()-1)
                            self.archivo.write("---,"+str(variable) + "\n")
                        else:
                            self.archivo.write(str(self.idDato) + "," + str(variable) + "\n")
                            self.archivo.close()
                            self.idDato += 1
        except Exception as error:
            print(error)

    def visualizacion(self):
        try:
            if not self.arduino == None:
                if self.btn_visual.text()=="Visualizar":
                    self.btn_visual.setText("No Visualizar")
                    self.visual=True
                else:
                    self.btn_visual.setText("Visualizar")
                    self.visual = False
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())