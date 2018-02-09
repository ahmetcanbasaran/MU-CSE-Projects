/*This class is subclass of the Person class. It creates Employee object that has
 *salary variable as well as name and birth date variables*/
class Employee extends Person {
	
	//Define salary variable
	protected double salary;
	
	//Create no-arg. contructor with no-arg. constructor of the superclass
	public Employee(){
	
		super();
	
	}
	
	//Create constructor with obtained variables with using argument constructor of the superclass
	public Employee(String name, java.util.Date birthDate){
		
		super(name, birthDate);
		
	}
	
	//Create a public method which turns the salary of the employee
	public double getSalary(){
		
		return salary;
		
	}
	
	//Create a public method which changes the salary of the employee
	public void setSalary(double salary){
		
		this.salary = salary;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString(){
		
		return "Employee: " + name + "\n" + "Birth Date: " + birthDate +
			 "\nSalary: " + salary + "\n";
		
	}
	
}	//End of the class
