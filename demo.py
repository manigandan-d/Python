def minion_game(data):
    data = data.strip()
    
    vowels = "AEIOU"
    
    stuart_score = 0
    kevin_score = 0
    
    length = len(data)

    for i in range(length):
        if data[i] in vowels:
            kevin_score += length - i
            
        else:
            stuart_score += length - i

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
        
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
        
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)