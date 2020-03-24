s = "soskasososkakaso"
count=0
for n in range(len(s)):
    print(n)
    if s[n:n+2]=="so":
        count+=1
print("Number of times bob occurs is: " + str(count))

# s[1:len(s)]

