/*This class creates person object(s) with or without specifing name and birth date
 *of person(s). It has own toString method*/
class Person {
	
	//Define protected String and Date variables
	protected String name;
	protected java.util.Date birthDate;
	
	//Create no-arg. constructor
	public Person(){
	}
	
	//Create an object with obtained parameters
	public Person(String name, java.util.Date birthDate){
		
		this.name = name;
		this.birthDate = birthDate;		
		
	}
	
	//Create a public method that returns name of person object
	public String getName(){
		
		return name;
		
	}
	
	//Create a public method that returns birth date of person object
	public java.util.Date getBirthDate(){
		
		return birthDate;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString(){
		
		return "Person: " + name + "\nBirth date: " + birthDate + "\n";
		
	}	
	
}	//End of class
