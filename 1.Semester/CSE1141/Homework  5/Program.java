/*This program creates cources and courses' students and students' personal data
 With helps of methods that exist in subclass, the program class can do different
 changes on the course*/
class Program{
	
	public static void main (String[] args){
		
		//Define the birtdates with milliseconds
		java.util.Date birthDate1 = new java.util.Date(1905472124);
		java.util.Date birthDate2 = new java.util.Date(1090521028);
		java.util.Date birthDate3 = new java.util.Date(1005721284);
		java.util.Date birthDate4 = new java.util.Date(1090572284);
		java.util.Date birthDate5 = new java.util.Date(1005472184);
		
		//Define the personal datas with birthdate and ssn
		PersonalData p1 = new PersonalData(94, 9, 10, 98465 );
		PersonalData p2 = new PersonalData(97, 3, 3, 65978 );
		PersonalData p3 = new PersonalData(94, 3, 7, 93568 );
		PersonalData p4 = new PersonalData(96, 6, 1, 69325 );
		PersonalData p5 = new PersonalData(95, 7, 11, 96465 );
		
		//Define the students with their name, id, gpa and personal datas
		Student s1, s2, s3, s4, s5;
		s1 = new Student ("Murat ÇELIK" , 5001, 2.59, p1);
		s2 = new Student ("Gamze AKKAN" , 5002, 2.12, p2);
		s3 = new Student ("Mine DOGANGÜN" , 5003, 3.14 , p3);
		s4 = new Student ("Furkan GÖNÜLALAN" , 5004, 2.89, p4);
		s5 = new Student ("Ahmet Yasin ÖZER" , 5005, 2.46, p5);
		
		//Crate a course object
		Course course1 = new Course ("CSE141" , 3);
		
		//Add 3 students into the course1 randomly
		course1.addStudent(s1);
		course1.addStudent(s4);
		course1.addStudent(s2);
		System.out.println("Three students added into the CSE141");
		
		//Show the course students
		course1.list();
		
		//Increase the capacity
		course1.increaseCapacity();
		System.out.println("Capacity of the CSE141 increased (+5)");
		
		//Add two more students
		course1.addStudent(s5);
		course1.addStudent(s3);
		System.out.println("Two more students added into the CSE141");
		
		//Print the students
		course1.list();
		
		System.out.println("\nThe student which has ID 5005 dropped? " + 
							course1.dropStudents(s5));
		
		System.out.println("New list of CSE141");
		course1.list(); 	//Print the students
		
		
		System.out.printf("\nNumber of students enrolled to CSE141: %d" ,
							 course1.getNumberOfStudents());
							 
		//Find the best student according to GPA and show his/her birthdate		
		System.out.println("\n\nBirth year of the best student of the CSE141: " +
							course1.getBestStudent().getPersonalData().getBirthDate().getYear());
		
		//Create a new course					
		Course course2 = new Course ("CSE142");
		System.out.println("New course created (CSE 142)");
		
		//Write the names of students of course1 into the course2 list
		Student[] stu = course1.getStudents();
        for(int p = 0; p < course1.getNumberOfStudents(); p++){
     
            course2.addStudent(stu[p]);
            
        }
 
		//Clear the CSE141
		course1.clear();
		System.out.println("CSE141 has been cleared");
		
		System.out.println("List of CSE142: ");
		course2.list();
		
		//Delete the name of best students from course2 list
		course2.dropStudents(course2.getBestStudent());
		System.out.println("The best student has been dropped");
		
		//Show the students
		System.out.println("New list of the CSE142");
		course2.list();
		
		//Find and show youngest student's gpa
		System.out.println("GPA of the youngest student in CSE 142: " + 
							course2.getYoungestStudent().getGPA());
		
		//Display the course objects
		System.out.println(course1);
		System.out.println(course2);
		
	} 
	
}