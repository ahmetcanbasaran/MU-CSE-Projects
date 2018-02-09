/*This class creates a personal datas, some of the unique like ssn,
 *whereas the other can be common like address*/

import java.util.Date;

class PersonalData {

	//Define variables
	private java.util.Date birthDate = new java.util.Date();
	
	private long ssn;
			
	private String address;
	
	//No-arg. constructor
	public PersonalData (){
	}
	
	//Use directly birthdate and ssn
	public PersonalData(java.util.Date birthDate, long ssn){
			
		this.birthDate = birthDate;
		
		this.ssn = ssn;	
	}
	
	//Define constructor with parameters of all variable
	public PersonalData (int year, int month, int day, long ssn){
				
		this.birthDate = new Date(year, month, day);
		
		this.ssn = ssn;
		
	}
	
	//Returns birthdate
	public Date getBirthDate(){
		
		return birthDate;
		
	}
	
	//Returns address
	public String getAddress(){
		
		return address;
		
	}
	
	//Returns ssn
	public long getSsn(){
		
		return ssn;
		
	}
	
	//Returns address
	public void setAddress(String address){
		
		this.address = address;
		
	}
		
		
		
}
