#!/bin/bash

echo $'\n' "###---Hello-$USER---###"


#This while loop supports to program to run every parts until the user want to exit
while : ; do

	echo $'\nPlease select an option:
	1. Print asterisks
	2. Delete files
	3. Substitute words
	4. Organize directory
	5. Print sum of numbers
	6. Exit'

	#Read the user's choice
	read choice

	#Go to and run correct part of the pr11ogram
	case $choice in

		#Question: 1. Print asterisks
		"1")

		echo "Please write filename:"

		read file

		#Check whether the file is exist
		if ! [ -e "$file" ] ; then
		
			 echo "$0: $file does not exist" >&2		# error message includes $0 and goes to stderr

			 exit 1		# exit code is non-zero for error

		fi
	
		#File is exist, then read number in file line by line then print the "*" as readed integer
		while read line ; do
			
			for (( i=0; i<$line; i++)) ; do
			
				echo "*" | tr -d "\n"
				
			done
			
			echo ""

		done < "$file" 
		
		;;
		
		##############################################################################################
		
		"2")
		
		echo "Enter directory name if you want: "
		
		read directory
		
		
		#Check whether obtained a directory
		if ! [ -z $directory ] ; then
		
			cd $directory		#Change directory

		fi
		
		
		#Turn for every file in the current folder
		for i in * ; do

			#Pass if it is a C file
			if [ ${i: -2} == ".c" ] ; then
			
				continue;
			
			#Pass if it is a library file
			elif [ ${i: -2} == ".h" ] ; then
			
				continue;
			
			#Pass if it is a makefile
			elif [[ $i == "Makefile" ]] || [[ $i == "makefile" ]] ; then
			
				continue;
			
			#Run for other files
			else
			
				#Ask to user for every file what he/she want
				echo "$i: ? (y/n) "; #Display File name
	
				read choice
				
				if [[ $choice == "y" ]] || [[ $choice == "Y" ]] ; then
				
					rm -r $i
				
				elif [[ $choice == "n" ]] || [[ $choice == "N" ]] ; then
				
					continue;
				
				elif [[ -z "$choice" ]] ; then
				
					rm -rf * 		#Remove everthing
					
					echo "Current working directory has cleaned up!"
				
					break
				
				fi
	
			fi

 		done
		
		;;
		
		##############################################################################################
		
		"3")

		echo "Please enter filename"
		
		read file
		
		#Check whether the file is exist
		if ! [ -e "$file" ] ; then
		
			 echo "$0: $file does not exist" >&2		# error message includes $0 and goes to stderr

			 exit 1		# exit code is non-zero for error

		fi

		#Get a word which user want to change inside the file
		echo "Please enter word to change"
		read firstWord

		#Get new word
		echo "Please enter new word"
		read secondWord

		#Count how many first word occurs in the file
		counter=$(grep -w "$firstWord" $file | wc -w )
		
		#Change the word and write new word to the file
		sed -i -e "s/$firstWord/$secondWord/g" $file
		
		#Print the result to the user
		echo "All $counter occurrences of “$firstWord” in “$file” has changed with “$secondWord”" 
		
		;;
		
		##############################################################################################
		
		"4") 
		
		#Make a largest and smallest directory if the are not exist
		if ! [ -d "smallest" ]; then

			mkdir smallest ; fi
			
		if ! [ -d "largest" ]; then

			mkdir largest ; fi
		
		
		#Move the smallest file in size to the smallest directory
		file=$(ls -Sr | sed -n '1p')
		
		echo "Smallest file: $file"
		
		mv $file smallest/
		
		#Move the largest file in size to the largest directory
		file=$(ls -S | sed -n '1p')
		
		echo "Largest file: $file"
		
		mv $file largest/
		
		;;
		
		##############################################################################################
		
		"5")

		echo "Please enter a number"

		read number
		
		#Run until user inputs a number which has at least two digits and is positive integer
		until [ $number -gt 10 ] ; do

           echo "Wrong input; try again!" 
           read number 

		done 

		#To reverse the obtained number
		lastDigit=0 
		reverseNumber=0

		while [ $number -gt 0 ] ; do

			lastDigit=$(( $number % 10 ))
			reverseNumber=$(( $reverseNumber * 10 + $lastDigit ))
			number=$(( $number / 10 ))

		done

		#To find the sum of numbers formed by exchanging consecutive digits

		#Use while loop to caclulate the sum of all digits
		while [ $reverseNumber -gt 10 ] ; do

			digits=$(( $reverseNumber % 100 ))		#get digits
			reverseNumber=$(( $reverseNumber / 10 ))		#get next digit
			sum=$(( $sum + $digits ))		#calculate sum of digit

		done

		echo  "Sum of all digit  is $sum"
		
		;;		
		
		##############################################################################################
		
		"6") echo "Have a nice day!" ; exit 0 
		
		;;
		
		
		*) echo "Wrong input!" 
		
		;;

	esac

done

#-----------------------------------------------------------------------------------#
