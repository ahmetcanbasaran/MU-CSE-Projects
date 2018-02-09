
public class Sort {
	
	public static int counter = 0;
	
	public static final int LEFT_PIVOT = 1;
	public static final int MEDIAN_OF_THREE = 2;
	public static final int MIDDLE_PIVOT = 3;
	public static final int RIGHT_PIVOT = 4;
	

	
	public static void quickSort(int[] arr, int left, int right, int insertionCondition, int pivotSelection) {
		   
        	 double controlNumber = Math.abs(left-right)/2.0;
        	 int index = partition(arr, left, right,pivotSelection);
        	 
        	 if((right-left)/2.0 < insertionCondition) {
        		 if (left < index - 1)
        			 InsertionSort(arr, left, index-1);
        		 if (index < right)
        			 InsertionSort(arr, index, right);
        		 return;
        	 } else {
        		 if (left < index - 1)
                     quickSort(arr, left, index - 1, insertionCondition, pivotSelection);
               if (index < right)
                     quickSort(arr, index, right, insertionCondition, pivotSelection);
        	 }
        	 return;
        	
	}
	
	
	
	public static void quickSortWithElimination(int[] arr, int left, int right, int insertionCondition, int pivotSelection) {
		int index = partition(arr, left, right, pivotSelection); 
		if((right-left)/2.0 < insertionCondition) {
    		 if (left < index - 1)
    			 InsertionSort(arr, left, index-1);
    		 if (index < right)
    			 InsertionSort(arr, index, right);
    	 }
		else {
			while (left < right)
		    {
		        /* pi is partitioning index, arr[p] is now
		           at right place */
		        int pi = partition(arr, left, right, pivotSelection);
		        quickSortWithElimination(arr, left, pi-1, insertionCondition, pivotSelection);
		        left = pi;
		        	      
		    }
		}
		
	}
	
	
	
	
	
	
	
	
	
	
	public static int partition(int[] arr, int left, int right, int pivotSelection) {
		
		int pivot = 0;
        if(pivotSelection == LEFT_PIVOT) {
        	pivot = left;
        }else if(pivotSelection == MEDIAN_OF_THREE) {
        	pivot = medianOf3(arr, left, right);
        }else if(pivotSelection == MIDDLE_PIVOT) {
        	pivot = left+(right-left)/2;
        } else {
        	pivot = right;
        }
        
        int i = left, j = right;
        int tmp;
       
        while (i <= j) {
              while (arr[i] < arr[pivot]) {
            	  counter++;
            	  i++;
              }
            	  
              while (arr[j] > arr[pivot]) {
            	  j--;
            	  counter++;
              }
                    
              counter++;
              if (i <= j) {
                    tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                    i++;
                    j--;
              }
        };
        
        return i;
}
	

	
	 public static void InsertionSort(int[] list, int start, int end)
	    {
		 int i, j, newValue;
	      for (i = start+1; i <= end; i++) {
	            newValue = list[i];
	            j = i;
	            while (j > 0 && list[j - 1] > newValue) {
	            	counter++;
	                  list[j] = list[j - 1];
	                  j--;
	            }
	            list[j] = newValue;
	      }
	    }
	
	 private static void exchangeNumbers(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
	 
	 
		
	   public static int medianOf3(int[] intArray, int left, int right) {
		    int center = (left + right) / 2;
		    if(Math.abs(left-right)>=2) {
		    	  if (intArray[left] > intArray[center])
				      exchangeNumbers(intArray, left, center);

				    if (intArray[left] > intArray[right])
				      exchangeNumbers(intArray, left, right);

				    if (intArray[center] > intArray[right])
				      exchangeNumbers(intArray, center, right);

				    exchangeNumbers(intArray, center, right - 1);
				    return right - 1;
		    }else {
		    	return center;
		    }
		  
		  }

}
