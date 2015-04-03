
int led = 13;

void setup() {                
  
  pinMode(led, OUTPUT);     
}


void loop() {
  
   if(Serial.available()>0) {
    char command = Serial.read();
    if(command == '1') {
    led = true;
    }else if(command == '0') {
      led = false;
    }
  }
  
  
}
  /*
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
*/
