def sort_divisions(number):#約数列挙
    i = 2
    front, back = [],[number]
    while i*i <= number:
        if number%i==0:
            front.append(i)
            if i!=number//i: back.append(number//i)
        i+=1
    return front+back[::-1]

num = 7
for i in range(1,12):
    num = num*10+7
    print(sort_divisions(num), num)