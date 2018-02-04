/*This class generates students with helping PersonalData(subclass)*/

class Student {
	
	//Define variable private in order to avoid accessing without authorized
	private String name;
	
	private long id;
	
	private double gpa;
	
	private PersonalData pd = new PersonalData();
	
	//No-arg. constructor
	public Student(){
	}
	
	//That constructor contains all of variables
	public Student (String name, long id, double gpa, PersonalData pd){
		
		this.name = name;
		this.id = id;
		this.gpa = gpa;
		this.pd = pd;
		
	}
	
	//Returns name
	public String getName(){
		
		return name;
		
	}
	
	//Returns ID
	public long getID(){
		
		return id;
		
	}
	
	//Returns GPA
	public double getGPA(){
		
		return gpa;
		
	}
	
	//Returns peronal data
	public PersonalData getPersonalData(){
		
		return pd;
		
	}
	
	//Display the object with its variables 
	public String toString(){
		
		String express = "\t" + name + "\n\t\t\tID: " + id + "\n\t\t\tGPA: " + gpa;
		
		return express;
		
	}
	
	
}
