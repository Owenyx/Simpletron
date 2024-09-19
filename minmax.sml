;
; Program reads user input into an array and finds the largest and smallest values of the array
; User enters 999999 (six nines) when done inputting
; output will be the max number followed by the min
;
; 0101 will be variable x
; 0102 will be variable y
; 0103 will store length of the array when calculated
;
; Start by reading values into array, the address of which is stored in loc 0100, the address being 0110
0000 22 0100 ; loadx 0100 -- loc 0100 has address for array
0001 10 0101 ; read 0101 -- Read into x
0002 20 0101 ; load 0101 -- load x into acc
0003 41 0007 ; branchneg 0007 -- if x is negative then following subtraction will overflow, so avoid it
0004 32 0105 ; subtract 0105 -- x - 999999 to see if x == 999999, which is saved at loc 0105
0005 42 0010 ; branchzero 0010 -- branch out of array loading
0006 30 0105 ; add 0105 -- x + 999999 to get original value of x
0007 26 ; storeidx -- store acc into array
0008 38 ;inc
0009 40 0001 ; branch 0001 -- read next input 

; array loading done
; store length
0010 43 ; swap -- put index of last value loaded into acc
0011 32 0100 ; subtract 0100 -- subtract start to get array length
0012 42 0040 ; branchzero 0040 -- jump to halt if array is empty
0013 25 0103 ; store 0103 -- 0103 will save the arrays length

;  now find max and min
0014 25 0104 ; store 0104 -- 0104 will be used to track loop iterations, now has array length
0015 22 0100 ; loadx 0100 -- idx = array start = i
0016 23 ; loadidx -- acc = arr[0]
0017 25 0101 ; store 0101 -- x = acc -- x will store the max
0018 25 0102 ; store 0102 -- y = acc -- y will store the min

;  for length of array
0019 38 ; inc -- i++

; check and update loop iterations
0020 20 0104 ; load 0104 -- acc = iterations
0021 43 ; swap -- put iteration into idx
0022 39 ; dec
0023 43 ; swap -- put iteration into acc and i back to idx
0024 42 0038 ; branchzero 0038 -- if iterations == 0, whole array checked
0025 25 0104 ; store 0104 -- update iterations remaining

; check x
0026 20 0101 ; load 0101 -- acc = x
0027 33 ; subtractx -- acc(x) - arr[i]
0028 41 0035 ; branchneg 0035 -- go to x is smaller to change it
; otherwise x is bigger, don't change it

; check y 
0029 20 0102 ; load 0102 -- acc = y
0030 33 ; subtractx -- acc(y) - arr[i]
0031 41 0034 ; branchneg 0034 -- y is smaller, go around to avoid changing y

; y is bigger, change y to new min, arr[i]
0032 23 ; loadidx -- acc = arr[i]
0033 25 0102 ; store 0102 -- y = acc = new min

0034 40 0019 ; branch 0019 -- repeat loop

; x is smaller, change x to new max, arr[i]
0035 23 ; loadidx -- acc = arr[i]
0036 25 0101 ; store 0101 -- x = acc = new max
0037 40 0029 ; branch 0029 -- branch to check y

; max and min found
0038 11 0101 ; write 0101 -- print x = max
0039 11 0102 ; write 0102 -- print y = min
0040 45 0001 ; HALT 0001

0100 000110
0105 999999