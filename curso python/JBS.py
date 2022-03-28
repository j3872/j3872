f=open('../twl06.txt')
    return [t[:-1] for t in f]
    
    n = int(input())
    
    if n == 1: 
        for t in f:  
            t = t[len(t[:-1])]
            sorted(t) = sort #syntaxerroroccurshere
        print(len(sort[-1])) 
