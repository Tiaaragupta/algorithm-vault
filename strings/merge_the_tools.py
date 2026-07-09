def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        temp = ""
        block = string[i:i+k]

        for ch in block:
            if ch not in temp:
                temp += ch

        print(temp)

    
