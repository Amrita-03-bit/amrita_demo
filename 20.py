def count_vowels(s):
    vowels="aeiou"
    total_vowel=0

    for ch in s:
        if ch in vowels:
            total_vowel+=1

        

    return total_vowel        

s = "hello world"               
print(count_vowels(s))
