taxable_income = float(input("enter your salary"))
income_slabs = [300000, 600000, 900000, 1200000, 1500000]
tax_percentage = [0.05, 0.1, 0.15, 0.2, 0.3]
cumulative_tax = 0
tax=0
for i in range(0,len(income_slabs)):
    print(cumulative_tax)
    if taxable_income <= income_slabs[i]:
        if i > 0:
            tax = cumulative_tax + (taxable_income - income_slabs[i - 1]) * tax_percentage[i]
        else:
            tax = taxable_income * tax_percentage[i]
        break
    else:
        if i > 0:
            cumulative_tax = cumulative_tax + (income_slabs[i]-income_slabs[i-1])*tax_percentage[i]
        else:
            cumulative_tax = cumulative_tax + (income_slabs[i] * tax_percentage[i])
print("income tax:", tax)




