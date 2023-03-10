//Sensores Analogicos -> 
int pulsador1 = 2;
int pulsador2 = 3;
int pulsador3 = 4;
int pulsador4 = 5;
int pulsador5 = 6;

void setup() {
  // put your setup code here, to run once:
  pinMode(pulsador1, INPUT_PULLUP);
  pinMode(pulsador2, INPUT_PULLUP);
  pinMode(pulsador3, INPUT_PULLUP);
  pinMode(pulsador4, INPUT_PULLUP);
  pinMode(pulsador5, INPUT_PULLUP);

  Serial.begin(9600);
  Serial.setTimeout(10);
}

int sA, sB, sC, sD, sE;

void loop() {
  // put your main code here, to run repeatedly:
  sA = digitalRead(pulsador1) == 1?0:1;
  sB = digitalRead(pulsador2) == 1?0:1; 
  sC = digitalRead(pulsador3) == 1?0:1;
  sD = digitalRead(pulsador4) == 1?0:1; 
  sE = digitalRead(pulsador5) == 1?0:1;  

  //Armar la cadena que se enviará
  String cadena = "P" + String(sA) + " " + String(sB) + " " + String(sC) + " " + String(sD) + " " + String(sE) +  "K";//K de kilo
  Serial.println(cadena);

  delay(200);
}




