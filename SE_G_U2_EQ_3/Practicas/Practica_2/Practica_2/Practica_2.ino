int led[] = { 2, 3, 4, 5, 6, 7, 8, 9 };  //pin 13 = pin digital de pruebas de Arduino
String cadenaRecib = "";  //E+numLetras+?+C
int i;
const char separador = '+';
int numLetras;
int binario[8];

void setup() {
  // put your setup code here, to run once:
  for (i = 0; i < 8; i++) {
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);  //ms por defecto 1000
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    cadenaRecib = Serial.readString();
    Serial.println("CadenaReciv>>"+cadenaRecib);
    if (cadenaRecib.indexOf("E") == 0 && cadenaRecib.indexOf("C") == cadenaRecib.length() - 1) {
      numLetras = cadenaRecib.substring(2, 4).toInt();
      Serial.println(String("NumLetras>>"+String(numLetras)));
      //String binario[numLetras];
      cadenaRecib = cadenaRecib.substring(4, cadenaRecib.length() - 2);
      Serial.println("cadenaAcortada>>"+cadenaRecib);
      for (i = 0; i < numLetras; i++) {
        int index = cadenaRecib.indexOf(separador);
        int dato = cadenaRecib.substring(0, index).toInt();
        Serial.println("dato>>"+String(dato));
        String assci = "";
        for (i = 7; i >= 0; i--) {
          binario[i] = dato % 2;
          if(dato>0){
            dato = dato / 2;
          }
        }
        digitalWrite(led[0], binario[0]);
        digitalWrite(led[1], binario[1]);
        digitalWrite(led[2], binario[2]);
        digitalWrite(led[3], binario[3]);
        digitalWrite(led[4], binario[4]);
        digitalWrite(led[5], binario[5]);
        digitalWrite(led[6], binario[6]);
        digitalWrite(led[7], binario[7]);
        delay(1000);
        digitalWrite(led[0], binario[0]);
        digitalWrite(led[1], binario[0]);
        digitalWrite(led[2], binario[0]);
        digitalWrite(led[3], binario[0]);
        digitalWrite(led[4], binario[0]);
        digitalWrite(led[5], binario[0]);
        digitalWrite(led[6], binario[0]);
        digitalWrite(led[7], binario[0]);
        delay(300);
        cadenaRecib = cadenaRecib.substring(index + 1);
        
      }
    }
  }
}

 