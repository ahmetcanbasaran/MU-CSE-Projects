#include <AFMotor.h>



AF_DCMotor motor(4);


AF_DCMotor motor2(2);




void setup() {
  

Serial.begin(9600);	//Serial ekranı hızını ayarla 
  
  

motor.setSpeed(200); 	// baslangic hızı belirle.
 
  

motor.run(RELEASE);	// motoru baslangıcta durdur.


}




void loop() {
 
 
uint8_t i;
  
 
 
Serial.print("Ileri Yonde Dongu");
  
  

motor.run(FORWARD);		//ileri yonu belirle
  
  

for (i=0; i<255; i++) {		//hizlan
    

	motor.setSpeed(i);  
    

	delay(10);
 

}
    

for (i=255; i!=0; i--) {	//yavasla
    

	motor.setSpeed(i);  
    

	delay(10);
 

}
  
  

	Serial.print("Geri Yonde Dongu");

  

	motor.run(BACKWARD);	//geri yonu belirle

  

for (i=0; i<255; i++) {		

	//hızlan
    

	motor.setSpeed(i);  
    

	delay(10);
 
} 
  

for (i=255; i!=0; i--) {		

	//yavasla
    

	motor.setSpeed(i);  
    

	delay(10);
 

}

  

motor.run(RELEASE);	// Motoru durdur
  

delay(1000);


}
