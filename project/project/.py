def remove(x):
    for i in x:
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            a=""
            a.append(i)
            print(a)
str=input()
remove(str)            