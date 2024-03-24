#write a program to check the on road price for a bike
#under the conditions if the price is greater than 72000 and less than 150000 then income takes 10%  and insurance will be 15% 
#if the price is greater than 1,50,000 and less than 2,00,000 the tax would be 25% and insurance will be 20%
#if the price is above 2,00,000 then tax would be 35% and insurance will be 28%
#otherwise enter a valid price
#print on road price
actual=int(input("enter the price of the bike:"))
if actual>=72000 and actual<=150000:
    income_tax=actual*(10/100)
    insurance=actual*(15/100)
    on_road_price=actual+income_tax+insurance
    print("on road price of the bike is ",on_road_price)
elif actual>150000 and actual<=200000:
    income_tax=actual*(25/100)
    insurance=actual*(20/100)
    on_road_price=actual+income_tax+insurance
    print("on road price of the bike is ",on_road_price)
elif actual>200000:
    income_tax=actual*(35/100)
    insurance=actual*(28/100)
    on_road_price=actual+income_tax+insurance
    print("on road price of the bike is ",on_road_price)
else:
    print("bike rate starts from 72000 so please enter a valid price")
