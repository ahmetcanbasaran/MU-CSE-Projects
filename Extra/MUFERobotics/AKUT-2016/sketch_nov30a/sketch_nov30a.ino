int ldr = A1;
unsigned long duration;

void setup(){
  Serial.begin(9600);
  pinMode(ldr, INPUT);
}

void loop(){
 /* 
 if(digitalRead(ldr) == HIGH){
    duration = pulseIn(ldr, LOW);//pulseIn(pin, value), pulseIn(pin, value, timeout) 
 } else{
    duration = pulseIn(ldr, HIGH);
 }
  Serial.println( duration );
  delay(2000);*/
  Serial.println("gh");
}

int freq(){//ldr frekansı
  if(digitalRead(ldr) == HIGH){
    duration = pulseIn(ldr, LOW,10000000);
 } else{
    duration = pulseIn(ldr, HIGH,10000000);
  }

   duration = duration / 1000.000;
   if(duration < 6)
     return freq();
   else
    return (int)duration;
}


