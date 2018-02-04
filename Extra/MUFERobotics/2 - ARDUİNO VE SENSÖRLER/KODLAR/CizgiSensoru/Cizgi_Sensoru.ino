
void setup() {
  

	Serial.begin(9600);
  

	for( int sayi = 2 ; sayi <= 10 ; sayi++  ){
    
	
		pinMode(sayi, INPUT_PULLUP);	//Cizgi sensoru input olarak ayarlandi
  

	}
  
  


}



void loop() {
  

	for(int a = 2 ; a < 10 ; a++){ 	//2 den 9 a kadar dondu
   

		if( !digitalRead(a)){		// Hangi sensor gorduyse numarasını ekrana yaz
      

			Serial.print("Sensor ");
      
		
			Serial.print(a);
      
		
			Serial.println(" gordu");
      
		}
   
	}
 

}

