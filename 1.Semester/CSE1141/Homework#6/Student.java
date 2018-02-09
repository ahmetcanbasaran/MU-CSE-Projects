/*This class is subclass of the Person class. It creates student object that has
 *gpa and borrowed book variable as well as name and birth date variables*/
class Student extends Person{
	
	//Define gpa variable and borrowed book object
	private double gpa;
	private Book borrowedBook;
	
	//Create no-arg. contructor with no-arg. constructor of the superclass
	public Student(){
		
		super();
		
	}
	
	//Create a student object with using constructor of super class and this method
	public Student(String name, java.util.Date birthDate, double gpa){
		
		super(name, birthDate);
		this.gpa = gpa;
		
	}
	
	//Create a method that returns the borrowed book object
	public Book getBorrowedBook(){
		
		return borrowedBook;
		
	}
	
	//Create a method which returns gpa of the student
	public double getGPA(){
		
		return gpa;
		
	}
	
	//Create a method that changes borrowed book object of the object
	public void setBorrowedBook(Book borrowedBook){
		
		this.borrowedBook = borrowedBook;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString (){
		
		return "Student: " + name + "\nBirth Date: " + birthDate + "\nGPA: " + gpa +
				"\nBorrowed book: " + borrowedBook + "\n";
		
	}
	
}
