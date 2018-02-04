#include <pic.h>
__CONFIG (LVPDIS & HS & WDTDIS & BORDIS);

#define _XTAL_FREQ 20000000


void init(){
	ADCON1 = 0x07;
	
	TRISD = 0b00000000;
    PORTD = 0x00;
}


void main(){
	init();
		
	int i;
	while(1){
		RD5 = 1;
		for(i =0 ; i<5 ; i++){
		__delay_ms(200);
		}

		RD5 = 0;
		for(i =0 ; i<5 ; i++){
		__delay_ms(200);
		}
	}
}


