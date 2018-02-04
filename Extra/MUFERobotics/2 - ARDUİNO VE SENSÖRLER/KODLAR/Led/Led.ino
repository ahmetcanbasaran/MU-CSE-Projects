void setup() {
  pinMode(A0 , OUTPUT);	// analog olarak ayarla
}

void loop() {
  digitalWrite(A0 , HIGH );	//Ledi yak
  delay(250);
  digitalWrite(A0, LOW);		//Ledi sondur
  delay(250);
}

