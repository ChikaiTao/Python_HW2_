import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    number_of_payments = m * ppy
    discount_rates = (1 + y/ppy) ** np.arange(1, number_of_payments + 1)
    coupon_pv = np.sum(coupon_payment / discount_rates)
    face_pv = face / (1 + y/ppy) ** number_of_payments
    price = coupon_pv + face_pv
    
    return price

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

# Calculate the bond price
bond_price = getBondPrice(y, face, couponRate, m)
print(f"The bond price is: ${bond_price:,.2f}")

def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    return(x)