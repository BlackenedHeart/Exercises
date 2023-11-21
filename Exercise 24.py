def calculate_amount_excluding_vat():
    vat_rate = float(input("Enter the VAT rate as a decimal: "))
    amount_including_vat = float(input("Enter the amount including VAT: "))
    
    amount_excluding_vat = amount_including_vat / (1 + vat_rate)
    print(f"The amount excluding VAT is: {amount_excluding_vat:.2f}")

calculate_amount_excluding_vat()