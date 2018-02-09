/*This program calculates sum of triangle's edges' values and also
 *shows error message when user inputing negative value or wrong value
 *which means do not specify a triangle */
 

import javax.swing.JOptionPane; //Import java library to use JOptionPane class


class ComputePerimeterOfATriangle {
	
	
	public static void main(String [] args) {
	
	
	
		//Obtain values from user and convert its to double values
		String firstEdgeValue =	JOptionPane.showInputDialog (null, "Enter first edge of triangle's value: ",
		 "Input Box", JOptionPane.QUESTION_MESSAGE);
			double firstEdge = Double.parseDouble(firstEdgeValue);
		
	
		String secondEdgeValue = JOptionPane.showInputDialog (null, "Enter second edge of triangle's value: ",
		 "Input Box", JOptionPane.QUESTION_MESSAGE);
			double secondEdge = Double.parseDouble(secondEdgeValue);
		
	
		String thirdEdgeValue =	JOptionPane.showInputDialog (null, "Enter third edge of triangle's value: ",
		 "Input Box", JOptionPane.QUESTION_MESSAGE);
			double thirdEdge = Double.parseDouble(thirdEdgeValue);
			
	
	
		//Show error messsage when user input negative value or values
		if (firstEdge < 0 || secondEdge < 0 || thirdEdge < 0){
			JOptionPane.showMessageDialog (null, "THE VALUE OF EDGES MUST BE POSITIVE!",
			 "ERROR", JOptionPane.INFORMATION_MESSAGE);
			 
	
	
		//Values will be compared in mathematical theorem that is if sum of two edge less than
		//other edge or the difference between two edge in absolute value bigger than other edge,
		//those values cannot specify a triangle.
		} else if (firstEdge + secondEdge < thirdEdge || firstEdge - secondEdge > thirdEdge 
			|| secondEdge - firstEdge > thirdEdge){
				
				
				JOptionPane.showMessageDialog (null, "Those values cannot specify a triangle!",
				 "ERROR", JOptionPane.INFORMATION_MESSAGE);
				 
				 
		
			} else if (secondEdge + thirdEdge < firstEdge || secondEdge - thirdEdge > firstEdge 
				|| thirdEdge - secondEdge > firstEdge){
					
					
					JOptionPane.showMessageDialog (null, "Those values cannot specify a triangle!",
					 "ERROR", JOptionPane.INFORMATION_MESSAGE);
					 
					 
					
				} else if (thirdEdge + firstEdge < secondEdge || thirdEdge - firstEdge > secondEdge 
					|| firstEdge - thirdEdge > secondEdge){
						
					
						JOptionPane.showMessageDialog (null, "Those values cannot specify a triangle!",
						 "ERROR", JOptionPane.INFORMATION_MESSAGE);
						 
						 
					
					//If the values of edges are correct, calculate and show the perimeter of the triangle with JOptionPane
					} else {
						
						
						double perimeter = firstEdge + secondEdge + thirdEdge;
						
					
							JOptionPane.showMessageDialog (null, "Perimeter of the triangle: " + perimeter,
							 "RESULT", JOptionPane.INFORMATION_MESSAGE);
							 
					
		}		//End of the else
			
	}		//End of the main function

}		//End of the class