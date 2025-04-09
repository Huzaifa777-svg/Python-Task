
purchase_amount=float(input("Enter The Purchase Amount: $"))
if purchase_amount>100:
    discount=purchase_amount*0.10
    final_price=purchase_amount-discount
else:
    final_price=purchase_amount 
#Display the final price
print(f"Final price after discount(ifapplicable): ${final_price:.2f}")#.2f dislay only 2 digits       