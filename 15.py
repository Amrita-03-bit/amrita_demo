def calculate_bill(name,amount, discount=10, tax=5):

    dicount_amount=0
    discount_amount=amount*discount/100
    after_dicount=0
    after_discount=amount-discount_amount
    tax_amount=0
    tax_amount=after_discount *tax/100
    final_amount=0
    final_amount=after_discount+tax_amount

    return name,final_amount

print(calculate_bill("aditya",10000))
print(calculate_bill("palka",10000,20,10))


    