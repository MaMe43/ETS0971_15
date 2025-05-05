car_prices = {
    "MARCEDES": 20000,
    "AUDI": 30000,
    "JETURE": 45000
}

price_of_BMW = car_prices.get("BMW")
print("Price of BMW:", price_of_BMW)
price_of_FORD = car_prices.get("FORD")
print("price of FORD :", price_of_FORD)
price_of_truck = car_prices.get("truck", "Not available")
print("Price of truck:", price_of_truck)
