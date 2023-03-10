import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "Practica_4.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> object:
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.conexion)
        self.btn_iniciar.clicked.connect(self.juego)

        self.arduino = None
        self.posicion = "1"
        self.turno = "X"
        self.iniciar = False
        self.victoria = False
        self.numero = 1
        self.gato=[self.n1,self.n2,self.n3,
                  self.n4,self.n5,self.n6,
                  self.n7,self.n8,self.n9]

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

    # Área de los Slots
    def juego(self):
        self.btn_iniciar.setText("Reiniciar")
        self.lbl_turno_jugador.setText(self.txt_nombre1.text())
        self.iniciar = True
        self.Ganador.setText("Ganador:")
        self.victoria = False
        for i in range(0, len(self.gato)):
            self.gato[i].setText("")

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting() and self.iniciar == True:
                    # leer
                    valor = self.arduino.readline().decode()
                    valor = valor.replace("\r", "")
                    valor = valor.replace("\n", "")
                    if not valor == "" and self.victoria == False:
                        # IZQUIERDA
                        if valor[7] == "1":
                            if self.posicion != "1" and self.posicion != "4" and self.posicion != "7":
                                self.numero = int(self.posicion) - 1
                        # ARRIBA
                        if valor[5] == "1":
                            if self.posicion != "1" and self.posicion != "2" and self.posicion != "3":
                                self.numero = int(self.posicion) - 3
                        # ABAJO
                        if valor[3] == "1":
                            if self.posicion != "7" and self.posicion != "8" and self.posicion != "9":
                                self.numero = int(self.posicion) + 3
                        # DERECHA
                        if valor[1] == "1":
                            if self.posicion != "3" and self.posicion != "6" and self.posicion != "9":
                                self.numero = int(self.posicion) + 1

                        self.posicion = str(self.numero)
                        print("posicion == " + self.posicion)

                        if valor[9] == "0":
                            # JUGADOR MOVIMIENTO EN EL GATO
                            for i in range(0, len(self.gato)):
                                if self.gato[i].objectName()[1] == str(self.numero) and self.gato[i].text() != "X" and self.gato[i].text() != "O":
                                    self.gato[i].setText("Aqui")
                                    for j in range(0, len(self.gato)):
                                        if j != i and self.gato[j].text() != "X" and self.gato[j].text() != "O":
                                            self.gato[j].setText("")
                                elif self.gato[i].objectName()[1] == str(self.numero) and self.gato[i].text() == "X" or self.gato[i].objectName()[1] == str(self.numero) and self.gato[i].text() == "O":
                                    for z in range(0, len(self.gato)):
                                        if self.gato[z].text() != "X" and self.gato[z].text() != "O":
                                            self.gato[z].setText("")

                        elif valor[9] == "1":
                            # SELECCIONAR CASILLA TURNO JUGADOR 1
                            if str(self.lbl_turno_jugador.text()) == str(self.txt_nombre1.text()):
                                for i in range(0, len(self.gato)):
                                    if self.gato[i].objectName()[1] == str(self.numero) and self.gato[i].text() != "X" and self.gato[i].text() != "O":
                                        self.gato[i].setText("X")
                                        self.ganador()
                                        print("entro3")
                                        # CAMBIAR TURNO
                                        self.lbl_turno_jugador.setText(self.txt_nombre2.text())
                                        self.turno = "O"
                                    elif self.gato[i].text() == "X" or self.gato[i].text() == "O":
                                        print("No se puede")

                            # SELECCIONAR CASILLA TURNO JUGADOR 2
                            if self.lbl_turno_jugador.text() == self.txt_nombre2.text():
                                for i in range(0, len(self.gato)):
                                    if self.gato[i].objectName()[1] == str(self.numero) and self.gato[i].text() != "X" and self.gato[i].text() != "O":
                                        self.gato[i].setText("O")
                                        self.ganador()
                                        # CAMBIAR TURNO
                                        self.lbl_turno_jugador.setText(self.txt_nombre1.text())
                                        self.turno = "X"
                                    elif self.gato[i].text() == "X" or self.gato[i].text() == "O":
                                        print("No se puede")

    def ganador(self):
        if self.gato[0].text() == self.turno and self.gato[1].text() == self.turno and self.gato[2].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[3].text() == self.turno and self.gato[4].text() == self.turno and self.gato[5].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[6].text() == self.turno and self.gato[7].text() == self.turno and self.gato[8].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[0].text() == self.turno and self.gato[3].text() == self.turno and self.gato[6].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[1].text() ==  self.turno and self.gato[4].text() == self.turno and self.gato[7].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[2].text() == self.turno and self.gato[5].text() == self.turno and self.gato[8].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[0].text() ==  self.turno and self.gato[4].text() == self.turno and self.gato[8].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")
        elif self.gato[2].text() == self.turno and self.gato[4].text() == self.turno and self.gato[6].text() == self.turno:
            print("Gano: " + self.turno)
            self.victoria = True
            self.Ganador.setText("Ganador: " + self.lbl_turno_jugador.text() + " (" + self.turno + ")")

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
