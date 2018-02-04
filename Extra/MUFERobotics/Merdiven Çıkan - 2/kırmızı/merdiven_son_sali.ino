#include <digitalWriteFast.h>

#include <NewPing.h>
#include <AFMotor.h>
#include <Servo.h>

#define echoPin A3
#define trigPin A2
#define echoPin_arka A5
#define trigPin_arka A4
#define SERVO1_PWM 10
#define SERVO2_PWM 9
#define MAXDISTANCE 500
#define MOTOR_PWM_VALUE 27  // Öntanımlı Motor PWM Değeri: 33
#define MOTOR_PWM_VALUE_ON 35


//m1=m3=3.86 
//m2=4.01
//m4=3.30
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

Servo servo_1;
Servo servo_2;

NewPing ultrasonic_on(trigPin,echoPin,MAXDISTANCE);
NewPing ultrasonic_arka(trigPin_arka,echoPin_arka,MAXDISTANCE);

int count ;


void setup() {
  // Motorlara başlangıçta tanımladığımız MOTOR_PWM_VALUE değerini atadık.
  setMotorSpeed(MOTOR_PWM_VALUE_ON);
  //setMotorSpeed_down(MOTOR_PWM_VALUE);
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  pinMode(trigPin_arka, OUTPUT);
  pinMode(echoPin_arka, INPUT);
  
  servo_1.attach(SERVO1_PWM);
  servo_2.attach(SERVO2_PWM);
  
  servoZero();  
  count = 0;
}
