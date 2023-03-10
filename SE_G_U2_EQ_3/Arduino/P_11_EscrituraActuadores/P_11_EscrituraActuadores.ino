int vA,vB,vC;


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    String c = Serial.readString();
    //Serial.println(c); // Confirmación de la lectura recibida
    //E001R010R2203
    if(c.lenght()=13){
      if(c.charAt(0)='E'&&c.charAt(c.lenght()-1)=='C'){//Segunda validación
        //E001R056R300C
        c = c.substring(1,c.lenght()-1 + 'R');
        Serial.println("L: " + c + "T");
        int cont = 0;
        String temp = "";
        for(int i = 0; i<c.lenght(); i++){
          if(c.charAt(i) != 'R'){
            temp += c.charAt(i);
          }
          else{
            switch(cont){
              case 0:
                vA = temp.toInt();
              break;
              case 1:
                vB = temp.toInt();
              break;
              case 2:
                vC = temp.toInt();
              break;
            }
            temp = "";
            cont++;
          }
        }
        Serial.println(String(vA) + "   " + String(vB) + "   " + String(vC));
      }
    }
  }

}
