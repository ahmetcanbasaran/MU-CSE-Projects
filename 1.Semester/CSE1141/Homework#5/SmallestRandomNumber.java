import java.util.Scanner;

class SmallestRandomNumber {
	
	final static int AMOUNT_OF_NUMBERS = 15;
	
	public static int[] Random(){
		
		int[] numeros = new int[AMOUNT_OF_NUMBERS];
		
		for (int i = 0; i < numeros.length ; i++){
			
			numeros [i] = (int)(Math.random() * 100 ) + 1;
			
		}
		
		return numeros;
		
	}
	
	public static int Scan(){
		
		int obtained = 0;
		boolean wrongInput = true;
		
		while (wrongInput){
				
			Scanner input = new Scanner(System.in);
		
			System.out.printf("Enter smallest number's order: ");
			
			obtained = input.nextInt();
			
			if (obtained < 1 || obtained > 14){
				
				System.out.printf("\nYou wrote out of the range number!\n\n");
				System.out.printf("");
				
			}
			
			else
				
				wrongInput = false;
				
		}
		
		return obtained;		
		
	}
	
	public static void PrintArray(int[] generatedArray){
		
		System.out.printf("Randomly generated array is: {");
		
		for(int count = 0; count < generatedArray.length -1 ; count++ ){
			
			System.out.printf("%d," , generatedArray[count]);
			
		}
		
		System.out.printf("%d}\n" , generatedArray[generatedArray.length - 1]);
		
	}
	
	public static void Print(int orderValue, int number, int[] printableArray){
		
		if (orderValue == 1)
			System.out.printf("\n%dst smallest element is: %d" , orderValue, number);
			
		else if( orderValue == 2)
			System.out.printf("\n%dnd smallest element is: %d" , orderValue, number);
			
		else if (orderValue == 3)				
			System.out.printf("\n%drd smallest element is: %d" , orderValue, number);
			
		else
			System.out.printf("\n%dth smallest element is: %d" , orderValue, number);	
	}
	
	public static int findNthSmallestNumber(int n, int[] numbers){
				
		int[] orderedArray = new int[AMOUNT_OF_NUMBERS];
		
		int writtenNumbers = 0;
		
		for(int m = 0; m < 101; m++){
			
			for(int k = 0; k < numbers.length ; k++){
				
				if (m == numbers[k]){
					
					orderedArray[writtenNumbers] = m;
					
					writtenNumbers++;
					
				}
				
			}
			
		}		
		
		
		int wantedValue = orderedArray[n-1];
		
		return wantedValue;
		
	}	
	
	public static void main (String[] args){
		
		int[] randomArray = Random();
		
		PrintArray(randomArray);
		
		int order = Scan();
		
		int smallestNumber = findNthSmallestNumber(order, randomArray);
		
		Print(order, smallestNumber, randomArray);
		
	}
	
}
