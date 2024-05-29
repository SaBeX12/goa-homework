#1.მომხმარებელს შეეკითხეთ თუ რომელ პროგრამირების აკადემიაში სწავლობს. თუ პასუხი იქნება "GOA", დაუბეჭდეთ რომ სწორია. სხვა შემთხვევაში დაუბეჭდეთ, რომ არასწორი გადაწყვეტილება მიიღო.


#academy = input("გთხოვთ შემოიტანოთ იმ აკადემიის სახელი სადაც ამჟამად სწავლობთ: ")

#if academy == "GOA":
    #print("ჩადურ აკადემიაში სწავლობ!")
#else:
    #print("ლუსერულ აკადემიაში სწავლობ!")

#print(academy)



#2.მომხმარებელს შემოატანინეთ საყიდელი ნივთის ფასი და მისი ბიუჯეტი. თუ ბიუჯეტი აღემატება ან ტოლია საყიდელი ნივთის ფასის, დაუბეჭდეთ რომ თანხა ყოფნის. სხვა შემთხვევაში, დაუბეჭდეთ თუ რამდენი აკლდება საყიდლად.


#budget = int(input("Please enter your budget: "))
#price = int(input("Please enter price: "))

#if budget >= price:
#    print("You have enough money to buy thing")
#else:
#    print("You need", price - budget)


#3.დაწერეთ პროგრამა, რომელიც შეამოწმებს მომხმარებლის მიერ შემოტანილ რიცხვს. თუ რიცხვი მეტია ან ტოლი ხუთის, დაბეჭდეთ მისი ნამრავლი ორზე. სხვა შემთხვევაში დაბეჭდეთ მისი ნამრავლი ოთხზე.



#number = int(input("Please enter number: "))

#if number >= 5:
#    print(number * 2)
#else:
#    print(number * 4)


#4.თქვენს პროგრამაში ბილეთის ფასი იქნება 10 ლარი. მომხმარებელს შეეკითხეთ თუ რამდენი ბილეთის ყიდვა უნდა. თუ ეს რიცხვი ნაკლები იქნება 5-ზე, გამოუტანეთ ჩვეულებრივი შედეგი. სხვა შემთხვევაში ყოველ ბილეთზე გააკეთეთ 30%-იანი ფასდაკლება.


#ticket_price = 10
#ticket_count = int(input("Please enter how many tickets do you want to buy: "))

#if ticket_count < 5:
#    print(ticket_price * ticket_count)
#else:
#    discount = ticket_price - ((30 / 100) * ticket_price)
#    print(discount * ticket_count)



#5.შექმენით კალკულატორის პროგრამა, სადაც გექნებათ +, -, *, /. მომხმარებელს ჯერ შეეკითხეთ ორი რიცხვი, შემდეგ სასურველი ოპერაცია და ბოლოს დაუბეჭდეთ შედეგი.


#num2 = int(input("Please enter number2: "))

#operation = input("Please enter (+, -, * or /): ")

#if operation == "+":
   # print(num1 + num2)
#elif operation == "-":
    #print(num1 - num2)
#elif operation == "*":
    #print(num1 * num2)
#elif operation == "/":
    #print(num1 / num2)
#else:
#    print("Your operation is not valid")


academy = input("გთხოვთ შემოიტანოთ იმ აკადემიის სახელი სადაც ამჟამად სწავლობთ: ")

if academy == "GOA":
    print("ჩადურ აკადემიაში სწავლობ!")
else:
    print("ლუსერულ აკადემიაში სწავლობ!")

print(academy)



budget = int(input("Please enter your budget: "))
price = int(input("Please enter price: "))

if budget >= price:
    print("You have enough money to buy thing")
else:
    print("You need", price - budget)



number = int(input("Please enter number: "))

if number >= 5:
    print(number * 2)
else:
    print(number * 4)



ticket_price = 10
ticket_count = int(input("Please enter how many tickets do you want to buy: "))

if ticket_count < 5:
    print(ticket_price * ticket_count)
else:
    discount = ticket_price - ((30 / 100) * ticket_price)
    print(discount * ticket_count)



num1 = int(input("Please enter number1: "))
num2 = int(input("Please enter number2: "))

operation = input("Please enter (+, -, , or /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Your operation is not valid")
