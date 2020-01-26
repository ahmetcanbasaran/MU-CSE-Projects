#include<Servo.h>

Servo motor; //motor adında bir servo nesnesi oluşturduk.
int LDR_Pin = A0; //analog pin 0
int motor_pin = 3;
int angle;

void setup(){
  motor.attach(motor_pin);
}

void loop(){
  int LDRReading = analogRead(LDR_Pin);
  if(LDRReading >= 800 && LDRReading < 1024)
    LDRReading = 1023;
  else if(LDRReading >= 600 && LDRReading < 800)
    LDRReading = 750;
  else if(LDRReading >= 400 && LDRReading < 600)
    LDRReading = 550;
  else if(LDRReading >= 200 && LDRReading < 400)
    LDRReading = 350;
  else if(LDRReading >= 100 && LDRReading < 200)
    LDRReading = 200;
  else if(LDRReading < 100)
    LDRReading = 0;
  // scaling the potentiometer value to angle value for servo between 0 and 180)
  angle = map(LDRReading, 0, 600, 0, 179);     
  motor.write(200-angle);  //command to rotate the servo to the specified angle 
  delay(100);
}
