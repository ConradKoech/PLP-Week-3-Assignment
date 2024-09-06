#creating a function called calculate_discount
def calculate_discount(price, discount_percent) :
     
#creating a condition for the discount price depending on price 
    if discount_percent >= 20:
        
         new_price = price * (1 - discount_percent/100)
         return new_price
           
    else:
        return original_price
       
 #ask user for input       
discount_percent = float(input("Enter the discount percent: "))
original_price = float(input("Enter the original price: "))

new_price = calculate_discount(original_price, discount_percent)   

#print the new_price

if discount_percent >=20:
    print(f"The new price after applying discount is: {new_price:.2f} ") 
    
else:
    print(f"No discount is applied. Price remains unchanged: {original_price:.2f}") 
  
  