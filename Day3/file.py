for i in range(2,4): # outer loop
    j = 0

    while j<=10: #inner loop
        j+=1
        if j == 4:
            break

        print(i*j,end=" ")
    print("")
    print("")    
