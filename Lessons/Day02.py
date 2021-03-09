# cost = int(input('Cost: '))

# calculate tax cost
# tax = cost * 0.08

# calculate tip cost
# tip = cost * 0.1

# calculate total cost
# totalCost = cost + tax + tip

# print total cost
# print('The tax is' , str(tax)  , 'Tip is' , str(tip) , 'Total cost is' , totalCost)


# Lists

# Crate List
# list = ['3', '6', '12', 3, '12', '12']
# list[2] = 'Python Must Go On'

# list.append('Hello')
# list.append('World')

# find index of value
# print(list.index('6'))

# count how many times in list
# print(list.count('12'))

# remove value from list
# list.remove('World')

# sorting values
# sortableList = [87, 3, 68, 99, 12, 44, 1, 4, 22]
# sortableList.sort()
# print(sortableList)
# sortableList.reverse()
# print(sortableList)

# extend list
# sortableList.extend(list)
# print(sortableList)

# range
# numbers = list(range(8))
# numbers = list(range(1, 5))
# numbers = list(range(1, 50, 4))

# numbers[2:5] = [2, 5, 6]

# print(numbers * 5)

# list2 = [[1,2],3,5,6]
# print(list2[0][1])


# if condition
print('HOŞGELDİNİZZZZ!')
userName = 'Semih'
password = 'hello123'

inputUserName = input('Kullanıcı Adınızı Giriniz: ')
inputPassword = input('Şifrenizi Giriniz:')

if userName != inputUserName and password == inputPassword:
    print('Kullanıcı adınız hatali')
elif userName == inputUserName and password != inputPassword:
        print('Şifre Hatalı')
elif userName == inputUserName and password == inputPassword:
        print('Tebrikler Giriş Yaptınız')
