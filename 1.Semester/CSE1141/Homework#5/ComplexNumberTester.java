/*This program creates a complex number and does some kind of mathematical processes
 *which can seen below on it*/
class ComplexNumberTester {
	
	//Main method
	public static void main (String[] args){
		
		//Create a complex number with real and imaginary parts values
		ComplexNumber comNum = new ComplexNumber(3 , 4);
		ComplexNumber coNu1, coNu2, coNu3, coNu4, coNu5, coNu6, coNu7;
		
		//Display the created complex number with its values
		System.out.printf("%s\n\n" , comNum);
		
		
		//Display real and imaginary parts of the complex number
		System.out.printf ("Real part of the complex number is: %.1f\n\n" , comNum.getReal());
		System.out.printf ("Imaginary part of the complex number is: %.1fi\n\n" , comNum.getImaginary());
		
		
		//Invert number and display it
		coNu1 = comNum.reciprocal();
		System.out.printf ("After reciprocal; %s\n\n" , coNu1);
	
		
		//Add the another complex number and display it
		coNu2 = comNum.add(3 , 4);
		System.out.printf ("After addition with (3 + 4i), new complex number is: %.1f + %.1fi\n\n" , coNu2.getReal() , coNu2.getImaginary());
		
		
		//Substract the complex  number with another complex number
		coNu3 = comNum.subtract(5 , 7);
		System.out.printf ("After subtraction with (5 + 7i), new complex number is: %.1f + %.1fi\n\n" , coNu3.getReal() , coNu3.getImaginary());
		
		
		//Multiply the complex  number with another complex number
		coNu4 = comNum.multiply(7 , 11);
		System.out.printf ("After multiplication with (7 + 11i), new complex number is: %.1f + %.1fi\n\n" , coNu4.getReal() , coNu4.getImaginary());
		
		
		//Divide the complex  number with another complex number
		coNu5 = comNum.divide(3 , -4);
		System.out.printf ("After division with (3 - 4i), new complex number is: %.1f + %.1fi\n\n" , coNu5.getReal() , coNu5.getImaginary());
		
		
		//Control the equivalent of complex numbers and display its
		System.out.printf ("Does this complex number (4 - 7i) equal to the our complex number? -> %b\n\n" , comNum.equals(4 ,7));
		System.out.printf ("Does this complex number (3 + 4i) equal to the our complex number? -> %b\n\n" , comNum.equals(3 ,4));

		
		//Conjugate the complex number and display it on the screen
		coNu7 = comNum.conjugate();
		System.out.printf ("Conjugate complex number of the our complex number is: %.1f + %.1fi\n\n" , coNu7.getReal() , coNu7.getImaginary());
		
		
		//Display the angle of the complex number in degrees
		System.out.printf ("Angle of the complex number is: %.1f degrees\n\n" , comNum.getAngle());
		
		//Display the magnitude of the complex number on the screen
		System.out.printf ("Magnitude of the complex number is: %.1f\n\n" , comNum.getMagnitude());
		
	}
}
