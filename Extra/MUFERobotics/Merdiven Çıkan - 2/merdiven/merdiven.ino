int maviEn = 4;
int maviIn1 = 49;
int maviIn2 = 48;
int morIn1 = 47;
int morIn2 = 46;
int morEn = 5;

int onSagEn = 2;
int onSagIn1 = 53;
int onSagIn2 = 52; 
int onSolIn1 = 51;
int onSolIn2 = 50;
int onSolEn = 3;

int arkaSagEn = 6;
int arkaSagIn1 = 45;
int arkaSagIn2 = 44; 
int arkaSolIn1 = 43;
int arkaSolIn2 = 42;
int arkaSolEn = 7;

int ortaSagEn = 8;
int ortaSagIn1 = 41;
int ortaSagIn2 = 40; 
int ortaSolIn1 = 39;
int ortaSolIn2 = 38;
int ortaSolEn = 9;

int pinionSpeed = 255;

//int frontSpeed = 150;
//int middleSpeed = 125;
//int backSpeed = 100;

int frontSpeed = 230;
int middleSpeed = 125;
int backSpeed = 100;

void setup() {
  
  // set all the motor control pins to outputs
  pinMode(maviEn, OUTPUT);      pinMode(maviIn1, OUTPUT);     pinMode(maviIn2, OUTPUT);     
  pinMode(morIn1, OUTPUT);      pinMode(morIn2, OUTPUT);      pinMode(morEn, OUTPUT);
  
  pinMode(onSagEn, OUTPUT);     pinMode(onSagIn1, OUTPUT);      pinMode(onSagIn2, OUTPUT);
  pinMode(onSolIn1, OUTPUT);      pinMode(onSolIn2, OUTPUT);      pinMode(onSolEn, OUTPUT);
  pinMode(ortaSagEn, OUTPUT);     pinMode(ortaSagIn1, OUTPUT);      pinMode(ortaSagIn2, OUTPUT);
  pinMode(ortaSolIn1, OUTPUT);      pinMode(ortaSolIn2, OUTPUT);      pinMode(ortaSolEn, OUTPUT);
  pinMode(arkaSagEn, OUTPUT);     pinMode(arkaSagIn1, OUTPUT);      pinMode(arkaSagIn2, OUTPUT);
  pinMode(arkaSolIn1, OUTPUT);      pinMode(arkaSolIn2, OUTPUT);      pinMode(arkaSolEn, OUTPUT);

  //Setup all motors off
  digitalWrite(maviIn1, LOW);     digitalWrite(maviIn2, LOW);
  digitalWrite(morIn1, LOW);      digitalWrite(morIn2, LOW);
  digitalWrite(onSagIn1, LOW);    digitalWrite(onSagIn2, LOW);  
  digitalWrite(onSolIn1, LOW);    digitalWrite(onSolIn2, LOW);
  digitalWrite(ortaSagIn1, LOW);    digitalWrite(ortaSagIn2, LOW);    
  digitalWrite(ortaSolIn1, LOW);    digitalWrite(ortaSolIn2, LOW);
  digitalWrite(arkaSagIn1, LOW);    digitalWrite(arkaSagIn2, LOW);    
  digitalWrite(arkaSolIn1, LOW);    digitalWrite(arkaSolIn2, LOW);

  analogWrite(onSagEn, frontSpeed);     analogWrite(onSolEn, frontSpeed);
  analogWrite(ortaSagEn, middleSpeed);     analogWrite(ortaSolEn, middleSpeed);
  analogWrite(arkaSagEn, backSpeed);     analogWrite(arkaSolEn, backSpeed); 
   
  Serial.begin(9600);

}

void loop(){

  int i = 0;

  for(i = 0; i < 4; i++){
    
    deneme();

    wait(3000);
        
  }

  wait(3000);

  digitalWrite(onSagIn1, LOW);     digitalWrite(onSagIn2, HIGH);
  digitalWrite(onSolIn1, LOW);     digitalWrite(onSolIn2, HIGH);
  digitalWrite(ortaSagIn1, LOW);     digitalWrite(ortaSagIn2, HIGH);
  digitalWrite(ortaSolIn1, LOW);     digitalWrite(ortaSolIn2, HIGH);
  digitalWrite(arkaSagIn1, HIGH);     digitalWrite(arkaSagIn2, LOW);
  digitalWrite(arkaSolIn1, HIGH);     digitalWrite(arkaSolIn2, LOW);  
  
  analogWrite(onSagEn, 100);     analogWrite(onSolEn, 100);
  analogWrite(ortaSagEn, 100);     analogWrite(ortaSolEn, 100);
  analogWrite(arkaSagEn, 100);     analogWrite(arkaSolEn, 100);

  delay(100);

  wait(3000);

  turnRight();

  wait(3000);

  for(i = 0; i < 3; i++){
    
    deneme();
        
  }
  
  wait(10000);

}
