; 
; program reads 2 positive integers and displays the greatest common divisor.
; the program uses euclid's algorithm
; program terminates if either input is negative or zero
;
;
; First get the 2 positive integer inputs
* 10 0100; read 0100 -- 0100 will be x
* 10 0101; read 0101 -- 0101 will be y

; check that they are both positive
* 20 0100; load 0100 x
* 41 0023; jump to halt if negative
* 42 0023; jump to halt if zero
* 20 0101; load 0101 y
* 41 0023; jump to halt if negative
* 42 0023; jump to halt if zero


; now check which is larger
* 20 0100; load 0100
* 32 0101; subtract 0101
* 41 0013; branchneg 0013 -- if y is greater, branch to that case
* 25 0100; store 0100 -- else x is greater, so store that as the new x
* 40 0017; branch 0017 -- branch to the part that checks equality

; y is larger
* 20 0101; load 0101 -- load y
* 32 0100; subtract 0100 -- y is greater, so subtract x from it
* 25 0101; store 0101 -- store the difference as the new y
* 40 0017; branch 0017 -- branch to the part that checks equality

; check equality
* 20 0100; load 0100 -- load x
* 32 0101; subtract 0101 -- subtract y
* 42 0021; branchzero 0021 -- if x == y, then x == y == GCD of both, so branch to display GCD
* 40 0002; branch 0002 -- otherwise repeat the subtraction

; display GCD
* 20 0100; load 0100 -- load x (now GCD)
* 11 0100; write 0100 -- print x
* 45 0001; halt 0001