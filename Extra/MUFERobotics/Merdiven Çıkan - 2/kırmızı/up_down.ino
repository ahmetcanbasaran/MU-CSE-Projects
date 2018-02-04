void up(){
  servoZero();
    while(1){
      forward();
      if(ultrasonic_on.ping_cm()<4 && ultrasonic_on.ping_cm() != 0){
        stopMotors();
        break;
      }
    }
    servo_2.write(15);
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
    for (int i = 15; i < 100 ; i++) {
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
  servoInc(servo_1,0, 100,20);
  for (int i = 100; i < 135 ; i++) {
    servo_1.write(i);
    delay(20);
    forward();
  }
  
  stopMotors();
  servoInc(servo_2,0, 20,20);
  //arkayı indir ve ilerle  
  for (int i = 20; i < 100 ; i++) {
    setMotorSpeed(MOTOR_PWM_VALUE_ON - 10);
    servo_2.write(i);
    delay(20);
    forward();
    if(ultrasonic_arka.ping_cm()<6){
      stopMotors();
    }
  }
  stopMotors();
  setMotorSpeed(MOTOR_PWM_VALUE_ON);
  for (int i = 135; i > 70 ; i--) {
    servo_1.write(i);
    delay(20);
    forward();
  }

  //ön servo 70, arka servo 100
  stopMotors();
  servoDec(servo_1,70, 0, 10);
  //forward();
  /*if(ultrasonic_on.ping_cm()<7 || ultrasonic_arka.ping_cm()>18){
      stopMotors();
    }*/
   /***** 
  for (int i = 100; i < 135 ; i++) {
    forward();
    servo_2.write(i);
    delay(15);
    
  }
  stopMotors();
  //servoInc(servo_2,100, 140);
 
  servoDec(servo_2,145, 0,10);
  
  //servoInc(servo_1,100, 140);

 /** while(1){
    forward();
    if(ultrasonic_arka.ping_cm()<10){
      stopMotors();
      break;
    }
  }*/
 
}
void down(){
  servoZero();
  setMotorSpeed_down(MOTOR_PWM_VALUE-5); 
  while(1){
    backward();
    if(readUltra()>9){
      stopMotors();
      break;
    }
  }  
  if(readUltra()>9){
    stopMotors();
    servoInc(servo_2,0,120 , 20);
    while(1){
      setMotorSpeed_down(MOTOR_PWM_VALUE+15);
      backward();
      if(readUltra()<18 && readUltra()>11){
        break;
      }
    }
    
    stopMotors();
    servoInc(servo_1,0,110,20);
    backward();

    for (int i=120; i>38; i--){
      setMotorSpeed_down(MOTOR_PWM_VALUE-10);
      backward();
      servo_2.write(i);
      delay(25);
    }
    
    setMotorSpeed_down(MOTOR_PWM_VALUE-5);
    //for(int i=0; stopMotors();
    //servoDec(servo_2,120,30);
    
    for (int i = 110; i > 61 ; i--) {
      setMotorSpeed_down(MOTOR_PWM_VALUE);
      backward();
      servo_1.write(i);
      delay(25);
     }
    stopMotors();
    servoDec(servo_1,62,0,20);
   /* while(readUltra()!=6){
      backward();
    }*/
    //servoDec(servo_1,110,0); üstteki for bunun yerine yazıldı
    stopMotors(); 
    //servoZero();
   // servoDec(servo_2,30,0);
    
  }

}

