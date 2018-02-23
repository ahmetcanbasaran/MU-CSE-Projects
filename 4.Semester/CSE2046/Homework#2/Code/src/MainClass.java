import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

import javax.naming.ldap.SortControl;
import javax.swing.text.html.MinimalHTMLWriter;

public class MainClass {
	
	
	public static void main(String[] args) {
		int in = 0;
		int keeper[] = new int[1];
		int arr[] = new int[1];
		long startTime, finishTime,time;
		ArrayList<Integer> countersLeftNormal = new ArrayList<Integer>();
		ArrayList<Long> timesLeftNormal = new ArrayList<Long>();
		ArrayList<Integer> countersMedianNormal = new ArrayList<Integer>();
		ArrayList<Long> timesMedianNormal = new ArrayList<Long>();
		ArrayList<Integer> countersLeftElim = new ArrayList<Integer>();
		ArrayList<Long> timesLeftElim = new ArrayList<Long>();
		ArrayList<Integer> countersMedianElim = new ArrayList<Integer>();
		ArrayList<Long> timesMedianElim = new ArrayList<Long>();
		ArrayList<Integer> sizeOfInput = new ArrayList<Integer>();
		ArrayList<Integer> insertions = new ArrayList<Integer>();
		
		Scanner sc = new Scanner(System.in);
		System.out.println("input size: insort");
		int size = sc.nextInt();
		int insert = 0;
		int pivot = Sort.LEFT_PIVOT;
		
		int counterTime = 0;
		
		for(int j=1; j<=500; j++ ) {
			
			
			int sizeOfArr = size*j;
			keeper = randomInput(sizeOfArr);
			
			
			//timesLeftNormal.clear();
			//countersLeftNormal.clear();
			for(int i=0; i<=in; i++) {
				
				insertions.add(i);
				sizeOfInput.add(sizeOfArr);
				arr = keeper.clone();
				Sort.counter = 0;
				startTime = System.currentTimeMillis();
				Sort.quickSort(arr, 0, arr.length-1, i, Sort.MIDDLE_PIVOT);
				finishTime = System.currentTimeMillis();
				time = finishTime - startTime;
				timesLeftNormal.add(time);
				countersLeftNormal.add(Sort.counter);
				System.out.println("loading: % " + ((counterTime++)/180.0*100));
			}
			
			
			//timesMedianNormal.clear();
			//countersMedianNormal.clear();
			for(int i=0; i<=in; i++) {
				arr = keeper.clone();
				Sort.counter = 0;
				startTime = System.currentTimeMillis();
				Sort.quickSort(arr, 0, arr.length-1, i, Sort.MEDIAN_OF_THREE);
				finishTime = System.currentTimeMillis();
				time = finishTime - startTime;
				timesMedianNormal.add(time);
				countersMedianNormal.add(Sort.counter);
				System.out.println("loading: % " + ((counterTime++)/180.0*100));
				
			}
			//timesLeftElim.clear();
			//countersLeftElim.clear();
			for(int i=0; i<=in; i++) {
				arr = keeper.clone();
				Sort.counter = 0;
				startTime = System.currentTimeMillis();
				Sort.quickSortWithElimination(arr, 0, arr.length-1, i, Sort.MIDDLE_PIVOT);
				finishTime = System.currentTimeMillis();
				time = finishTime - startTime;
				timesLeftElim.add(time);
				countersLeftElim.add(Sort.counter);
				System.out.println("loading: % " + ((counterTime++)/180.0*100));
			}
			
			//timesMedianElim.clear();
			//countersMedianElim.clear();
			for(int i=0; i<=in; i++) {
				arr = keeper.clone();
				Sort.counter = 0;
				startTime = System.currentTimeMillis();
				Sort.quickSortWithElimination(arr, 0, arr.length-1, i, Sort.MEDIAN_OF_THREE);
				finishTime = System.currentTimeMillis();
				time = finishTime - startTime;
				timesMedianElim.add(time);
				countersMedianElim.add(Sort.counter);
				System.out.println("loading: % " + ((counterTime++)/180.0*100));
				
			}
			
		}
		
		for(int i=1; i<=countersLeftElim.size(); i++) {
			System.out.println(sizeOfInput.get(i-1)+"\tNormal\t"+insertions.get(i-1)+"\t"+
		timesLeftNormal.get(i-1)+"\t"+
		countersLeftNormal.get(i-1)+"\t"+
		timesMedianNormal.get(i-1)+"\t"+
		countersMedianNormal.get(i-1)+"\t"+
		"Elim"+"\t"+
		timesLeftElim.get(i-1)+"\t"+
		countersLeftElim.get(i-1)+"\t"+
		timesMedianElim.get(i-1)+"\t"+
		countersMedianElim.get(i-1));
		
		}
		
		
		
		
		
	}
		

	
	public static int[] stringToArray(String input) {
		
		String[] strings = input.split("\n");
		int arr[] = new int[strings.length-1];
		for (int i=0; i<strings.length-1; i++) {
			arr[i] = Integer.parseInt(strings[i]);
		}
		return arr;
	}
	

	public static void generateLogarithmicInput(int numberOfRepeat, int range) {
		//Generate input files
		for(int inputPower=1; inputPower<=numberOfRepeat; inputPower++) {
			int sizeOfInput = (int) Math.pow(range, inputPower);
			System.out.println("Size of input is determined: " + sizeOfInput);
			
			//Sorted
			String inputText = "";
			for(int index = 0; index<sizeOfInput; index++) {
				
			
				inputText =  inputText.concat(index+"\n");
			}
			System.out.println("sorted_log_"+range+"_"+inputPower+"'s inputs iare generated for sorted" );

			writeToFile("sorted_log_"+range+"_"+inputPower+".txt", inputText);
			System.out.println("sorted_log_"+range+"_"+inputPower+".txt"+" is generated for sorted");
			
			//unsorted
			inputText = "";
			for(int index = sizeOfInput; index>0; index--) {
				
			
				inputText =  inputText.concat(index+"\n");
			}
			System.out.println("unsorted_log_"+range+"_"+inputPower+"'s inputs iare generated for unsorted" );
			
			writeToFile("unsorted_log_"+range+"_"+inputPower+".txt", inputText);
			System.out.println("unsorted_log_"+range+"_"+inputPower+".txt"+" is generated for unsorted");
			
			
			//Random
			inputText = "";
			for(int index = 0; index<sizeOfInput; index++) {
				
				int randomNumber = (int)(Math.random()*Integer.MAX_VALUE)+1;
				inputText =  inputText.concat(randomNumber+"\n");
			}
			System.out.println("random_log_"+range+"_"+inputPower+"'s inputs iare generated for random" );
	
			writeToFile("random_log_"+range+"_"+inputPower+".txt", inputText);
			System.out.println("random_log_"+range+"_"+inputPower+".txt"+" is generated for random");
			
			System.out.println("Inputs are generated");
			
		}
	
	}
	
	public static void generateArithmeticInput(int numberOfRepeat, int range) {
		//Generate input files
		for(int inputPower=0; inputPower<=numberOfRepeat; inputPower++) {
			int sizeOfInput = 20 + inputPower*range;
			System.out.println("Size of input is determined: " + sizeOfInput);
			
			//Sorted
			String inputText = "";
			for(int index = 0; index<sizeOfInput; index++) {
				
			
				inputText =  inputText.concat(index+"\n");
			}
			System.out.println("sorted_arit_"+range+"_"+inputPower+"'s inputs iare generated for sorted" );

			writeToFile("sorted_arit_"+range+"_"+inputPower+".txt", inputText);
			System.out.println("sorted_arit_"+range+"_"+inputPower+".txt"+" is generated for sorted");
			
			//unsorted
			inputText = "";
			for(int index = sizeOfInput; index>0; index--) {
				
			
				inputText =  inputText.concat(index+"\n");
			}
			System.out.println("unsorted_arit_"+range+"_"+inputPower+"'s inputs iare generated for unsorted" );
			
			writeToFile("unsorted_arit_"+range+"_"+inputPower+".txt", inputText);
			System.out.println("unsorted_arit_"+range+"_"+inputPower+".txt"+" is generated for unsorted");
			
			
			//Random
			inputText = "";
			for(int index = 0; index<sizeOfInput; index++) {
				
				int randomNumber = (int)(Math.random()*Integer.MAX_VALUE)+1;
				inputText =  inputText.concat(randomNumber+"\n");
			}
			System.out.println("random_arit_"+range+"_"+inputPower+"'s inputs iare generated for random" );
	
			writeToFile("random_arit_"+range+"_"+inputPower+".txt", inputText);
			System.out.println("random_arit_"+range+"_"+inputPower+".txt"+" is generated for random");
			
			System.out.println("Inputs are generated");
			
		}
	
	}
	
	public static int[] randomInput(int length) {
		int arr[] = new int[length];
		for(int i=0; i<arr.length; i++) {
			arr[i] = (int)(Math.random()*Integer.MAX_VALUE);
		}
		return arr;
	}
	
	public static int[] sortedInput(int length) {
		int arr[] = new int[length];
		for(int i=0; i<arr.length; i++) {
			arr[i] = i;
		}
		return arr;
	}
	
	
	public static void writeToFile(String url, String text) {
		try{
			
			File file = new File(url);
			if(!file.exists())
				file.createNewFile();
		    PrintWriter writer = new PrintWriter(url, "UTF-8");
		    writer.println(text);
		    writer.close();
		    
		} catch (IOException e) {
		   System.err.println("The text cannot printed to txt file!");
		}
	}
	
	public static String readFromFile(String url) {
		 String text = "";
		try {
			File file  = new File(url);
			Scanner scnr = new Scanner(file);
		     
			while(scnr.hasNextLine()){
		            String line = scnr.nextLine();
		            
		            
		            	text = text.concat(line);
		            	text = text.concat("\n");
		            
		            	
		            
		        } 
		
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			System.err.println("The text cannot be readen from the txt file.");
		}
		
		return text;
       
	}

}
