

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

String cadena;
char *c;
char *token;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    // 100R567R041
    cadena = Serial.readString();
    c = cadena.c_str();
    
    Serial.println("Cadena Completa: ");
    Serial.println(c);
    
    token = strtok(c,"R"); //Tokeniza la cadena

    while(token != NULL){
      Serial.println(token);
      token = strtok(NULL,"R");
    }


    Serial.println("Acceso a la ubicacion de memoria de los tokens: ");
    Serial.println(&c[0]);
    Serial.println(&c[4]);
    Serial.println(&c[8]);

    Serial.print("Cadena despues de tokenizar:");
    Serial.println(c);



  }

  delay(10);
}