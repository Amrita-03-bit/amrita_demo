def first_non_repeating(s):

    freq={}

    for i in s:
        if i in freq:
            freq[i]+=1

        else:
            freq[i]=1

    for j in freq:
       if freq[j]==1:

           return j
         

s = "aabbcdde"

print(first_non_repeating(s))