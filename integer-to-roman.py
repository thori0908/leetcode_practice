class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        while num != 0:

dict = {
    1:   I      
    4:   IV    
    5    V      
    9    IX    
    10   X     
    40    XL   
    50   L     
    90    XC   
    100   C    
    400   CD   
    500   D    
    900    CM  
    1000   M   
}

# 723 = 500 + 100 + 100 + 10 + 10 + 1 + 1 + 1 = DCCXXIII
# 724 = 500 + 100 + 100 + 10 + 10 + 4 = DCCXXIV
# num = num - roman_char
# while num != 0
-