/*	This programs runs step by step. In first step, it takes input from user 
 *and controls it. If the input less or long than 16-bits binary or if input
 *consists of any other characters such as letter or number that is different
 *from 1 and 0, the programs warns the user to write 16-bits binary input 
 *correctly. In second step, it takes first 4 digits from the input in order
 *to calculate what the opcode is in decimal with helps of convertToDecimal method.
 *After that, the program invokes instruction method to find the opcode correctly.
 *If the opcode(9 sample opcode) is exist in this program, the method will invoke
 *the opcode's method with sending parameters. Finally, the last step examines the
 *input and divides into parts like the system of run of the opcode and the methods
 *displays the result on the screen.
 *
 *
 *	This program has written by:
 *
 *		150114022 - Oguzhan BÖLÜKBAS
 *
 *
 */
import java.util.Scanner;

class Binary {
	
	//Start value of Program Counter
	static int PC = 1300;
	
	public static String scan (){
		
		//Create a scan method in order to take the input from user
		Scanner input = new Scanner(System.in);
		
		//Create 2 boolean variable to control the input is written correctly or not
		boolean contentController;
		boolean lengthController;
		
		//Create a boolean variable in order to turn 
		//input process until get correct input
		boolean fault = true;
		
		//Create Instruction Register with start value empty
		String IR = "";
		
		
		//Turn until get 16-bits input correctly	
		while(fault){
			
			//At the beginning, boolean controllers assign true
			lengthController = true;
			contentController = true;
			
			//Display the user what he/she should do
			System.out.print("\nEnter the binary value in IR: ");
			
			//Take the input wheter correct or not
			IR = input.nextLine();
			
			//Control the length and if it is not 16-bits, warn the user
			if(IR.length() != 16){
				
				lengthController = false;
				
				System.out.println("\nYour input's length must be 16!");
				
			}
			
			
			//Control every digits of input and if it does not 
			//equal 1 or 0, warn the user
			for(int i = 0; i < IR.length(); i++){
				
				if(IR.charAt(i) != '1' && IR.charAt(i) != '0'){
					
					contentController = false;
					
					System.out.println("\nThe input must consists of only 1s and 0s");
				
					break;
					
				}
							
			}	//End of for loop
			
			
			//Fix the fault true if any fault has not found
			if(lengthController == true && contentController == true){
				
				fault = false;
			
			}
			
		}	//End of while loop
		
		
		return IR;
		
	}
	
	/*This method calculate the number of digits of input, 
	 *and convert it into decimal */
	public static int convertToDecimal (int bottom, int top, char[] instruction){
		
		int decimal = 0;
		
		//This loop takes the first and end point of the domain, 
		//then multiples it with 2's powers
		for(int a = bottom; a < top; a++){
			
			decimal += ((int)instruction[a] - 48) * 
							Math.pow(2, (top-bottom-1)-(a-bottom));
		}
		
		return decimal;
		
	}
	
	/*This method invokes the convertToDecimal method and finds the correct
	*opcode in decimal with it's result*/
	public static void instruction (char[] instruction){
		
		int opcodeInDecimal = 0;
		
		//Had convertToDecimal method calculate the opcode in decimal
		opcodeInDecimal = convertToDecimal(0, 4, instruction);
		
		
		if (opcodeInDecimal == 0)
			
			branch(instruction);	//b0000
			
		else if (opcodeInDecimal == 1)
			
			add(instruction);		//b0001
		
		else if (opcodeInDecimal == 2)
			
			loadIns(instruction);	//b0010
		
		else if (opcodeInDecimal == 3)
			
			storeIns(instruction);	//b0011
		
		else if (opcodeInDecimal == 6)
			
			loadR(instruction);		//b0110
			
		else if (opcodeInDecimal == 7)
			
			storeR(instruction);	//b0111
				
		else if (opcodeInDecimal == 10)
			
			loadImm(instruction);	//b1010
				
		else if (opcodeInDecimal == 11)
			
			storeImm(instruction);	//b1011
				
		else if (opcodeInDecimal == 12)
			
			jumpIns(instruction);	//b1100
				
		else
			
			System.out.println("In this program, " + 
								"there is no instruction for this opcode!");		
		
	}
	
	/*This operator is generated 2 kinds. First generation is sum of the value in 
	 *the register and the other is sum of value in register with immediate value
	 *This operator sums the source registers of source register and immediate
	 *value and writes the result into the destination register */
	public static void add (char[] process){
		
		//Define variables for the 3 registers
		int dest;
		int source1 = 0;
		int source2 = 0;
		
		//Define 
		int immVal = 0;
		int crudeImmVal = 0;
		
		//Crate 2 boolean variables in order to check which generation is used
		boolean useImm = false;
		boolean useReg = false;
		
		//Destination register exists between third and seventh	digits
		dest = convertToDecimal(4, 7, process);
		
		//First source register exists between sixth and tenth digits
		source1 = convertToDecimal(7, 10, process);
		
		//Check that it is register mode
		if (process[10] == '0'){
			
			source2 = convertToDecimal(13, 16, process);;
				
			useReg = true;
			
		}
		
		//Check that it is immediate mode. If it is, calculates the immediate value
		if (process[10] == '1'){
			
			crudeImmVal += convertToDecimal(12, 16, process);
		
				if(process[11] == '1')
			
					immVal = crudeImmVal - 16;
				
				else
				
					immVal = crudeImmVal;
				
			useImm = true;
				
		}
		
		//Print the result
		if (useReg){
			
			System.out.println("ADD " + "R" + dest + " R" + source1 + " R" + source2);
			System.out.println("R" + dest + " = " + "R" + source1 + " + R" + source2);
			
		}
		
		//Print the result
		if (useImm){
			
			System.out.println("ADD " + "R" + dest + " R" + source1 + " #" + immVal);
			System.out.println("R" + dest + " = " + "R" + source1 + " + " + immVal);
		}
		
	}
	
	/*Branch operator calculates last 9 digits of input sign-extended and
	 *changes the program counter */
	public static void branch (char[] process){
		
		int PCOffset9;
		
		int crudePCOffset9 = convertToDecimal(8, 16, process);
		
		//Check the PCOffset9 is whether negative or not.
		//If it is, calculates it
		if(process[7] == '1'){
			
			PCOffset9 = crudePCOffset9 - (int)Math.pow(2, 8);
			
		}
			
		else
			
			PCOffset9 = crudePCOffset9;
		
		System.out.println("BR #" + (PC + 1 + PCOffset9));
		System.out.println("PC = " + (PC + 1 + PCOffset9));
		
	}
	
	/*The Branch code changes the program counter only with additon or 
	 *subtraction the values which are between -32 and +31. Whereas, the jump 
	 *operator changes the program counter directly. It is assigned the value 
	 *that is in the register */
	public static void jumpIns (char[] process){
		
		//Tell to the user in which form the jump operator must be written
		if((convertToDecimal (4, 7, process)) != 0 ||
			 (convertToDecimal (10, 16, process)) != 0 )
		
			System.out.println("The JUMP instruction must be like this: " + 
								"1100 000 Base 000000");
		
		else {
		
			int base = convertToDecimal (7, 10, process);
		
			System.out.println("JMP R" + base);	
			System.out.println("PC = R" + base);
		
		}		
		
	}
	
	/*This instruction has three parts those are opcode, detination register and
	 *pc offset. It adds the sign-extended offset to the incremented program counter.
	 *After that, MAR reads the value of the founded address of memory location and
	 *it loads the value into the destination register. */
	public static void loadIns (char[] process){
		
		int PCOffset9 = 0;
		int dest = convertToDecimal (4,7, process);
		int crudePCOffset9 = convertToDecimal(8, 16, process);
		
		if (process[7] == '1')
			
			PCOffset9 = crudePCOffset9 - (int)Math.pow (2, 8);
			
		else
				
			PCOffset9 = crudePCOffset9;	
		
		System.out.println("LD R" + dest + " M[" + (PC+1) + " + #" + PCOffset9 + "]");
		System.out.println("R" + dest + " = M[" + ((PC+1) + PCOffset9) + "]");
		
	}
	
	/*This instructin is more useful than load instruction owing to the fact that the
	 *load instruction can only access 255 lower the program counter or 256, whereas
	 *that the address of the operand can be anywhere in the computer's memory. This
	 *instruction adds the program counter with pc offset. Then, it reads contents
	 *and sends it to the MAR register again because of the fact that it is not 
	 *operand. After that, it reads the content of the new destination and loads it
	 *into the destination register */
	public static void loadImm (char[] process){
		
		int PCOffset9 = 0;
		int dest = convertToDecimal (4,7, process);
		int crudePCOffset9 = convertToDecimal(8, 16, process);
		
		if (process[7] == '1')
			
			PCOffset9 = crudePCOffset9 - (int)Math.pow (2, 8);
			
		else
				
			PCOffset9 = crudePCOffset9;	
		
		System.out.println("LD R" + dest + " M[M[" + (PC+1) + " + #" + PCOffset9 + "]]");
		System.out.println("R" + dest + " = M[M[" + ((PC+1) + PCOffset9) + "]]");
		
	}
	
	/*This instruciton adds the sign-extended offset with the source register adress
	 *Then, the content of the calculated address of the memory will be written
	 *in to the source register	*/
	public static void loadR (char[] process){
		
		int Offset6 = 0;
		int dest = convertToDecimal(4, 7, process);
		int base = convertToDecimal(7, 10, process);
		int crudeOffset6 = convertToDecimal(11, 16, process);
		
		if (process[10] == '1')
			
			Offset6 = crudeOffset6 - (int)Math.pow(2, 5);
			
		else	
			
			Offset6 = crudeOffset6;	
		
		System.out.println("LDR R" + dest + " M[R" + base + " + #" + Offset6 + "]");
		System.out.println("R" + dest + " = " + "M[R" + base + " + " + Offset6 + "]");
		
	}
	
	/*This instruction runs similarly the load instruciton. The pc offset in [8:0]
	 *is adden t the incremented program counter. Value which is stored source
	 *register will write into the calculated address of the memory location*/
	public static void storeIns (char[] process){
		
		int PCOffset9 = 0;
		int src = convertToDecimal (4,7, process);
		int crudePCOffset9 = convertToDecimal(8, 16, process);
		
		if (process[7] == '1')
			
			PCOffset9 = crudePCOffset9 - (int)Math.pow (2, 8);
			
		else
				
			PCOffset9 = crudePCOffset9;	
		
		System.out.println("ST R" + src + " M[" + (PC+1) + " + #" + PCOffset9 + "]");
		System.out.println("M[" + ((PC+1) + PCOffset9) + "] = " + "R" + src);
		
	}
	
	/*This instruction runs loadImm instruction similarly. In first step, it adds
	 *pc offset with incremented program counter. Then, it read contents, but the
	 *content not instruction, so it reads the value again and the final address
	 *will have the instruction of the source register*/
	public static void storeImm (char[] process){
		
		int PCOffset9 = 0;
		int src = convertToDecimal (4,7, process);
		int crudePCOffset9 = convertToDecimal(8, 16, process);
		
		if (process[7] == '1')
			
			PCOffset9 = crudePCOffset9 - (int)Math.pow (2, 8);
			
		else
				
			PCOffset9 = crudePCOffset9;
		
		System.out.println("ST R" + src + " M[M[" + (PC+1) + " + #" + PCOffset9 + "]]");
		System.out.println("M[M[" + ((PC+1) + PCOffset9) + "]] = " + "R" + src);
		
	}
	
	/*This instruciton adds the sign-extended offset with the source register adress
	 *Then, the content of the source register will be writen there.	*/
	public static void storeR (char[] process){
		
		int Offset6 = 0;
		int src = convertToDecimal(4, 7, process);
		int base = convertToDecimal(7, 10, process);
		int crudeOffset6 = convertToDecimal(11, 16, process);
		
		if (process[10] == '1')
			
			Offset6 = crudeOffset6 - (int)Math.pow(2, 5);
			
		else	
			
			Offset6 = crudeOffset6;
		
		System.out.println("STR R" + src + " M[R" + base + " + #" + Offset6 + "]");
		System.out.println("M[R" + base + " + " + Offset6 + "] = R" + src);
		
	}	
	
	/*Main method. It invokes scan method,then it changes the string value into the
	 *char. Then, invokes the instruction method*/
	public static void main (String[] args){
		
		//Take the input in string form with scan methods
		String IR = scan();
		
		//Convert the string input into array forms
		char[] binary = IR.toCharArray();
		
		//Invoke the instruction method with sending array like a parameter.
		instruction (binary);
		
	}
	
}
