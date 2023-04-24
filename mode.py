def main(a):
    max_value = 0
    counter = 0
    result = 0
    for i in range(0, len(a)):
        if max_value!=a[i]:
            count = 0 
            for j in range(0, len(a)):
                if i!=j and a[i]==a[j]:
                    count += 1
            if count>counter:
                counter += 1
        


                    



if __name__=="main":
    main()