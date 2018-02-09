/*This program creates objects of the seven different classes. After that,
 *it changes some variables and object with using methods which are written
 *in the other classes, and prints the results*/

import java.util.Date;

class TesterHW6 {
	
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {

		/* create an author */
		Author joseph = new Author("Joseph Smile", new Date());

		/* create an employee */
		Employee yusuf = new Employee("Yusuf Gül", new Date());

		/* create a manager */
		Person mustafa = new Person("Mustafa Deva", new Date(1938, 11, 10));

		/* set manager of joseph */
		joseph.setManager(mustafa);

		/* create a student with the same birth date of yusuf */
		Student yahya = new Student("Yahya Dogru", yusuf.getBirthDate(), 3.87);

		/* create a dictionary */
		Dictionary whiteHome = new Dictionary(joseph, 6666, 114);

		/* create a faculty */
		Faculty abraham = new Faculty("Abraham Jacob", new Date());
		abraham.setTitle("Prof");

		/* now display the objects */

		System.out.println(whiteHome);
		System.out.println("---------");
		System.out.println(yahya + " " + yahya.getName());
		System.out.println("---------");
		System.out.println(joseph + " " + joseph.getName());
		System.out.println("---------");
		System.out.println(yusuf + " " + yusuf.getName());
		System.out.println("---------");
		System.out.println(mustafa);
		System.out.println("---------");
		System.out.println(abraham + abraham.getName());
		System.out.println("---------");
		/* update a few fields */
		yusuf.setSalary(2750.500);
		yahya.setBorrowedBook(whiteHome);

		/* display changes */
		System.out.println(yahya.getBorrowedBook());
		System.out.println("---------");
		System.out.println(yusuf + " " + yusuf.getName());
		System.out.println("---------");

		/* check subclass hierarchy */
		System.out.println(joseph.getClass().getSuperclass());
		System.out.println("---------");
		if (yahya instanceof Person && whiteHome instanceof Book) {
			System.out.println("good deal :)");
		}
		System.out.println("---------");

		if (abraham instanceof Person && abraham instanceof Employee
				&& abraham instanceof Faculty) {
			System.out.println("Abraham is a grandchild.");
		}
	}

}
