from IPython.display import clear_output


cStore = {
    'milk':7.99,
    'bread':2.99,
    'water':1.99,
    'cheese':6.99,
    'cookies':2.99,
    'icecream':5.99,
    'toilet paper':11.99,
    'ceral':12.99,
    'frozen pizza':10.99,
    'chicken': 12.00,
    'beef':13.00,
    'fish':16.99,
    'juice':6.99
    
}

welcome = 'Welcome to cStore, Unfortunatly our inventory is limited today but what we have is good. '
cont = 'do you still want to continue? Y/N'
choose = 'please enter any item from the list, if you dont see it then we dont have it.'
choices = " ".join(cStore.keys()) 
addItem = 'would you like to add any other items?'
checkOut = 'are you ready to check out? Y/N'
total = 'your total is {shoppingCost}'
cart = 'shoppingCart'
salutation = 'thanks for shopping with with cstore, hope to see you again soon.'
noStock = " we are currently out of {choice}"
added = '{choice} has been added to your cart'
              
shoppingCart=[]
shoppingCost=[]



def cStoreCart():
    
    while True:
    
        print(welcome)
        print(choices)
        choice = input(choose)
        
    try:
        if choice in cStore:
            raise Exception(f"we dont sell {choice} here ")
            shoppingCart.append(choice)
            shoppingCost.append(cStore[choice])
            print(added.format(choice =choice))
            print(shoppingCart)
        elif choice not in  cStore:
            print(noStock.format(choice =choice))
    except: Exception as error:
        print(error)


        go = input(cont)
        if go == 'n':
            checkout = input(checkOut)

            if checkout == 'y':
                print(total.format(shoppingCost = sum(shoppingCost)))
                print(salutation) 
                break



cStoreCart()

            
            
        
        
        
        

    

    