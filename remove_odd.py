def remove_odd(word):
    result = ""
    for i in range (len(word)): 
        if i % 2 !=0:
            result+=word[i]
    return result

print(remove_odd("semicolon"))
