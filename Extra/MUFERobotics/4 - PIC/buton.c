#include <pic.h>
__CONFIG (LVPDIS & HS & WDTDIS & BORDIS);

#define _XTAL_FREQ 20000000
#define HIGH 1
#define LOW 0

void init(){
	ADCON1 = 0x07;

    TRISB = 0b11100000;
    PORTB = 0b00000000;

	TRISD = 0b00000000;
    PORTD = 0x00;

	TRISE = 0b000;
    PORTE = 0b000;
}

void main(){
	init();
	int i;
	while(1){
		if(RB7 == LOW){
			RD5 = HIGH;
		}else{
			RD5 = LOW;
		}
	}
}


