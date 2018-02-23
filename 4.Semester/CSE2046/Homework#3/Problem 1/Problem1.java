import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.Scanner;
import java.util.Stack;

public class Problem1 {
	
	public static void main(String[] args) {
		
		if(args.length>0) {
			
			String inputText = readFile(args[0]);
			System.out.println(inputText);
			
			String lines[] = inputText.split("\n");
			String firstLine[] = lines[1].split("\t");
			System.out.println(Arrays.toString(firstLine));
			int numberOfRow = Integer.parseInt(firstLine[0]);
			int numberOfColumn = Integer.parseInt(firstLine[1]);
			
			System.out.println("row: " + numberOfRow);
			System.out.println("col: " + numberOfColumn);
			String values[][] = new String[lines.length][7];
		
			int grid[][] = new int[numberOfRow][numberOfColumn];
			
			for (int i=2; i<lines.length; i++) {
				String lineString[] = lines[i].split("\t");
				
				for(int j=0; j<lineString.length; j++) {
					String val = lineString[j];
					if(val.equals("X")) {
						grid[i-2][j] = -99;
					} else {
						grid[i-2][j] = Integer.parseInt(val);
					}
				}
			}
			
			String x = findBestPath(grid);
			writeToFile("outputProblem1.dat", x);
			System.out.println(x);
			
		}
		
		
	}
	
	// This method is applicating the algorithm.
	public static String findBestPath(int[][] input) {
		
		int [][] grid = clone(input);
		
		//Taking row and calumn number.
		int numberOfRow = grid.length;
		int numberOfColumn = grid[0].length;
		
		//Update the weight of all cells for taken grid.
		for(int i=0; i<numberOfRow; i++) {
			for(int j=0; j<numberOfColumn; j++) {
				if(grid[i][j] == -99) {
					
				} else if(i>0 && j>0) {
					int value = Math.max(grid[i-1][j], grid[i][j-1]);
					if(value != -99)
						grid[i][j] += value;
				} else if(i>0) {
					int value = grid[i-1][j];
					if(value != -99)
						grid[i][j] += value;
				} else if(j>0) {
					int value = grid[i][j-1];
					if(value != -99)
						grid[i][j] += value;
				} 
			}
		}
		
		Stack<Tuple> myStack = new Stack<Tuple>();
		
		myStack.push(new Tuple(numberOfRow-1, numberOfColumn-1));
		determineBestWay(myStack, grid, numberOfRow-1, numberOfColumn-1);
		
		int totalValue = 0;
		while(!myStack.isEmpty()) {
			Tuple tempTuple = myStack.pop();
			totalValue += input[tempTuple.x][tempTuple.y];
			input[tempTuple.x][tempTuple.y] = 888;
		}
		StringBuilder strBuilder = new StringBuilder();
		strBuilder.append(totalValue + "\n");
		
		for(int i=0; i<numberOfRow; i++) {
			for(int j=0; j<numberOfColumn; j++) {
				if(input[i][j] == -99) {
					strBuilder.append("X" + "\t");
				} else if(input[i][j] == 888) {
					strBuilder.append("P" + "\t");
				} else {
					strBuilder.append(input[i][j] + "\t");
				}
			}
			strBuilder.deleteCharAt(strBuilder.length()-1);
			if(i != numberOfRow-1)
				strBuilder.append("\n");
		}
		
		return strBuilder.toString();
		
	}
	
	public static int[][] clone(int[][] array) {
		int [][] clone = new int[array.length][array[0].length];
		
		for(int i=0; i<array.length; i++) {
			for(int j=0; j<array[0].length; j++) {
				clone[i][j] = array[i][j];
			}
		}
		return clone;
	}
	
	public static void determineBestWay(Stack<Tuple> stack, int[][] grid, int i, int j) {
		if(i>0 && j>0) {
			if(grid[i-1][j] > grid[i][j-1]) {
				if(grid[i-1][j] >= 0) {
					stack.push(new Tuple(i-1, j));
					determineBestWay(stack, grid, i-1, j);
				} else {
					grid[i][j] = -99;
					stack.pop();
					Tuple tempTuple = stack.peek();
					determineBestWay(stack, grid, tempTuple.x, tempTuple.y);
				}
			} else {
				if(grid[i][j-1] >= 0) {
					stack.push(new Tuple(i, j-1));
					determineBestWay(stack, grid, i, j-1);
				} else {
					grid[i][j] = -99;
					stack.pop();
					Tuple tempTuple = stack.peek();
					determineBestWay(stack, grid, tempTuple.x, tempTuple.y);
				}
			}
		} else if(i>0) {
			if(grid[i-1][j] >= 0) {
				stack.push(new Tuple(i-1, j));
				determineBestWay(stack, grid, i-1, j);
			} else {
				grid[i][j] = -99;
				stack.pop();
				Tuple tempTuple = stack.peek();
				determineBestWay(stack, grid, tempTuple.x, tempTuple.y);
			}
		} else if(j>0) {
			if(grid[i][j-1] >= 0) {
				stack.push(new Tuple(i, j-1));
				determineBestWay(stack, grid, i, j-1);
			} else {
				grid[i][j] = -99;
				stack.pop();
				Tuple tempTuple = stack.peek();
				determineBestWay(stack, grid, tempTuple.x, tempTuple.y);
			}
		}
	}
	
	public static int func(int[][] grid, int i, int j) {
		if(i>0 && j>0) {
			return Math.max(func(grid, i-1, j), func(grid, i, j-1)) + grid[i][j];
		} else if(i>0) {
			int val = func(grid, i-1, j);
			if(val + grid[i][j] < 0) {
				return -99;
			}
			return val + grid[i][j];
		} else if(j>0) {
			int val = func(grid, i, j-1);
			if(val + grid[i][j] < 0) {
				return -99;
			}
			return val + grid[i][j];
		} else {
			return grid[i][j];
		}
 		
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

 class Tuple { 
	  public final int x; 
	  public final int y; 
	  public Tuple(int x, int y) { 
	    this.x = x; 
	    this.y = y; 
	  } 
	} 