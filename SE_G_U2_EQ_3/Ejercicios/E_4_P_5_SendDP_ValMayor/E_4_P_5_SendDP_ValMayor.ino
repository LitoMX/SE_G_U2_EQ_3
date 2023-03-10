int potenciometro = A0;
int tamMuestra = 30;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

int valMayor = -1;
int i,valor;
void loop() {
  // put your main code here, to run repeatedly:
  //Preprocesamiento de datos...
  for(i=0;i<tamMuestra; i++){
    valor = analogRead(potenciometro); //buscar dismunuir el efecto del ruido

    if(valor>valMayor){
      valMayor = valor;
    }

  }

  //Serial.println("Valor=" + String(valor));
  Serial.println(valMayor);
  delay(1000);
}
//Ejercicio 1. Moda
//Ejercicio 2. Mediana. ***
// /dev/cu.usbmodem1101