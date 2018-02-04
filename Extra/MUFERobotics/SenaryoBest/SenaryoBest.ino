#include <QTRSensors.h>

int motorADir = 3; //left motor direction
int motorAPwm = 5; //left motor pwm
int motorBDir = 6; //right motor direction
int motorBPwm = 9; //right motor pwm

int right1 = A0; //8
int right2 = A1; //7
int right3 = A2; //6
int right4 = A3; //5
int right5 = A4; //4
int right6 = A5; //3
int right7 = 7;  //2
int right8 = 8;  //1   
                                                              
int qtr1,qtr2,qtr3,qtr4,qtr5,qtr6,qtr7,qtr8; //qtr values (qtr1 is the rightest one)

int xQtr1,xQtr2,xQtr3,xQtr4,xQtr5,xQtr6,xQtr7,xQtr8; //sensors' coefficients

int errorQtr; //sum of sensors' coefficients

int initialSpeed=90;

void setup() {
  //motor pins
  pinMode(motorADir, OUTPUT);
  pinMode(motorAPwm, OUTPUT);
  pinMode(motorBDir, OUTPUT);
  pinMode(motorBPwm, OUTPUT);
  
  //qtr pins
  pinMode(right1,INPUT_PULLUP);
  pinMode(right2,INPUT_PULLUP);
  pinMode(right3,INPUT_PULLUP);
  pinMode(right4,INPUT_PULLUP);
  pinMode(right5,INPUT_PULLUP);
  pinMode(right6,INPUT_PULLUP);
  pinMode(right7,INPUT_PULLUP);
  pinMode(right8,INPUT_PULLUP);

  //motor initial speeds and directions
  digitalWrite(motorADir, HIGH);
  analogWrite(motorAPwm, initialSpeed);
  digitalWrite(motorBDir, HIGH);
  analogWrite(motorBPwm,initialSpeed);
  
  Serial.begin(9600);
}

void loop() {

  readQtr();
  debug(); //prints QTR values
  PID(); //Following Line
  
}
void readQtr(){
  qtr1=!digitalRead(right1);
  qtr2=!digitalRead(right2);
  qtr3=!digitalRead(right3);
  qtr4=!digitalRead(right4);
  qtr5=!digitalRead(right5);
  qtr6=!digitalRead(right6);
  qtr7=!digitalRead(right7);
  qtr8=!digitalRead(right8);
}

void debug(){
  Serial.print(qtr1);
  Serial.print(" ");
  Serial.print(qtr2);
  Serial.print(" ");
  Serial.print(qtr3);
  Serial.print(" ");
  Serial.print(qtr4);
  Serial.print(" ");
  Serial.print(qtr5);
  Serial.print(" ");
  Serial.print(qtr6);
  Serial.print(" ");
  Serial.print(qtr7);
  Serial.print(" ");
  Serial.print(qtr8);
  Serial.println(" ");
}

void errorQTR(){

  //coefficients of sensors
  xQtr1=qtr1*4;
  xQtr2=qtr2*3;
  xQtr3=qtr3*2;
  xQtr4=qtr4*1;
  xQtr5=qtr5*-1;
  xQtr6=qtr6*-2;
  xQtr7=qtr7*-3;
  xQtr8=qtr8*-4;
  
  errorQtr=xQtr1+xQtr2+xQtr3+xQtr4+xQtr5+xQtr6+xQtr7+xQtr8;
  //Serial.println(error);
}

void PID(){
  
  errorQTR();
  
  //Following Line
  digitalWrite(motorADir,HIGH);
  digitalWrite(motorBDir,HIGH);
  analogWrite(motorAPwm,initialSpeed-errorQtr*10);
  analogWrite(motorBPwm,initialSpeed+errorQtr*10);
  
  //Checking L-shaped turn for right
  if(errorQtr>7){ // QTR---> 0 0 0 1 1 1 1 1 or 0 0 0 0 1 1 1 1 or 0 0 0 0 0 1 1 1
    turnRight();
  }
  
  //Checking L-shaped turn for left
  if(errorQtr<-7){ // QTR--> 1 1 1 1 1 0 0 0 or 1 1 1 1 0 0 0 0 or 1 1 1 0 0 0 0 0
    turnLeft();
  }
  
}

void turnRight(){
  
  //L-shaped turn
   while(true){
    readQtr();
      digitalWrite(motorBDir,LOW);
      analogWrite(motorAPwm,initialSpeed+errorQtr*10);
      analogWrite(motorBPwm,initialSpeed-errorQtr*10);

      Serial.println("First Half");
      if(qtr4==0){
        break;
      }
      
   }
   
   Serial.println("Half Time Break!!");
    
   while(true){
    readQtr();
      digitalWrite(motorBDir,LOW);
      analogWrite(motorAPwm,initialSpeed+errorQtr*10);
      analogWrite(motorBPwm,initialSpeed-errorQtr*10);    

      Serial.println("Second Half"); 
      if(qtr4==1||qtr5==1){
        break;
      }
   }
      
    analogWrite(motorAPwm, initialSpeed);
    analogWrite(motorBPwm, initialSpeed);
 
}

void turnLeft(){
  
    //L-shaped turn 
    while(true){
      readQtr();
      Serial.println("First Half of Turning Left");
      digitalWrite(motorADir,LOW);
      analogWrite(motorAPwm,initialSpeed+errorQtr*10);
      analogWrite(motorBPwm,initialSpeed-errorQtr*10);
      if(qtr5==0){
        break;
      }
    }

    Serial.println("Half Time Break!!");
    
    while(true){
      readQtr();
      Serial.println("Second Half of Turning Left");
      digitalWrite(motorADir,LOW);
      analogWrite(motorAPwm,initialSpeed+errorQtr*10);
      analogWrite(motorBPwm,initialSpeed-errorQtr*10);
      if(qtr4==1||qtr5==1){
        break;
      }
    }
      
    analogWrite(motorAPwm, initialSpeed);
    analogWrite(motorBPwm, initialSpeed);
        
}

void stopMotors(){
    analogWrite(motorAPwm, 255);
    analogWrite(motorBPwm, 255);
}
  


