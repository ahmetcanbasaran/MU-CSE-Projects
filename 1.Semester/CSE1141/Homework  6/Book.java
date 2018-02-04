/*This class creates book object(s) with or without specifing pages variable
 *and author object of person(s). It has own toString method*/
class Book {
	
	//Define pages variable and author object
	protected Author author;
	protected int pages;
	
	//Create a no-arg. constructor
	public Book(){
	}
	
	//Create an object with obtained parameters
	public Book (Author author, int pages){
		
		this.author = author;
		this.pages = pages;
		
	}
	
	//Create a public method that returns author object of the class object
	public Author getAuthor(){
		
		return author;
		
	}
	
	//Create a method which returns pages variable of the object
	public int getPages(){
		
		return pages;
		
	}
	
	//Create a public method that allows to change the old author object with new one
	public void setAuthor(Author author){
		
		this.author = author;
		
	}
	
	//Create a public method that allows to change pages variable with new one
	public void setPages (int pages){
		
		this.pages = pages;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString (){
		
		return "Book: " + "\n\tAuthor: " + author + "\n\t" + pages + " pages\n";
		
	}
	
}
