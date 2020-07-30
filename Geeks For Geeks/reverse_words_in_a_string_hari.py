# User function Template for python3

'''
	Your task is to reverse the string without reversing
	individual words and return the obtained string.

	Function Arguments: s (given string)
	Return Type: string
'''


def reverseWords(s):
    # code here
    w= s.split('.')
    w=w[::-1]
    x= ".".join(w)
    print(x,end="")
