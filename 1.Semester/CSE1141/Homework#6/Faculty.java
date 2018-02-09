/*This class is subclass of the both Person and Employee classes. It creates faculty
 *object that has title variable as well as name, birth date and salary variables*/
class Faculty extends Employee {
	
	//Define title variable
	private String title;
	
	//Create no-arg. contructor with no-arg. constructor of the superclass
	public Faculty (){
		
		super();
		
	}
	
	//Define constructor with obtained variables with using argument constructor of the superclass
	public Faculty(String name, java.util.Date birthDate){
		
		super(name, birthDate);
		
	}
	
	//Create a method that returns the title of the object
	public String getTitle(){
		
		return title;
		
	}
	
	//Create a method which changes the title of the objects
	public void setTitle(String title){
		
		this.title = title;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString(){
		
		return "Faculty: " + title + ". " + name + "\n\t" + "Birth Date: " +
				 birthDate + "\n\tSalary: " + salary  + "\n";
		
	}
	
}
