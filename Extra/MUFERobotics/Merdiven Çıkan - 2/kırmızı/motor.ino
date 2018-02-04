void setMotorSpeed(int pwm){
 /* motor1.setSpeed(pwm * 1000 / 386);
  motor2.setSpeed(pwm * 1000 / 401);
  motor3.setSpeed(pwm * 1000 / 386);
  motor4.setSpeed(pwm * 1000 / 330);*/

  motor1.setSpeed(pwm * 1000 / 386+30);
  motor2.setSpeed(pwm * 1000 / 411);
  motor3.setSpeed(pwm * 1000 / 396);
  motor4.setSpeed(pwm * 1000 / 330+30);
}

void setMotorSpeed_down(int pwm){
  motor1.setSpeed(pwm * 1000 / 386);
  motor2.setSpeed(pwm * 1000 / 411);
  motor3.setSpeed(pwm * 1000 / 396);
  motor4.setSpeed(pwm * 1000 / 330);
}
// İleri
// Motorların ikiside ileri yönde sürülür
void forward() {

  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

// Geri
// Motorların ikisi de geri yönde sürülür
void backward() {
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

// Sağ
// Motor1 ileri yönde, Motor2 geri yönde sürülür
void right() {
  int pwm = MOTOR_PWM_VALUE_ON + 40;
  
  motor1.setSpeed(pwm * 1000 / 386+30);
  motor2.setSpeed(pwm * 1000 / 411);
  motor3.setSpeed(pwm * 1000 / 360);
  motor4.setSpeed(pwm * 1000 / 330+30);

  
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
  setMotorSpeed(MOTOR_PWM_VALUE_ON);
}

// Sol
// Motor1 ileri geri, Motor2 ileri yönde sürülür
void left() {
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
}

// Motorları Durdur
// Not: Takılan güç kaynağına göre, motor shield bazen güç kaçırabilir. Böyle
// durumlarda, DC Motorlar çok yavaş şekilde hareket ederler.
void stopMotors() {

  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}
void absistem(){
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  delay(30);
}


void servoInc (Servo servo, int degree1 , int degree2 , int delaytime){
  for (int i = degree1; i < degree2; i++) {
   // Serial.println("servoInc baslangıç");
    servo.write(i);
    delay(delaytime);
  }
}
void servoDec (Servo servo, int degree1 , int degree2 , int delaytime){
  for (int i = degree1; i > degree2; i--) {
   // Serial.println("servoDec baslangıç");
    servo.write(i);
    delay(delaytime);
  }
}
void servoZero(){
  
  servo_2.write(0); 
  servo_1.write(0);
  
}

