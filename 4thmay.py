class Solution:
    def findComplement(self, num: int) -> int:
        dec1=bin(num)[2:]
        binary=[]
        decimal=0
        j=0
        for i in range(len(dec1)):
            if(dec1[i]=='0'):
                binary.append('1')
            else:
                binary.append('0')
        binary=int(''.join(binary))
        j=0
    
        while(binary!= 0): 

            dec = binary% 10

            decimal = decimal + dec * pow(2, j) 

            binary = binary//10

            j += 1

        return decimal
        
