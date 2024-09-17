;
; program reads values in an array  and displays the sum of these. If no values are
; entered it displays -1. program assumes that all elements of array are positive.
;
;
0000 22 0100		;loadx  	0100	loc 0100 holds base address of array
0001 10 0101		;read		0101	tmp var to hold value that we will store in array
0002 20 0101		;load		0101	take value and put in accumulator
0003 41 7		;branchneg	7	if value <0 we are done reading continue execution
0004 26 		;storeidx		save the value in the array 
0005 38 		;inc			move to next array location
0006 40 0001		;branch		1	read the next element of array
0007 43 		;swap			acc may hold addr of location one past last element 
0008 32 0100		;subtract	0100	if acc holds 0 no values were entered
0009 42 0025		;branchzero	25	branch to code that outputs -1 as sum
0010 30 0100		;add 		0100	
0011 43 		;swap			index register now hold addr of location one past last element 
0012 21 0000		;loadim		0000	acc has 0 in it
0013 39 		;dec			and we have at least one element in array
0014 31 		;addx				
0015 43 		;swap			mov sum to index register 
0016 32 0100		;subtract	0100	
0017 42 0021		;branchzero  	21	we are done summing, branch to code that outputs sum
0018 30 0100		;add		0100
0019 43 		;swap
0020 40 0013		;branch		13
0021 43 		;swap			this swap puts the sum back in accumulator
0022 25 0101		;store		0101
0023 11 0101		;write		0101
0024 45 0001		;halt		00,01	dump first 2 pages
0025 21 -0001		;loadim		-1
0026 25 0101		;store		0101
0027 11 0101		;write		0101
0028 45 0001    	;halt		00,01

0100 0105					;holds the starting loc of array