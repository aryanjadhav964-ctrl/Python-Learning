#casting 
##having some data in string format by payload need to convert it in their data type
#the data
base_price = "249"
surge_multiplier = "1.5"
delivery_distance_km = "4.0"
is_rain_surge_active = "False"
promo_code = ""

#casting data
base_price = int(base_price)
surge_multiplier = float(surge_multiplier)
delivery_distance_km = float(delivery_distance_km)
is_rain_surge_active = bool(is_rain_surge_active)
promo_code = bool(promo_code)

#testing
print(type(base_price))
print(type(surge_multiplier))
print(type(delivery_distance_km))
print(type(is_rain_surge_active))
print(type(promo_code))

print(base_price)
print(surge_multiplier)
print(delivery_distance_km)
print(is_rain_surge_active)
print(promo_code)