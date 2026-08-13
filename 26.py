def name(n,left,right):

    if left>=right:
        return True

    if n[left]!=n[right]:
        return False   

    return name(n,left+1,right-1)

print(name("madam",0,len("madam")-1))
