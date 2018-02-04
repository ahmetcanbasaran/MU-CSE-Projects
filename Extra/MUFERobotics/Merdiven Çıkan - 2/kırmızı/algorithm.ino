void loop(){
 //up();
// Serial.println(ultrasonic_arka.ping_cm()); 
 //Serial.println("dfgdgdfgdsg");
 
 //down(); 

/*
  for(int i=0; i<10; i++){
    forward();
    delay(100);
    right();
    delay(500);
    backward();
    delay(50);    
  }

    stopMotors();
    delay(1000);
    */
 algorithm();
/*
      right();
      if(ultrasonic_on.ping_cm() < 5 && ultrasonic_arka.ping_cm() < 10){
        stopMotors();
        delay(1100);   // Serial.println(ultrasonic_arka.ping_cm());
    //Serial.println(ultrasonic_on.ping_cm());
      }
  
  /* while(1){
      right();
      if(ultrasonic_on.ping_cm() < 7){
         
         break;
         
      }
   }
   stopMotors();*/
}
void algorithm(){
  if(count < 3 || (count > 4 && count <7)){
    up();   
  }else if(count == 3){
    up();
    /*
    servoZero();
    while(1){
      forward();
      if(ultrasonic_on.ping_cm()<4 && ultrasonic_on.ping_cm() != 0){
        stopMotors();
        break;
      }
    }
    
    //öndeki servo 128 derece indi
    servoInc(servo_1,0, 100, 20);
    for (int i = 100; i < 135 ; i++) {
      servo_1.write(i);
      delay(25);
      forward();
    }
    absistem();
    stopMotors();
    
    //arkayı indir ve ilerle  
    for (int i = 0; i < 100 ; i++) {
      servo_2.write(i);
      delay(25);
      forward();
      if(ultrasonic_arka.ping_cm()<6){
        stopMotors();
      }
    }
    stopMotors();
    
    for (int i = 135; i > 70 ; i--) {
      servo_1.write(i);
      delay(25);
      forward();
    }
  
    //ön servo 70, arka servo 100
    stopMotors();
    servoDec(servo_1,70, 0,20);
    for (int i = 100; i < 145 ; i++) {
      forward();
      servo_2.write(i);
      delay(25);
      
    }
    stopMotors(); 
    servoDec(servo_2,150, 0,20);
    
    */
  }
  else if(count == 4){
    for(int i=1; i<7; i++){
      forward();
      delay(100);
      right();
      delay(500);
      backward();
      delay(50);   
    }
    forward();
   /* while(1){
      right();
      if(ultrasonic_on.ping_cm() < 7 && ultrasonic_arka.ping_cm() < 10){
         break;
      }
    }*/
    up(); 
  }else if(count == 7 ){
    stopMotors();
    delay(2000);
    down();
  }else if((count > 7 && count < 10) || count > 10){
    down();
  }else if(count == 10){
    for(int i=1; i<9; i++){
      backward();
      delay(100);
      left();
      delay(500);
      forward();
      delay(50);   
    }
    backward();
    down();
  }
  
    count = count + 1; 
}




double readUltra() {
  long duration, distance;
  digitalWriteFast(trigPin_arka, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWriteFast(trigPin_arka, HIGH);
  delayMicroseconds(10); // Added this line
  digitalWriteFast(trigPin_arka, LOW);
  duration = pulseIn(echoPin_arka, HIGH);
  distance = (duration/2) / 29.1;
  
  delay(30);
  if (distance >= 200 || distance <= 0){
    return 99;
  }
  else {
   return distance;
  }
  
}



