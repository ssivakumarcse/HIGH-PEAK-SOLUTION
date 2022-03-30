def fun(d,n):
    #sort the dictionary based on values
    if (n<=0 or n>=len(d)):
        print("Goodies cant be distributed based on given condition")
        exit()
    a = sorted(d.values())
    print(a)
    min1 = 999999
    i = 0
    j = n-1
    #get minimum diffrence
    while (i <= (len(a) - (n-1)) and j < len(a)):
        if (abs(a[i] - a[j]) <= min1):
            l = []
            min1 = abs(a[i] - a[j])
            p = i
            q = j
        i += 1
        j += 1
    res = {}
    for i in d.keys():
        if d[i] in a[p:q + 1]:
            res[i] = d[i]
    #return the resultant dictionary and minimum diffrence
##    print(res,min1)
    return (res,min1)

def filewrite(d,diff):
    s = "The goodies selected for distribution are:" + "\n" + "\n"
    for i in d:
        s += i + ": " + str(d[i]) + "\n"
    s += "\n" + "And the difference between the chosen goodie with highest price and the lowest price is " +str(diff)
    f=open("sample_output.txt","w")
    f.write(s)
    print(s)
    f.close()


myfile = open("sample_input.txt","r") #Opening file
a1=myfile.readline()
l=a1.split(": ") #Number of emloyees
n=int(l[1])
a1=myfile.readline()
a1=myfile.readline()
a1=myfile.readline()

d={} #Extracting input values from file to dictionary
for i in range(10):
    a1=myfile.readline()
    a=a1.split(": ")
    d[a[0]]=int(a[1])
d,diff=fun(d,n)
filewrite(d,diff)





