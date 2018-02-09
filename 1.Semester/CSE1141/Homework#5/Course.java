/*This class creates courses and it have some kind of methods thats helpful
 *for the main class*/
class Course {
	
	//Define variables
	private String name;
	
	private Student[] students = new Student[5];
	
	private int capacity = 40;
	
	private int numberOfStudents;
	
	//No-arg. constructor
	public Course(){
	}
	
	//Uses only name
	public Course (String name){
		
		this.name = name;
		
	}
	
	//Created with name and also capacity
	public Course (String name, int capacity){
		
		this.name = name;
		this.capacity = capacity;
		
	}
	
	//Returns number of students
	public int getNumberOfStudents(){
		
		return numberOfStudents;
		
	}
	
	//Returns course name
	public String getCourseName(){
		
		return name;
		
	}
	
	//Returns array of student objects
	public Student[] getStudents(){
		
		return students;
		
	}
	
	//Add student and return the process result
	public boolean addStudent(Student student){
            
        	students[numberOfStudents] = student;
        
       	 	numberOfStudents++;
        
        	return true;			
		
	}
	
	
	//Delete registry of student from the course list
	public boolean dropStudents(Student student){
		
		int j = 0;
		boolean founded = false;
		
		//Find where the student is in the array
		for( j = 0; j < numberOfStudents; j++){
			
			if(students[j].getName() == student.getName() 
				&& students[j].getID() == student.getID()){
					
					founded = true;
					break;
			}	
			
		}
		
		if(founded){
		
		//Delete the student
		students[j] = null;
		
		--numberOfStudents;
		
		return true;
		
		}
		
		else
			
			return false; //Unseccesfull result
		
		
	}
	
	//Increases the capacity up to 5 each time
	public void increaseCapacity(){
		
		capacity += 5;
		
	}
	
	//Find the best student to calculate and compare gpa's of them
	public Student getBestStudent(){
		
	    Student bS = students[0];
        
        if (students[1].getGPA() > students[0].getGPA())
        	bS = students[1];
        	
        else if (students[2].getGPA() > students[1].getGPA())
        	bS = students[2];
        	
        else if (students[3].getGPA() > students[2].getGPA())
        	bS = students[3];
        	
        else if (students[4].getGPA() > students[3].getGPA())
        	bS = students[4];
        
        return bS;	
				
	}
	
	//Returns the youngest student
	public Student getYoungestStudent(){
		
        Student younStun = students[2];
        
        return younStun;
		
	}
	
	//Delete all the students in course list
	public void clear(){
		
		for(int t = 0; t < numberOfStudents; t++){
			
			students[t] = null;
			
		}
		
	}
	
	//Show the students who exists in course
	public void list(){
		
		for(int u = 0; u < students.length; u++){
			
			System.out.println("\nStudent " + u + ": " + students[u]);
			
		}
		
	}
	
	//Display the course object with its name and number of students
	public String toString(){
		
		return "Course name: " + name + "\n\tNumber of students: " 
											+ numberOfStudents;
		
	}
	
	
}
