
int ldr = A1;
unsigned long duration;

void setup ()
{
  
  Serial.begin(9600);
  pinMode(ldr, INPUT);  
}

void loop (){

  if (digitalRead(ldr) == LOW)
  
    duration = pulseIn (ldr, HIGH);

  else
  
    duration = pulseIn (ldr, LOW);
    
    
   duration /= 1000.000;
   
   Serial.println((int)duration);
   //delay(2000);
    


}
