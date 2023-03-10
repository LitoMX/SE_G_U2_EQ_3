int potenciometro = A0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

int i,valor;
void loop() {
  // put your main code here, to run repeatedly:
  //Preprocesamiento de datos...
  for(i=0;i<10; i++){
    valor += analogRead(potenciometro); //buscar dismunuir el efecto del ruido
  }
  valor /=10;

  //Serial.println("Valor=" + String(valor));
  Serial.println(valor);
  delay(1000);
}
// /dev/cu.usbmodem1101