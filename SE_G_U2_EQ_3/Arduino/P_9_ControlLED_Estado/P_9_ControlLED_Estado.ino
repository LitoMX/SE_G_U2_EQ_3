/*
    De python a Arduino
    Tiempo de ejecucion de cuando llegó la info
    Tiempo cuando no hay información y el tiempo de espera es menor
    Solo se puede recibir 0/1
*/

int led = 13; //pin digital de pruebas de Arduino

void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);//ms por defecto 1000
}

int estado = 0;

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    estado = Serial.readString().toInt();
    digitalWrite(led, estado);
  }

  Serial.println(estado);
  delay(10);
}
