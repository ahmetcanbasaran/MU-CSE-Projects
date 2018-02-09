/*This class is subclass of the Person class. It creates student object 
 *that has name and birth date variables from the superclass*/
class Author extends Person{
	
	//Define a manager object of the person class
	private Person manager = new Person();
	
	//Create no-arg. contructor with no-arg. constructor of the superclass 
	public Author(){
		
		super();
		
	}
	
	//Define constructor with obtained variables with using argument constructor of the superclass
	public Author (String name, java.util.Date birthDate){
		
		super (name, birthDate);
		
	}
	
	//Create a method that returns manager object of the author object
	public Person getManager (){
		
		return manager;
		
	}
	
	//Create a method which changes the manager object of the object
	public void setManager(Person manager){
		
		this.manager = manager;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString (){
		
		return "Author: " + name + "\nBirth Date: " + birthDate +
				"\nManager: " + getManager();
		
	}
	
}
