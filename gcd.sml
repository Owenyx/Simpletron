; 
; program reads 2 positive integers and displays the greatest common divisor.
; the program uses euclid's algorithm
;
;
; First get the 2 positive integer inputs
0000 10 0100; read 0100 -- 0100 will be x
0001 10 0101; read 0101 -- 0101 will be y

; now check which is larger
0002 20 0100; load 0100
0003 32 0101; subtract 0101
0004 41 0007; branchneg 0007 -- if y is greater, branch to that case
0005 25 0100; store 0100 -- else x is greater, so store that as the new x
0006 40 0011; branch 00xx -- branch to the part that checks equality

; y is larger
0007 20 0101; load 0101 -- load y
0008 32 0100; subtract 0100 -- y is greater, so subtract x from it
0009 25 0101; store 0101 -- store the difference as the new y
0010 40 0011; branch 00xx -- branch to the part that checks equality

; check equality
0011 20 0100; load 0100 -- load x
0012 32 0101; subtract 0101 -- subtract y
0013 42 0015; branchzero 00xx -- if x == y, then x == y == GCD of both, so branch to display GCD
0014 40 0002; branch 0002 -- otherwise repeat the subtraction

; display GCD
0015 20 0100; load 0100 -- load x (now GCD)
0016 11 0100; write 0100 -- print x
0017 45 0001; halt 0001