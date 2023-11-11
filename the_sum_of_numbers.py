N = int(input("Enter a number ->  "))
sum = 0
eqution = ""
count = 0

if N <= 0: 
    print("you should write positive numbers")
else: 
    count = 1 
    equation = "" 
    sum = 0 
    
    while count <= N: 
        equation += str(count) 
        sum += count 
        count += 1 
        if count <= N: 
            equation += " + " 
    print(sum) # 
    print(equation, "=", sum) # და ვპრინტავთ მოქმედებას
