## Problem Statement ##
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

## My Python3 code ##

class Solution:
    def fizzBuzz(self, n):
        st = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0: #use i%15 directly...
                st.append('FizzBuzz')
            elif i%5==0:
                st.append('Buzz')
            elif i%3==0:
                st.append('Fizz')
            else:
                st.append(str(i))
        return st
        """
        :type n: int
        :rtype: List[str]
        """
        
        
