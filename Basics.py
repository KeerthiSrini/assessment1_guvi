# First Program
print("Hello World!!!")

#numbers 
x=1      # -->integer
y=1.0    # -->float
z=1j     # -->complex
a=float(x)
b=int(y)
c=complex(x)
d=complex(y)
print(a,b,c,d)

#math functions
e=10
f=20
#add
g=e+f
print("addition", g)
#sub
h=e-f
print("addition", h)
#mul
i=e*f
print("addition", i)
#div
j=e/f
print("addition", j)
#modlus
k=e%f
print("addition", k)
#exponential
l=e**f
print("addition", l)
#floor division
m=e//f
print("addition", m)

#variables
"""
    the variables should start with underscore or alphabets, number can be user any where in the words rather than 
    starting letter of the variable name
"""
value1=5
value2="String"
value3=3.8
print(value1,value2,value3)
value1=value2
print(value1)
n=6
N=7
print(n,N) #python is case sensitive
_o=90.0 
print(_o)
req1, req2, req3 = "1", "2", "3"  #many variable can declared in single line
print(req1,req2,req3)

# multiple string
statement1="""Python 
is
an
Interpreter
Language"""
statement2='''Python 
is
Portable'''
print(statement1, statement2) # with mulitiple comment line qoutes we can able to print the strins as the request we are giving
p="Don't let me alone , Please I beg you"
# uppercase and lowercase
print(p.lower())
print(p.upper())
print(p[10])  # print a single element of the string
# slicing the string with the index values
print(p[20:26])  
print(p[:26])
print(p[28:])
print(p[-3:-1])
# length of string
print(len(p))  
# check the existence of words or letter
print("me" in p)
print("my" in p)
# replace string
print(p.replace("beg", "need"))
# spliting string
print(p.split(" "))
#concat string
q='hello'
r='python  '
s=r.strip()
print(r, s)
print(q+" "+s)
print(q,s)