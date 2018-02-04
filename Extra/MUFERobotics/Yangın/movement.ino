
void moveStraight(int rightMotorSpeed){
  
  if(sag < 11){
    error = 10-sag;
    errordiff = error-preverror;
    control = PCONSTANT*error+DCONSTANT*errordiff;
   /* Serial.print("adfsd");
    Serial.println(control);*/
  }
  else{
    error = 10-sag;
    errordiff = error-preverror;
    control = (PCONSTANT/3.4)*error+(DCONSTANT/3.4)*errordiff;
    /*Serial.print("buyuk");
    Serial.println(control);*/
  }
  

lastLeftSpeed = rightMotorSpeed - control;
lastRightSpeed = rightMotorSpeed + control;


ileri(lastLeftSpeed,lastRightSpeed);
//rightMotorSpeed = lastRightSpeed;
//leftMotorSpeed = lastLeftSpeed;
preverror = error;

}

void pervane_run(int turn){
 pervane.run(FORWARD);
 pervane.setSpeed(turn);
}
void pervane_dur(){
 pervane.run(RELEASE);
}
void ileri(int sol,int sag){
 motorSol.run(FORWARD);
 motorSag.run(FORWARD);
}
void dur(){
  motorSol.run(RELEASE);
  motorSag.run(RELEASE);
}
void delaydur(int d){
  motorSol.setSpeed(RELEASE);
  motorSag.setSpeed(RELEASE);
  delay(d);
}
int getMotorSpeeds(int i){
  switch(i){
    case 0:
    return lastLeftSpeed;
    case 1:
    return lastRightSpeed;
  }
}

void sol90Don(){
  clear_ticks();
  motorSol.setSpeed(TURNSPEED);
  motorSag.setSpeed(TURNSPEED);
  while(1){
    soltamdon();
  // printEncoder();
    if(get_ticks_M1() < -TURNVALUE || get_ticks_M2() > TURNVALUE){
      break;
    }
  }
  clear_ticks();
}


void sag90Don(){
 clear_ticks();
  motorSol.setSpeed(TURNSPEED);
  motorSag.setSpeed(TURNSPEED); 
  while(1){
    sagtamdon();
  //  printEncoder();
    if(get_ticks_M1() > TURNVALUE || get_ticks_M2() < -TURNVALUE){
      break;
    }
  }
  clear_ticks();
}

void don180(){
  clear_ticks();
  motorSol.setSpeed(TURNSPEED);
  motorSag.setSpeed(TURNSPEED);

  while(1){
    sagtamdon();
    //printEncoder();
    if(get_ticks_M2() < -TURNVALUE180 || get_ticks_M1() > TURNVALUE180){
      break;
    }
  } 
  clear_ticks();
}

void sagtamdon(){
  motorSol.run(FORWARD);
  motorSag.run(BACKWARD);
  motorSol.setSpeed(TURNSPEED);
  motorSag.setSpeed(TURNSPEED);
}
void soltamdon(){
  motorSol.run(BACKWARD);
  motorSag.run(FORWARD);
}

