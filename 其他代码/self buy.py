# 在这里写上你的代码 :-)
print('''
1.milk[amounts:3;price:8]
2.soda water[amounts:5;price:6]
3.water[amounts:2;price:5]
''')
food={1:[3,8],2:[5,6],3:[2,5]}
id=int(input('Type the id of what you want to buy:'))
num=int(input('The amounts that you want:'))
pay=int(input('Please pay:'))
if id>=1 and id <=3:
    if num<=food[id][0]:
        money=num*food[id][1]
        if money>pay:
            print("Failed to make the deal:lack of money.")
        else:
            ret=pay-money
            print('What a great deal!{}returned!'.format(ret))
    else:
        print('The amount you typed was too large!')
else:
    print('Error!The goods you typed are not found.')
