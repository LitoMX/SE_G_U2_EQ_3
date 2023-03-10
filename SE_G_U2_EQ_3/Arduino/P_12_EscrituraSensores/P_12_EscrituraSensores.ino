//Sensores Analogicos -> 

int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int sA, sB, sC;

void loop() {
  // put your main code here, to run repeatedly:
  sA = analogRead(sensor1);
  sB = analogRead(sensor2);
  sC = analogRead(sensor3);

  //Armar la cadena que se enviará
  String cadena = "P" + String(sA) + " " + String(sB) + " " + String(sC) + "K";//K de kilo
  Serial.println(cadena);

  delay(500);
}
