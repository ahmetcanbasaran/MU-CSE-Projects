import java.awt.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;
import java.util.Scanner;

import javax.swing.text.html.HTMLDocument.Iterator;

public class Problem2 {
	
	public static void main(String[] args) {
		
		if(args.length>0) {
			
			String inputText = readFile(args[0]);
			System.out.println(inputText);
			
			String lines[] = inputText.split("\n");
			String firstLine[] = lines[1].split("\t");
			final int numberOfLaptop = Integer.parseInt(firstLine[0]);
			
			System.out.println("asdasd: " + numberOfLaptop);
			
		
			Laptop[] laptops = new Laptop[numberOfLaptop];
			
			for (int i=2; i<lines.length; i++) {
				String lineString[] = lines[i].split("\t");
				
				laptops[i-2] = new Laptop(Double.parseDouble(lineString[0]),
						Double.parseDouble(lineString[1]), 
						Double.parseDouble(lineString[2]));
				
			}
			
			LinkedList<Integer>[] graph = graphMaker(laptops);
			
			int result[] = findDistance(graph);
			String output = "";
			for (int i : result) {
				output += i + "\n";
			}
			System.out.println("Result: \n" + output);
			writeToFile("outputProblem2.dat", output);
			
		}
		
	}
	
	public static LinkedList<Integer>[] graphMaker(Laptop[] laptops) {
		int numberOfLaptop = laptops.length;
		LinkedList<Integer>[] graph = new LinkedList[numberOfLaptop];
		
		for(int i=0; i<numberOfLaptop; i++) {
			graph[i] = new LinkedList<Integer>();
		}
		
		for(int i=0; i<numberOfLaptop; i++) {
			for(int j=0; j<numberOfLaptop; j++) {
				if(i != j) {
					double distance = Math.sqrt(Math.pow(laptops[i].x-laptops[j].x, 2) + Math.pow(laptops[i].y-laptops[j].y, 2));	
					if(laptops[i].r >= distance) {
						graph[i].add(j);
					}
				}
			}
		}
		
		return graph;
	}
	
	public static int[] findDistance(LinkedList<Integer>[] graph) {
		
		Queue<Integer> queue = new LinkedList<Integer>();
		Queue<Integer> queueHelper = new LinkedList<Integer>();
		int[] result = new int[graph.length];
		
		queue.add(0);
		queueHelper.add(0);
		
		for(int i=1; i<result.length; i++) {
			result[i] = Integer.MAX_VALUE;
		}
		
		while(!queue.isEmpty()) {
			int currentLaptop = queue.poll();
			ListIterator<Integer> it = (ListIterator<Integer>) graph[currentLaptop].iterator();
			
			while(it.hasNext()) {
				int tempLaptop = it.next();
				if(queueHelper.contains(tempLaptop)) {
					continue;
				}
				queue.add(tempLaptop);
				queueHelper.add(tempLaptop);
				
				if(result[tempLaptop] > result[currentLaptop] + 1) {
					result[tempLaptop] = result[currentLaptop] + 1;
				}
				
			}
		}
		
		for(int i=0; i<result.length; i++) {
			
			if(result[i] == Integer.MAX_VALUE)
				result[i] = 0;
				
		}
		
		return result;
		
	}
	
	public static String readFile (String url) {
		File file = new File(url);
		String str = "";
		Scanner sc;
		try {
			sc = new Scanner(file);
			
			while(sc.hasNextLine()) {
				str = str + "\n" + sc.nextLine();
			}
			sc.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return str;
	}
		
		
		public static void writeToFile(String url, String s) {
			File file = new File(url);
			try {
				file.createNewFile();
				System.out.println("The file is created");
				
				PrintWriter writer  = new PrintWriter(file.getPath(), "UTF-8");
				writer.print(s);
				writer.close();
				
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

}

class Laptop {
	
	double x;
	double y;
	double r;
	
	public Laptop(double x, double y, double r) {
		this.x = x;
		this.y = y;
		this.r = r;
	}
	

	
	
}