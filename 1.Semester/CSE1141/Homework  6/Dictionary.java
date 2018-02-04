/*This class is subclass of the Book class. It creates Dictionary object(s) 
 *that has definition variable as well as pages variable*/
class Dictionary extends Book {
	
	//Define definitin variable
	private int defs;
	
	//Create a no-arg. contructor with using no-arg. constructor of super class
	public Dictionary(){
		
		super();
		
	}
	
	//Define constructor with obtained variables with helps of the argument constructor of the superclass
	public Dictionary(Author author, int pages, int defs){
		
		super(author, pages);
		this.defs = defs;		
		
	}
	
	//cerate a method that returns  definitions variable
	public int getDefs(){
		
		return defs;
		
	}
	
	//Create am method that can change the definitions variable with obtained one
	public void setDefs(){
		
		this.defs = defs;
		
	}
	
	//Create a public method in order to print the object with its specified variables
	public String toString (){
		
		return "Dictionary : " + "\nAuthor: " + author.getName() + "\n" +
				 pages + " pages\n" + defs + " definitions";
		
	}
	
}
