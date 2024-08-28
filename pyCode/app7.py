# from this list [a,b,c,d] get output [a,a+b,a+b+c,a+b+c+d]

list = [5,6,7,2,1,3,7]
output_list = []
answer = 0

for i in list:
    answer = answer + i
    output_list.append(answer)

print(output_list)
