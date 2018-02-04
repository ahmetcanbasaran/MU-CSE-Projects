#include <AFMotor.h>

#define TURNSPEED 80
#define TURNVALUE 22
#define TURNVALUE180 51

float rightAnalog = A0;
float leftAnalog = A2;
int alev=A1;

int front = 13;
float distance;
float PCONSTANT = 8;
float DCONSTANT = 8;

float error,preverror = 0;
float errordiff, control;
float sag, sol;
int fire;

int rightMotorSpeed = 100;
int leftMotorSpeed = 100;
int lastLeftSpeed,lastRightSpeed;
int nolt, nort;
int qtr = A5;

AF_DCMotor pervane(2);
AF_DCMotor motorSol(3);
AF_DCMotor motorSag(4);

void setup() {
 setup_encoder(9,10,A5,A4);  
 pinMode(rightAnalog,INPUT);
 pinMode(front,INPUT);
 pinMode(alev,INPUT);
 pinMode(qtr,INPUT);
 Serial.begin(9600);
 
}

void loop() {
  readSensors();
  //ileri(150,50);
 // Serial.println(analogRead(alev));
  //delay(200);
 //pervane_run(10);
  
Serial.println(digitalRead(front));
 readSensors();
  //ileri(150,150);
  nolt = get_ticks_M1();
  nort = get_ticks_M2(); 
 // printEncoder();

  //don180();
  //delaydur(2000);
  //Serial.println(digitalRead(qtr));
  
 
 if(digitalRead(front) == 1){
  moveStraight(rightMotorSpeed);
 //  printEncoder();
 // test();
  }
  else if(digitalRead(front) == 0){
    if(sag < 15){
       delaydur(500);
       sol90Don();
       delaydur(200);
    }
  /*  else if(sol < 15){
     // agresifDur(50,100);
      delaydur(500);
      sag90Don();
      delaydur(200);
    }
    else if(sag < 15 && sol < 15){
     //agresifDur(50,100);
     delaydur(500);
     don180();
     delaydur(200);
    }*/
  }
}
void blow(){
if(analogRead(alev) > 400 && analogRead(alev) < 800){
    pervane_run(100);

}
else{
 pervane_dur();
 }
}

void readSensors(){
  sag = readAnalog(rightAnalog);
  sol = readAnalog(leftAnalog);
 // fire = readAnalog(alev);
}

float readAnalog(float analog){
  distance = analogRead(analog);
  //distance = analogRead(rightAnalog);
  
  distance = 2076/(distance-11);
  if(distance<0){
    distance=30;
  }
  if(distance > 15){
    distance=15;
  }
  return distance;
}
void test(){
  Serial.print("Sol Analog: ");
  Serial.print(sol);
  Serial.print("Sag Analog: ");
  Serial.print(sag);
  Serial.print("  On Sensor: ");
  Serial.print(digitalRead(front));
  Serial.print("Sol/Left Motor: ");
  Serial.print(getMotorSpeeds(0));
  Serial.print("Sag/Right Motor: ");
  Serial.println(getMotorSpeeds(1));
}

void printEncoder(){
  int m1=get_ticks_M1();
  int m2=get_ticks_M2();
  Serial.print(m1);
  Serial.print("\t");
  Serial.println(m2);
}

int getVariables(int a){
  switch(a){
    case 0:
    
    return rightAnalog;
    break;
  }
}

