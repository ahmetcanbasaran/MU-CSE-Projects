//This class creates a complex number then does some operation with it
public class ComplexNumber {
	
	//Define the complex number variables like private to avoid any changes from others
	private double re;
	private double im;
	
	
	//No-arg. constructor
	public ComplexNumber(){
	
	}
	
	
	//Create complex number with obtained parameters
	public ComplexNumber(double r, double i){
	
		re = r;
		im = i;
	
	}
	
	
	//Take real part of the complex number
	public double getReal(){
		
		return re;
		
	}
	
	
	//Take imaginary part of the complex number	
	public double getImaginary(){
		
		return im;
		
	}
	
	
	//Find reciprocal of the complex number with helps of denominator
	public ComplexNumber reciprocal(){
	
		double denominator = Math.pow(re, 2) + Math.pow(im, 2);
		
		double recReal = re/denominator;
		double recImaginary = (-1) * (im/denominator);
	
		return new ComplexNumber (recReal, recImaginary);
	
	}
	
	
	//Add the our complex number with obtained
	public ComplexNumber add (double addRe , double addIm){
		
		double aR = re + addRe;
		double aI = im + addIm;
		
		return new ComplexNumber (aR, aI);
		
	}
	
	
	//Subtract the our complex number with obtained
	public ComplexNumber subtract (double subRe , double subIm){
		
		double sR = re - subRe;
		double sI = im - subIm;
		
		return new ComplexNumber (sR, sI);
		
	}
	
	
	//Multiply the our complex number with obtained
	public ComplexNumber multiply (double mulRe, double mulIm){
		
		double mR = re*mulRe - im*mulIm;
		double mI = re*mulIm + mulRe * im;
		
		return new ComplexNumber (mR, mI);
		
	}
	
	
	//Divide the our complex number with obtained
	public ComplexNumber divide (double divRe, double divIm){
		
		double dR = 0;
		double dI = 0;
		
		//Avoid to do processes with zero
		if (divRe == 0 || divIm == 0)
			System.out.println("Real or imaginary part of complex numbers" +  
				" cannot divided by zero!");
		
		else{
			
			dR = (re * divIm - im * divRe) / (divRe*divRe + divIm * divIm);
			dI = (im * divRe + re * divIm) / (divRe*divRe + divIm * divIm);
			
		}
		
		return new ComplexNumber (dR, dI);
				
	}
	
	
	//Control whether complex numbers equal
	public boolean equals (double real1, double imag1){
		
		if (re == real1 && im == imag1)
			return true;
			
		else
			return false;	
		
	}
	
	
	//Change the sign of imaginary part of complex number, this means conjugate in math
	public ComplexNumber conjugate(){
		
		return new ComplexNumber (re, (-1)*im);
		
	}
	
	
	//Find the angle in radian with division of imaginary part  
	//with real part and turn it into degrees
	public double getAngle(){
		
		double angle = Math.toDegrees(Math.atan(im /re));
		
		if (re > 0 && im > 0)
			return angle;
		
		else if(re < 0 && im > 0)
			return angle + 90;
			
		else if(re < 0 && im < 0)
			return angle + 180;
						
		else			
			return angle + 270;
	}
	
	
	//Find magnitude of complex number with this formula below
	public double getMagnitude(){
		
		double hypotenuse = Math.sqrt( re*re + im*im);
		
		return hypotenuse;
		
	}
	
	
	//Convert to complex number into string in order to show this object
	public String toString(){
		
		return re + " + " + im + "i";
		
	}
	
}
