def remove_character(word):
    for i in range (len(word)): 
        if i % 2 !=0:
            return (word[i])

print(remove_character("semicolon"))
