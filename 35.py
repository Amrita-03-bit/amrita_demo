def vow(n,i,count,vowel):

    if i==len(n):
        return count

    if n[i]in vowel:
        count+=1

    return vow(n,i+1,count,vowel)

print(vow("education",0,0,"aeiou"))    