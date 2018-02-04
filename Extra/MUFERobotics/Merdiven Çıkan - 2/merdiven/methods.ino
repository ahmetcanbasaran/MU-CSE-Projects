void wait(int myTime){

    digitalWrite(maviIn1, LOW);     digitalWrite(maviIn2, LOW);
    digitalWrite(morIn1, LOW);      digitalWrite(morIn2, LOW);  
    digitalWrite(onSagIn1, LOW);    digitalWrite(onSagIn2, LOW);  
    digitalWrite(onSolIn1, LOW);    digitalWrite(onSolIn2, LOW);
    digitalWrite(ortaSagIn1, LOW);    digitalWrite(ortaSagIn2, LOW);  
    digitalWrite(ortaSolIn1, LOW);    digitalWrite(ortaSolIn2, LOW);
    digitalWrite(arkaSagIn1, LOW);    digitalWrite(arkaSagIn2, LOW);  
    digitalWrite(arkaSolIn1, LOW);    digitalWrite(arkaSolIn2, LOW);

  if(myTime != 0){
    
    delay(myTime);

  }
    
}

void moveForward(int myTime){

  digitalWrite(onSolIn1, LOW);     digitalWrite(onSolIn2, HIGH);
  digitalWrite(ortaSagIn1, HIGH);     digitalWrite(ortaSagIn2, LOW);
  digitalWrite(ortaSolIn1, LOW);     digitalWrite(ortaSolIn2, HIGH);
  digitalWrite(arkaSagIn1, HIGH);     digitalWrite(arkaSagIn2, LOW);
  digitalWrite(arkaSolIn1, LOW);     digitalWrite(arkaSolIn2, HIGH);

  analogWrite(onSagEn, frontSpeed);     analogWrite(onSolEn, frontSpeed);
  analogWrite(ortaSagEn, middleSpeed);     analogWrite(ortaSolEn, middleSpeed);
  analogWrite(arkaSagEn, backSpeed);     analogWrite(arkaSolEn, backSpeed);

  if(myTime != 0){
    
    delay(myTime);

  }

}

void moveBackward(int myTime){

  digitalWrite(onSagIn1, HIGH);     digitalWrite(onSagIn2, LOW);      
  digitalWrite(onSolIn1, HIGH);     digitalWrite(onSolIn2, LOW);    
  digitalWrite(arkaSagIn1, HIGH);     digitalWrite(arkaSagIn2, LOW);      
  digitalWrite(arkaSolIn1, LOW);     digitalWrite(arkaSolIn2, HIGH);
      
//  analogWrite(onSagEn, wheelSpeed);     analogWrite(onSolEn, wheelSpeed);
//  analogWrite(arkaSagEn, wheelSpeed);     analogWrite(arkaSolEn, wheelSpeed);

  if(myTime != 0){
    
    delay(myTime);

  }

}

void climb(int myTime){
  
  digitalWrite(maviIn1, LOW);      digitalWrite(maviIn2, HIGH);     //Goes up
  digitalWrite(morIn1, HIGH);      digitalWrite(morIn2, LOW);     //Goes up

//  analogWrite(morEn, wheelSpeed);     analogWrite(maviEn, wheelSpeed);

  if(myTime != 0){
    
    delay(myTime);

  }
  
}

void fall(int myTime){

  digitalWrite(maviIn1, HIGH);      digitalWrite(maviIn2, LOW);     //Goes down
  digitalWrite(morIn1, LOW);      digitalWrite(morIn2, HIGH);     //Goes down  

//  analogWrite(morEn, wheelSpeed);     analogWrite(maviEn, wheelSpeed);

  if(myTime != 0){
    
    delay(myTime);

  }

}

void demoOne(){

  moveForward(3000);
  wait(1000);
  climb(2000);
  wait(1000);
  
  moveForward(200);
  wait(1000);
  fall(2000);
  wait(1000);
  
  moveForward(1000);
  climb(2000);
  moveForward(200);
  fall(2000);

  moveForward(1000);
  climb(2000);
  moveForward(200);
  fall(2000);
  
}

void turnLeft(){

  digitalWrite(onSagIn1, LOW);     digitalWrite(onSagIn2, HIGH);
  digitalWrite(onSolIn1, HIGH);     digitalWrite(onSolIn2, LOW);
  digitalWrite(ortaSagIn1, LOW);     digitalWrite(ortaSagIn2, HIGH);
  digitalWrite(ortaSolIn1, HIGH);     digitalWrite(ortaSolIn2, LOW);
  digitalWrite(arkaSagIn1, LOW);     digitalWrite(arkaSagIn2, HIGH);
  digitalWrite(arkaSolIn1, LOW);     digitalWrite(arkaSolIn2, HIGH);

  analogWrite(onSagEn, frontSpeed);     analogWrite(onSolEn, frontSpeed);
  analogWrite(ortaSagEn, middleSpeed);     analogWrite(ortaSolEn, middleSpeed);
  analogWrite(arkaSagEn, backSpeed);     analogWrite(arkaSolEn, backSpeed);

  delay(1000);
  
}

void turnRight(){

  digitalWrite(onSagIn1, HIGH);     digitalWrite(onSagIn2, LOW);
  digitalWrite(onSolIn1, LOW);     digitalWrite(onSolIn2, HIGH);
  digitalWrite(ortaSagIn1, HIGH);     digitalWrite(ortaSagIn2, LOW);
  digitalWrite(ortaSolIn1, LOW);     digitalWrite(ortaSolIn2, HIGH);
  digitalWrite(arkaSagIn1, LOW);     digitalWrite(arkaSagIn2, HIGH);
  digitalWrite(arkaSolIn1, HIGH);     digitalWrite(arkaSolIn2, LOW);

  analogWrite(onSagEn, 125);     
  analogWrite(onSolEn, 200);
  analogWrite(ortaSagEn, 125);     
  analogWrite(ortaSolEn, 200);
  analogWrite(arkaSagEn, 125);     
  analogWrite(arkaSolEn, 200);

  delay(2500);
  
}

void deneme(){

  digitalWrite(onSagIn1, LOW);     digitalWrite(onSagIn2, HIGH);
  digitalWrite(onSolIn1, LOW);     digitalWrite(onSolIn2, HIGH);
  digitalWrite(ortaSagIn1, LOW);     digitalWrite(ortaSagIn2, HIGH);
  digitalWrite(ortaSolIn1, LOW);     digitalWrite(ortaSolIn2, HIGH);
  digitalWrite(arkaSagIn1, HIGH);     digitalWrite(arkaSagIn2, LOW);  
  digitalWrite(arkaSolIn1, HIGH);     digitalWrite(arkaSolIn2, LOW);  
  
  analogWrite(onSagEn, 200);     analogWrite(onSolEn, 200);   //200dü
  analogWrite(ortaSagEn, 150);     analogWrite(ortaSolEn, 150);
  analogWrite(arkaSagEn, 150);     analogWrite(arkaSolEn, 150);

  delay(2000);

  digitalWrite(onSagIn1, LOW);     digitalWrite(onSagIn2, HIGH);
  digitalWrite(onSolIn1, LOW);     digitalWrite(onSolIn2, HIGH);
  digitalWrite(ortaSagIn1, LOW);     digitalWrite(ortaSagIn2, HIGH);
  digitalWrite(ortaSolIn1, LOW);     digitalWrite(ortaSolIn2, HIGH);
  digitalWrite(arkaSagIn1, HIGH);     digitalWrite(arkaSagIn2, LOW);
  digitalWrite(arkaSolIn1, HIGH);     digitalWrite(arkaSolIn2, LOW);  
  digitalWrite(maviIn1, LOW);      digitalWrite(maviIn2, HIGH);     //Goes up
  digitalWrite(morIn1, HIGH);      digitalWrite(morIn2, LOW);     //Goes up
  
  analogWrite(onSagEn, 200);     analogWrite(onSolEn, 200);   //200dü
  analogWrite(ortaSagEn, 150);     analogWrite(ortaSolEn, 150);
  analogWrite(arkaSagEn, 150);     analogWrite(arkaSolEn, 150);
  analogWrite(morEn, 235);     analogWrite(maviEn, 235);

  delay(1500);

  digitalWrite(onSagIn1, LOW);     digitalWrite(onSagIn2, HIGH);
  digitalWrite(onSolIn1, LOW);     digitalWrite(onSolIn2, HIGH);
  digitalWrite(ortaSagIn1, LOW);     digitalWrite(ortaSagIn2, HIGH);
  digitalWrite(ortaSolIn1, LOW);     digitalWrite(ortaSolIn2, HIGH);
  digitalWrite(arkaSagIn1, HIGH);     digitalWrite(arkaSagIn2, LOW);
  digitalWrite(arkaSolIn1, HIGH);     digitalWrite(arkaSolIn2, LOW);  
  digitalWrite(maviIn1, HIGH);      digitalWrite(maviIn2, LOW);     //Goes down
  digitalWrite(morIn1, LOW);      digitalWrite(morIn2, HIGH);     //Goes down
  
  analogWrite(onSagEn, 200);     analogWrite(onSolEn, 200);   //200dü
  analogWrite(ortaSagEn, 150);     analogWrite(ortaSolEn, 150);
  analogWrite(arkaSagEn, 150);     analogWrite(arkaSolEn, 150);
  analogWrite(morEn, 100);     analogWrite(maviEn, 100);

  delay(2500);
  
}
