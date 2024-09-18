;
; Program reads user input into an array and finds the largest and smallest values of the array
; User enters 999999 (six nines) when done inputting
;
;
; 0101 will be variable x
; 0102 will be variable y
;
; Start by reading values into array, the address of which is stored in loc 0100, the address being 0105
0000 22 0100 ; loadx 0100 -- loc 0100 has address for array
0001 10 0101 ; read 0101 -- Read into x
0002 ; load 0101 -- load x into acc
; now see if x == 999999, which is saved at loc 0103 
; subtract 0103 -- x - 999999
; branchzero xxxx -- branch out of array loading
; add 0103 -- x + 999999 to get original value of x
; storex -- store acc into array
; inc
; branch 0001 -- read next input 

; array loading done - now find max
; swap -- put index of last value into acc
; subtract 0100 -- subtract statrt to get array length
; 
; load 0104 -- x = -999999, which is in location 0104