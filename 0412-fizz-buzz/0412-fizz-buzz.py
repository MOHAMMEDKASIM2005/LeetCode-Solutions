class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l1=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                l1.append("FizzBuzz")
            elif i%5==0:
                l1.append("Buzz")
            elif i%3==0:
                l1.append("Fizz")
            else:
                l1.append(str(i))
        return l1
        
        