
# function to calculate number of prime numbers in a range
def prime_freq(n):
    count = 0        
    if n < 2 :
        return count
    else:
        for num in range(3,n):   
            
            # 2 is excluded in the above range because here i already set flag = False , which goes as a default value for 2. hence 2 is already counted according to conditon in line 14
            flag = False
            for i in range(2,num//2):       # checking for prime numbers
                if num % i == 0:
                    flag = True
            if flag == False:
                count += 1
    return count

n = int(input("Enter the value of n: "))
print(prime_freq(n))

