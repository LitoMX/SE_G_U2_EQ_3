int potenciometro = A0;
int tamMuestra = 30;
String moda="";
int valor;
int vecesNuev;
int vecesAnt;
int vecesMax;
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
  
  Serial.println("\nmuestra bruta:");
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

  valor=datos[0];
  vecesNuev=1;
  vecesAnt=0;
  for (i=1;i<tamMuestra;i++){ 		//saber cuantas veces es el maximo q se repite un numero
    if(valor==datos[i]){			//almacenando el valor maximo de repeticiones de los numeros
      vecesNuev++;
    }
    else{
      if(vecesNuev>vecesAnt){
        vecesAnt=vecesNuev;
      }
      valor=datos[i];
      vecesNuev=1;
    }
  }
  Serial.println(String(vecesAnt)+" ant "+String(vecesNuev)+" nuev");
  
  if(vecesNuev>vecesAnt){
    vecesMax=vecesNuev;
  }
  else if(vecesNuev<vecesAnt){
    vecesMax=vecesAnt;
  }
  Serial.println(String(vecesMax)+" maximo");
  valor=datos[0];
  vecesNuev=1;
  moda="";
  for(i=1;i<tamMuestra;i++){    	//recorrer nuevamente para buscar los valores que repiten el mismo numero de veces maxima
    if(valor==datos[i]){        
      vecesNuev++;
      if(vecesNuev==vecesMax){	//en caso de que sean varias modas se agregan cada una de ellas
      moda=moda+","+String(valor);	//y en caso de que sea una moda solo esa se agrega
      }
    }else{
      valor=datos[i];
      vecesNuev=1;
    
    }
  }

  Serial.println("");
  Serial.println(moda);
  delay(1000);
}