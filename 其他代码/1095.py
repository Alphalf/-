n_list=list(input())
letter=[]
space=[]
number=[]
others=[]
for i in range(len(n_list)):
    if ord(n_list[i]) in range(65,91) or ord(n_list[i]) in range(97,123):
        letter.append(n_list[i])
    elif n_list[i]==' ':
        space.append(' ')
    elif ord(n_list[i]) in range(48,58):
        number.append(n_list[i])
    else:
        others.append(n_list[i])
print(len(letter))
print(len(space))
print(len(number))
print(len(others))
