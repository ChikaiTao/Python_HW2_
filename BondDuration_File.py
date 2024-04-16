import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    number_of_payments = m * ppy
    discount_rates = (1 + y/ppy) ** np.arange(1, number_of_payments + 1)
    coupon_pv = np.sum(coupon_payment / discount_rates)
    face_pv = face / (1 + y/ppy) ** number_of_payments
    price = coupon_pv + face_pv
    return price

def getBondDuration(y, face, couponRate, m, ppy=1):
    bond_price = getBondPrice(y, face, couponRate, m, ppy)
    coupon_payment = face * couponRate / ppy
    number_of_payments = m * ppy
    time_periods = np.arange(1, number_of_payments + 1) / ppy
    discount_factors = (1 + y/ppy) ** time_periods
    pv_cash_flows = (coupon_payment / discount_factors)
    weighted_times = time_periods * pv_cash_flows
    pv_face_value = face / (1 + y/ppy) ** number_of_payments
    duration = (np.sum(weighted_times) + m * pv_face_value) / bond_price
    
    return duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

# Calculate the bond duration
bond_duration = getBondDuration(y, face, couponRate, m, ppy)
print(f"The bond duration is: {bond_duration} years")


def getBondDuration(y, face, couponRate, m, ppy = 1):
    return(8.51)