
//Define Pins
int Sag = A0;
int Sol = A2;
int disR, disL;

int PwmLeft = 3;
int PwmRight = 11;
int DirLeft = 12;
int DirRight = 13;

//QTR pins
int q2 = digitalRead(A1);
int q3 = digitalRead(7);
int q4 = digitalRead(6);
int q5 = digitalRead(5);
int q6 = digitalRead(4);
int q7 = digitalRead(2);

//Define variables

int left, right;
int leftNormal = 180;
int rightNormal = 180;

void setup() {
  
  pinMode(PwmLeft, OUTPUT);
  pinMode(PwmRight, OUTPUT);
  pinMode(DirLeft, OUTPUT);
  pinMode(DirRight, OUTPUT);

  // Initialize all pins as low:
  digitalWrite(PwmLeft, LOW);
  digitalWrite(PwmRight, LOW);
  digitalWrite(DirLeft, LOW);
  digitalWrite(DirRight, LOW);
  
  //QTR pins
  pinMode(2, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(A1, INPUT_PULLUP);
 
  Serial.begin(9600);
  
}

void loop() {
  /*
  Serial.print(digitalRead(A1));
  Serial.print(digitalRead(7));
  Serial.print(digitalRead(6));
  Serial.print(digitalRead(5));
  Serial.print(digitalRead(4));
  Serial.println(digitalRead(2));
  */
  
  readQTR();
  
    if(q2 == 1 && q3 == 1 && q4 == 0 && q5 == 0 && q6 == 1 && q7 == 1){
      forward(leftNormal, rightNormal);
    }
    
    else if(q2 == 1 && q3 == 0 && q4 == 0 && q5 == 1 && q6 == 1 && q7 == 1){
      forward(200, 160);
    }


    else if(q2 == 0 && q3 == 0 && q4 == 1 && q5 == 1 && q6 == 1 && q7 == 1){
      forward(220, 140);
    }


    else if(q2 == 1 && q3 == 1 && q4 == 1 && q5 == 0 && q6 == 0 && q7 == 1){
      forward(160, 200);
    }


    else if(q2 == 1 && q3 == 1 && q4 == 1 && q5 == 1 && q6 == 0 && q7 == 0){
      forward(140, 220);
    }  
}

/********************** MOTOR TURNS ***************************************/
void forward(int left, int right){
  //ileri için 1, Geri içn 0
  digitalWrite(DirRight, 1);
   digitalWrite(DirLeft, 1);
  analogWrite(PwmRight, right);
  analogWrite(PwmLeft, left);
  
}

void backward(int left, int right){
  //ileri için 1, Geri içn 0
  digitalWrite(DirRight, 0);
   digitalWrite(DirLeft, 0);
  analogWrite(PwmRight, right);
  analogWrite(PwmLeft, left);
  
}

void turnleft(int left, int right){
  //ileri için 1, Geri içn 0
  digitalWrite(DirRight, 0);
   digitalWrite(DirLeft, 1);
  analogWrite(PwmRight, right);
  analogWrite(PwmLeft, left);
  
}

void turnright(int left, int right){
  //ileri için 1, Geri içn 0
  digitalWrite(DirRight, 1);
   digitalWrite(DirLeft, 0);
  analogWrite(PwmRight, right);
  analogWrite(PwmLeft, left);
  
}

/********************** QTR ***************************************/
void readQTR(){
  q2 = digitalRead(A1);
  q3 = digitalRead(7);
  q4 = digitalRead(6);
  q5 = digitalRead(5);
  q6 = digitalRead(4);
  q7 = digitalRead(2);
}

