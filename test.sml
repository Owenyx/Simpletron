; test all errors and syntax

;can give franco a github url for submission

;*10100 ; read 100
 ;*1 1 10  0;; read
;000220 100; load it 

;*11 100 ; write it 
;*  -21 5 ; loadim -5
;*22 50 ; idx = 200
;* - 230000 ; acc = 51
;*25 0100 ; 0100 = 51
;*-43 000 ; acc = 200, idx = 51
;*26 ; 0051 = 200
;*11 51 ; print 200
;*30 50 ; acc = 400
;*26 52 ; 0051 = 400
;*11 51 ; print 400
;*31 ; acc = 800
;*25 49; 0025 = 800
;*11 49 ; print 800
;*32 50 ; acc = 600
;*25 49; store ^
;*11 49 ; print it

;*33 5 ; acc = 200
;*25 49; store ^
;*11 49 ; print it
;*34 5 ; acc = 0
;*25 49; store ^
;*11 49 ; print it
;* 30 50 ; acc = 200
;*36 50 ; acc = 40000
;*25 49; store ^
;*11 49 ; print it
;*45


;0050 200
;0200 51

;error test
; Test for Accumulator Overflow
0000    210000         ; LOADIM 1 into accumulator (ACC = 1)
*    300101         ; ADD memory at address 101, ACC += MEM[101] (this will cause accumulator overflow)
*43
*38


; Test for Divide by Zero
0005    210000         ; LOADIM 0 into accumulator (ACC = 0)
0006    340104         ; DIVIDE by memory at address 104 (MEM[104] = 0, this will cause divide by zero)

; Test for Address Out of Bounds (index error)
0007    220120         ; LOADX with address 120 (attempting to access out-of-bounds memory)
0008    450000         ; HALT, just to ensure a clear end of the program

; Test for Illegal Instruction Code
0009    990000         ; Invalid instruction code (990000 is not a valid opcode)

; Data Section (starting at address 100, far from instructions)
0100    000005         ; memory[100] = 5 (used for ADD instructions)
0101    999999         ; memory[101] = 999 (used for ADD that causes overflow)
0102    000010         ; memory[102] = 10 (used for DIVIDE test)
0103    000010         ; memory[103] = 10 (used for DIVIDE test)
0104    000001         ; memory[104] = 0 (used for DIVIDE by zero test)
0105    000000         ; filler data
0106    000000         ; filler data
0107    000000         ; filler data
0108    000000         ; filler data
0109    000000         ; filler data
0110    000000         ; filler data
0111    000000         ; filler data
0120    000000         ; memory boundary test (will trigger index out of bounds)