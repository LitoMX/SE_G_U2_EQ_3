int potenciometro = A0;
int tamMuestra = 30;
float mediana;
int i, j;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int datos[tamMuestra];
  for (i = 0; i < tamMuestra; i++) {
    datos[i] = analogRead(potenciometro);  //tomar las muestras
    delay(80);
  }
  Serial.println("muestra bruta:");
  for(i=0;i<tamMuestra;i++){
  	Serial.print(String(datos[i])+"-");
  }

  for (i = 0; i < tamMuestra - 1; i++) {  //acomodar muestra
    for (j = 0; j < (tamMuestra - 1); j++) {
      if (datos[j] > datos[j + 1]) {
        int aux = datos[j];
        datos[j] = datos[j + 1];
        datos[j + 1] = aux;
      }
    }
  }
  Serial.println("");
  Serial.println("muestra acomodada:");
  for(i=0;i<tamMuestra;i++){
  	Serial.print(String(datos[i])+"-");
  }
  
  Serial.println("");
  
  int m = int(tamMuestra / 2);

  if (tamMuestra % 2 == 0) {  //cuando es muestra de numero par
    mediana = (datos[m-1] + datos[m]) / 2.0;
  } else {  //cuando es muestra de numero impar
    mediana = datos[m+1];
  }

  Serial.println(mediana);
  delay(1000);