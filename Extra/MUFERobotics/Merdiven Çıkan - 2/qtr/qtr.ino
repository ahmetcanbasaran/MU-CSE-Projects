//QTRs
int solQTR1 = 8;
int solQTR2 = 9;
int sagQTR1 = 10;
int sagQTR2 = 11;

//Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

//int pos = 0;    // variable to store the servo position

void setup() {

  pinMode(solQTR1, INPUT_PULLUP);
  pinMode(solQTR2, INPUT);

  pinMode(sagQTR1, INPUT);
  pinMode(sagQTR2, INPUT);

  //myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  Serial.begin(9600);

}

void loop() {

  if(!digitalRead(solQTR1)){

    Serial.println("SOL -1- Gordu");
 
  }

  if(!digitalRead(solQTR2)){

    Serial.println("SOL -2- Gordu");
 
  }

  if(!digitalRead(sagQTR1)){

    Serial.println("SAG -1- Gordu");
 
  }

  if(!digitalRead(sagQTR2)){

    Serial.println("SAG -2- Gordu");
 
  }


  /*if(digitalRead(solQTR2)){

    Serial.println("Sol QTR -2- gordu");
    
  }

  if(!digitalRead(sagQTR1)){

    Serial.println("Sag QTR -1- gordu");
    
  }


  if(!digitalRead(sagQTR2)){

    Serial.println("Sag QTR -2- gordu");
    
  }*/
    
}
