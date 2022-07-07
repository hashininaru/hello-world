# eg.2.0.1 sorted with key, via def
v = ['Alice', 'Bob', 'Eve', 'Mallory']
def sort_key(x):
    return len(x)
print(sorted(v, key=sort_key))


# eg.2.0.2 sorted with key, via lambda
v = ['Alice', 'Bob', 'Eve', 'Mallory']
print(sorted(v, key = lambda v: len(v)))


# eg. 2.1 explain range()
def explain_range(n, s=0,step=1):    
    if s==0:  # input end only
        end = n
        i=s
    else:   # input start, end
        start = n
        end = s
        i=start
    while i < end:
        yield i
        i += step
print(list(explain_range(9)))
print(list(explain_range(2,9)))
print(list(explain_range(2,9,3)))


# eg.2.2.1 varargs sum_all(*numbers) 
def sum_all(*numbers):
    s=0
    for n in numbers:
        s=s+n
    return s
print(sum_all())
print(sum_all(1,-2,-3,6,7))


# eg.2.2.2 kwargs inventory(**items)
def inventory(**items):
    for item in items:
        print(f'{item}: {items[item]}', end = '; ')
print(inventory(stone=10, copper=4, iron=6, silver=2, gold=1, wood=100))


# eg.2.2.3 samples(*numbers, **kwargs)
def samples(*numbers, **kwargs):    # samples(v1,v2,v3,v4,..., k=vk)
    # kwargs={'k':vk}
    # numbers=(v1,v2,v3,v4,...)    
    if kwargs =={}:
        step=1
    else:  
        step = kwargs['k']        
    L=[] 
    turn = 0
    for n in numbers:
        turn += 1
        if turn % step == 0:
            L.append(n)
    return L
print(samples(1, 2, 3, 4, 5, 6, 7, k=2))
print(samples(0, 1, 0, 1, 0, 1, 0, 1, 0, k=3))
print(samples(0, 1, 0, 1, 0, 1, 0, 1, 0, k=10))
print(samples(1, 2, 3, 4, 5, 6, 7))


# eg. 2.3 min_max([])
def min_max(numbers):
    if len(numbers) == 0:
        return None, None
    minimum, maximum = numbers[0], numbers[0]   
    for x in numbers:
        if x < minimum:
            minimum = x       
        if maximum < x:
            maximum = x         
    return minimum, maximum
Number_list=[1,43,4,8,15]
x, y = min_max(Number_list)  # tuple
print(x, y)


# eg. 2.4.1 Calculate 1+2+ … +N via for loop
def series_sum(N):
    sum = 0
    for k in range(N+1):
        sum += k
    return sum
print(series_sum(100))


# eg. 2.5.1 Fibonacci Via Iteration (while loop)
def fibonacci(n):
    terms=[0,1]
    k=2
    while k <= n:                             
        terms.append(terms[k-1]+terms[k-2]) 
        k = k+1
    return terms[n]
print(fibonacci(10))


#  eg. 2.5.2 Fibonacci Via Recursion
def fibonacci(n):
    if n==0 or n==1:    #i.e. n<2
        return n
    else:                #i.e. n >= 2
        return (fibonacci(n-1)+fibonacci(n-2)) 
print(fibonacci(10))


# eg. 2.6.1 n! via Iteration (for loop)
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
print(factorial(5))


# eg. 2.6.2 n! via Recursion
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


# eg. 2.7 Guess a number on [1, 100]
import random
answer = random.randint(1, 100)
n = int(input('Guess a number: '))
while n != answer:
    if n > answer:
        print('Too high!')
        n = int(input('Guess a number: '))
    if n < answer:
        print('Too low!')
        n = int(input('Guess a number: '))
print('Bingo!')


#  eg. 2.8 Sort a list
def insertion_sort(list):
    for index in range(1, len(list)):
        value=list[index]
        i=index-1
        while  (i>=0) and (value<list[i]):
                list[i+1]=list[i]
                list[i]=value
                i=i-1
    return
alist = [33,4,8,35,8,6]
insertion_sort(alist)
print(alist)


# eg. 2.9.1 Identify prime number
def is_prime(x):
    '''int x >=0 '''
    if x <=1:
        return None
    else:
        result = 1
        for n in range(2, x):
            result *= (x % n)
        if result != 0:
            return True    # x is a prime number
        else:
            return False   # x is a composite number
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(5))
print(is_prime(10))


# eg. 2.9.2 Find primes on [0, N]
def primes(N):
    pl = []
    for k in range(N+1):
        if is_prime(k) == True:
            pl.append(k)
    return pl
print(primes(100))




# Major Example: construct a rational class

import numpy as np

class rational():
    """A class for arithmetic with rational numbers.
       
       Parameters
       ----------
       num, den: int
       
       Methods
       -------
       gcd()                : returns integer
       continued_fraction() : returns list of integers
       reduce()             : reduces by gcd()
       reciprocal()         : inverts a fraction
       
       All other methods are standard magic methods: 
           int, float, abs, max, min
           + , - , *, /, //, %,  ** , == , != , > , >= , < , <= 
       
       """
    
    def __init__(self,num=0,den=1):
        
        if den == 0: 
            raise ValueError('Undefined: zero denominator.')
        if den <  0: 
            num, den = -num, -den
        
        if isinstance(num,rational) or isinstance(den,rational): 
            num /= den
            num, den = num.num, num.den
        
        if isinstance(num,float) or isinstance(den,float):
            a, b = self._parse_float(num)
            c, d = self._parse_float(den)
            num, den = a*d, b*c
        
        self.num     = int(num)
        self.den     = int(den)
        self.reduce()
    
    def _parse_float(self,x):
    # This is only to be used internally. 
    
        s = str(x)
        p, e =s.find('.'), s.find('e')

        if (p == -1) and (e == -1): 
            return int(x), 1
        
        if e == -1: 
            den = 10**len(s[p+1:])
            s=reversed(s[:p]+s[p+1:])
            num = sum(int(d)*10**i for i, d in enumerate(s))
            return num, den
            
        num, den = self._parse_float(s[:e])
        
        if s[e+1] == '-':
            den *= 10**int(s[e+2:])
            return num, den

        if s[e+1] == '+':
            num *= 10**int(s[e+2:])
            return num, den

        num *= 10**int(s[e+1:])
        return num, den
    
    # self.gcd()
    def gcd(self):
        n, d = self.num, self.den
        while (d > 0): n, d = d, n%d
        return n
    
    # self.continued_fraction()
    def continued_fraction(self):
        n, d = self.num, self.den
        L = []
        while (d>0):
            L += [n//d]
            n, d = d, n%d
        return L

    # self.reduce()
    def reduce(self):
        n = self.gcd()
        self.num, self.den = self.num//n, self.den//n
    
    # str(self)
    def __str__(self): 
        if self.den == 1: 
            return str(self.num)
        return '%i/%i' % (self.num, self.den)
    
    # self
    def __repr__(self): 
        return str(self)
    
    # float(self)
    def __float__(self): 
        return self.num/self.den
    
    # int(self)
    def __int__(self): 
        return self.num//self.den
    
    # self + other
    def __add__(self,other):
        
        if isinstance(other,float):
            return other + float(self)

        if isinstance(other,np.ndarray):
            return other + self

        if isinstance(other,int):
            other = rational(other)
            
        a, b = self.num,  self.den
        c, d = other.num, other.den
        return rational(a*d+b*c,b*d)
    
    # -self
    def __neg__(self): 
        return rational(-self.num,self.den)
    
    # +self
    def __pos__(self): 
        return self
    
    # abs(self)
    def __abs__(self): 
        return rational(abs(self.num),abs(self.den))
    
    # self - other
    def __sub__(self,other): 
        return self + (-other)
    
    # self * other
    def __mul__(self,other):
        
        if isinstance(other,float):
            return other * float(self)

        if isinstance(other,np.ndarray):
            return other * self

        if isinstance(other,int):
            other = rational(other)
            
        a, b = self.num,  self.den
        c, d = other.num, other.den
        return rational(a*c,b*d)
    
    # # self**n
    def __pow__(self,n):
        if isinstance(n,float): 
            return float(self)**n

        if n == 0: 
            return rational(1)

        if n  > 0: 
            return self*(self**(n-1))

        return self*(self.reciprocal()**(1-n))
    
    # 1/self
    def reciprocal(self): 
        return rational(self.den,self.num)
    
    # self / other
    def __truediv__(self,other):
        
        if isinstance(other,float):
            return float(self)/other

        if isinstance(other,np.ndarray):
            return 1/(other/self)

        if isinstance(other,int):
            other = rational(other)
        
        return self*other.reciprocal()
    
    # self // other
    def __floordiv__(self,other): 
        return int(self/other)
    
    # self % other
    def __mod__(self,other): 
        return self - other*(self//other)
    
    # man(self,other)
    def __max__(self,other): 
        if self > other: 
            return self
        return other
    
    # min(self,other)
    def __min__(self,other): 
        if self < other: 
            return self
        return other
    
    # self == other
    def __eq__(self,other):

        if isinstance(other,int): 
            other = rational(other)

        if isinstance(other,float): 
            return float(self) == other

        return self.num*other.den == self.den*other.num
    
    # self != other
    def __ne__(self,other): 
        return not (self == other)
    
    # self < other
    def __lt__(self,other):

        if isinstance(other,int): 
            other = rational(other)

        if isinstance(other,float): 
            return float(self) < other

        return self.num*other.den < self.den*other.num
    
    # self <= other
    def __le__(self, other): 

        if isinstance(other,int): 
            other = rational(other)

        if isinstance(other,float): 
            return float(self) <= other

        return self.num*other.den <= self.den*other.num
    
    # self > other 
    def __gt__(self,other):

        if isinstance(other,int):
            other = rational(other)

        if isinstance(other,float):
            return float(self) > other

        return self.num*other.den > self.den*other.num
    
    # self >= other
    def __ge__(self,other):

        if isinstance(other,int):
            other = rational(other)

        if isinstance(other,float):
            return float(self) >= other
            
        return self.num*other.den >= self.den*other.num
    
    # other + self
    def __radd__(self, other): 
        return self + other
    
    # other - self
    def __rsub__(self,other): 
        return -self + other
    
    # other*self 
    def __rmul__(self, other): 
        return self * other
    
    # other/self
    def __rtruediv__(self,other): 
        if isinstance(other,float): 
            return other/float(self)
        return (self/other).reciprocal()
    
    # other//self
    def __rfloordiv__(self,other): 
        return int(other/self)
    
    # other % self
    def __rmod__(self,other): 
        return - self*(other//self) + other
    
    # max(other,self)
    def __rmax__(self,other): 
        return max(self,other)
    
    # min(other,self)
    def __rmin__(self,other): 
        return min(self,other)
    
    # other == self
    def __req__(self,other): 
        return self == other
    
    # other != self
    def __rne__(self,other): 
        return self != other
    
    # other > self
    def __rgt__(self,other): 
        return self <  other
    
    # other >= self
    def __rge__(self,other): 
        return self <=  other
    
    # other < self
    def __rlt__(self,other): 
        return self >  other
    
    # other <= self
    def __rle__(self,other): 
        return self >=  other
