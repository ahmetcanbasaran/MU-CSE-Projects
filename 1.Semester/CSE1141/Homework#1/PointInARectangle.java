/* This program find the given point is in the rectangle which
 * is identfy before or not in the rectangle */


import javax.swing.JOptionPane; //Import JOptionPane' library to get input from user.


class PointInARectangle {
	
	
	public static void main(String[] args){
		
		

/*                ^
 *			      |
 *				  |
 *				  |
 *         |------|------|              Our triangle looks like this
 *         |	  |		 |              The center point (0,0)
 *<--------|------.------|--------->    Point A (5 , 2.5)   , Point B (-5 , 2.5)
 *		   |	  |		 |              Point C (-5 , -2.5) , Point D ( 5 , -2.5)
 *         |------|------|
 *				  |
 *				  |
 *				  |
 *				  |
 */
 
 
 	
 		//Create a JOptionPane to get input and convert that from string to double for x coordinate point
		String stringXAxesPoint = JOptionPane.showInputDialog(null, "Enter a point with X coordinate: ",
  		 "INPUT", JOptionPane.QUESTION_MESSAGE);
  		 
  		 
			Double xAxesPoint = Double.parseDouble (stringXAxesPoint);
  			 
  		 
  		
  		//Create a JOptionPane to get input and convert that from string to double for y coordinate point
  		String stringYAxesPoint = JOptionPane.showInputDialog(null, "Enter a point with Y coordinate: ",
  		 "INPUT", JOptionPane.QUESTION_MESSAGE);
  		 
  		 
  		 	Double yAxesPoint = Double.parseDouble (stringYAxesPoint);
  		 	
  		
  		
  		//Control the given point whether inside in the rectangle and show result
  		if (xAxesPoint > 10.0/2 || xAxesPoint < -10.0/2 || yAxesPoint > 5.0/2 || yAxesPoint < -5.0/2){
  			
  			
  			JOptionPane.showMessageDialog (null, "Point (" + xAxesPoint + ", " 
  				+ yAxesPoint + ") is not in the rectangle", "RESULT", JOptionPane.INFORMATION_MESSAGE);
  				
  		
  		//If it is not inside, show the result to user
  		} else {
  			
  			
  			JOptionPane.showMessageDialog (null, "Point (" + xAxesPoint + ", "
  				+ yAxesPoint + ") is in the rectangle", "RESULT", JOptionPane.INFORMATION_MESSAGE);
  				
  		
  		}		//End of the else

	}		//End of the main function		
	
}		//End of the class

