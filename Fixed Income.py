import matplotlib.pyplot as plt
import numpy as np

# Pricing of a Bond
def Bond_Pricer(Coupon_Rate,r,Face_Value,n):
    Coupon = Coupon_Rate*Face_Value
    Price = 0
    for i in range(1,n+1):
        Price += (Coupon/((1+r)**i))
    Price += Face_Value/((1+r)**n)
    return Price

#Calculating the Duration
def Duration_Calculator(Coupon_Rate,r,Face_Value,n,Price):
    Coupon = Coupon_Rate*Face_Value
    Duration = 0
    for i in range(1,n+1):
        Duration += (i*Coupon)/((1+r)**i)
    Duration = (Duration + (n*Face_Value)/((1+r)**n))/Price
    return Duration 

#Calculating the Convexity
def Convexity_Calculator(Coupon_Rate,r,Face_Value,n,Price):
    Coupon = Coupon_Rate*Face_Value
    Convexity = 0
    for i in range(1,n+1):
        Convexity += (Coupon/((1+r)**i))*(i*(i+1)/((1+r)**2))
    Convexity += (Face_Value/((1+r)**n))*((n*(n+1))/((1+r)**2))
    Convexity /= Price
    return Convexity

#For testing
Coupon_Rate = 0.05
r = 0.03
Face_Value = 1000
n = 3

Price = Bond_Pricer(Coupon_Rate,r,Face_Value,n)
Duration = Duration_Calculator(Coupon_Rate,r,Face_Value,n,Price)
Convexity = Convexity_Calculator(Coupon_Rate, r, Face_Value, n, Price)


print(f'The bond Price is:  {Price:.2f}')
print(f'The duration of the bond is: {Duration:.2f}')
print(f'The convexity of the bond is: {Convexity:.2f}')


Prices = []
Interest_Rates = np.arange(0.01,0.16,0.01)

for i in Interest_Rates :
    Price = Bond_Pricer(Coupon_Rate, i, Face_Value, n)
    Prices.append(Price)
    
plt.plot(Interest_Rates, Prices, marker='.')
plt.title('Bond Prices vs Interest Rates') 
plt.xlabel('Interest Rates')
plt.ylabel('Bond Prices')  
plt.grid()
plt.show()