python_p = 499
python_l_price = 855
ds_price = 645
gst = 12/100
delivery_charges = 250
book1 = int(input("Enter number of python programming books yoy want : "))
book2 = int(input("Enter number of python libraries cookbooks  yoy want : "))
book3 = int(input("Enter number of data science in  python  books yoy want : "))
total_price = book1*python_p + book2*python_l_price + book3*ds_price
total_invoice_amount =total_price + total_price * gst + delivery_charges
print("Total invoice amount = ",total_invoice_amount)
#total invoice amount
