"""
Maruti Cars Showroom - Console Application
Simulates a car dealership: greets customer, recommends cars by budget,
shows car details, and finalizes purchase.
"""

# ---------- Data ----------
CARS = {
    "Alto K10":  {"price": 4.23, "features": ["Petrol engine", "Manual/Automatic", "Good mileage", "Compact design", "Keyless entry"]},
    "Celerio":   {"price": 5.64, "features": ["Best-in-class mileage", "SmartPlay studio", "AMT gearbox", "Central locking", "Engine start/stop button"]},
    "Wagon R":   {"price": 5.79, "features": ["Petrol/CNG", "Manual", "Power windows", "Android Auto/Apple CarPlay", "Better mileage"]},
    "Ignis":     {"price": 5.85, "features": ["Petrol engine", "Automatic climate control", "Rear camera", "Advanced infotainment", "Good mileage"]},
    "Eeco Cargo":{"price": 5.84, "features": ["Petrol/CNG", "Manual", "2-star rating", "2 seating capacity", "Average mileage"]},
    "Dzire Tour S": {"price": 6.82, "features": ["Petrol/CNG", "Manual", "Good mileage", "Airbags"]},
    "Swift":     {"price": 6.49, "features": ["Petrol/CNG", "Manual/Automatic", "Sporty design", "Dual airbags", "Wireless charger", "ABS"]},
    "Dzire":     {"price": 6.84, "features": ["Petrol/CNG", "Sedan comfort", "Touchscreen display", "5-star rating", "Parking sensors"]},
    "Baleno":    {"price": 6.70, "features": ["Petrol", "Manual", "Better mileage", "Advanced infotainment", "360-degree camera"]},
    "FRONX":     {"price": 7.54, "features": ["Petrol", "Manual", "5 seater", "360-degree camera", "Heads-up display"]},
    "Brezza":    {"price": 8.69, "features": ["Petrol", "Manual", "5 seater", "Cruise control", "4-star rating", "360-degree camera"]},
    "Ertiga":    {"price": 9.12, "features": ["Petrol", "Manual", "7 seater", "3-star rating", "Cruise control", "Paddle shifters"]},
    "Ciaz":      {"price": 9.41, "features": ["Petrol", "Manual", "Voice commander", "Adjustable steering", "Keyless entry", "Smart hybrid tech"]},
    "Swift ZXi Plus AMT DT": {"price": 9.64, "features": ["Petrol", "Automatic", "Larger boot space", "Better mileage"]},
    "Escudo":    {"price": 9.75, "features": ["Petrol/CNG", "Manual", "HUD", "Ventilated seats", "Lane keep assist", "Level 2 ADAS", "Launching soon"]},
    "Ertiga Tour": {"price": 10.18, "features": ["Petrol", "Manual", "7 seater", "3-star rating", "10+ colours available"]},
    "Grand Vitara": {"price": 11.42, "features": ["Petrol", "Manual", "5 seater", "6 airbags", "Panoramic sunroof", "FWD/AWD"]},
    "XL6":       {"price": 11.84, "features": ["Petrol", "Manual", "6 seater", "Connected car tech", "Rear charging sockets"]},
    "Jimny":     {"price": 12.76, "features": ["Petrol", "Manual", "4 seater", "4WD", "Low ratio gearbox"]},
    "Ertiga ZXi Plus AT": {"price": 13.40, "features": ["Petrol", "Automatic", "7 seater", "Child-safety lock", "Curtain airbags"]},
    "Brezza ZXi Plus AT": {"price": 13.98, "features": ["Petrol", "Automatic", "5 seater", "4-star rating", "Hill assist"]},
    "eVitara":   {"price": 17.0, "features": ["Electric", "Automatic", "Fast charging", "Eco/Normal/Sport modes"]},
    "Invicto":   {"price": 25.51, "features": ["Petrol", "Automatic", "5-star rating", "7-8 seater", "Strong hybrid powertrain"]},
    "Invicto Alpha Plus": {"price": 29.22, "features": ["Petrol", "Automatic", "7+ seater", "5-star rating", "Excellent mileage"]},
}

REFRESHMENTS = {
    "tea": "Here! your *tea* with some cookies. Please enjoy it.",
    "coffee": "Here! your *coffee* with some cookies. Please enjoy it.",
    "milk": "Here! your *milk* with some cookies. Please enjoy it.",
    "juice": "Here! your *juice*. Please enjoy it.",
}


# ---------- Functions ----------
def greet_and_offer_refreshment():
    print("------------------------------------")
    print("WELCOME!! TO MARUTI CARS SHOWROOM")
    print("------------------------------------")
    print("\nYour One Stop Destination For Quality & Trust.")
    print("Explore Our Latest Models, Test drive options, & offers.\n")

    choice = input("What would you like to have sir/madam (tea/coffee/milk/juice): ").strip().lower()
    print(REFRESHMENTS.get(choice, "\nOk sir/madam, if you need anything let me know."))
    print("\nOk, let's move on to the cars.")


def get_budget():
    while True:
        try:
            return float(input("\nEnter your car budget (in lakhs): ₹"))
        except ValueError:
            print("Please enter a valid number.")


def show_cars_in_budget(budget):
    matches = {name: info for name, info in CARS.items() if info["price"] <= budget}
    if not matches:
        print("Sorry, no cars available in this budget. Minimum budget is ₹4 lakhs.")
        return None

    print(f"\nCars available within ₹{budget} lakhs budget:")
    for name in matches:
        print(f"- {name} (₹{matches[name]['price']} lakh)")
    return matches


def show_car_details(car_name):
    car = CARS.get(car_name)
    if not car:
        print("Invalid car name. Please choose from the list shown above.")
        return None
    print(f"\nPrice: ₹{car['price']} lakh")
    print("Key features:")
    for feature in car["features"]:
        print(f"  - {feature}")
    return car


def finalize_purchase(car_name):
    choice = input("\nWould you like to buy this car? Let's finalize (yes/no): ").strip().lower()
    if choice == "yes":
        print("\nWe are including 3 years of warranty.")
        print("We provide free test drives for all cars.")
        print("We also have EMI options.")
        print("We are giving a free car cover, cleaning spray & brushes.")
        print("*********************************************")
        print(f"CONGRATS! You got our latest model: {car_name}")
        print("*********************************************")
        print("\n~~~~~~~~~~~~~~~\nTHANK YOU!!\n~~~~~~~~~~~~~~~")
        print("For selecting MARUTI Cars Company.")
        print("Enjoy your ride safely & happily!")
    else:
        print("\nOk, thank you for visiting our showroom. Hope you come again!")
    print("We'd appreciate it if you rated our showroom service on Google.")


def main():
    greet_and_offer_refreshment()
    budget = get_budget()
    matches = show_cars_in_budget(budget)

    if matches:
        car_name = input("\nEnter the car name you selected: ").strip()
        # allow case-insensitive matching against the dict keys
        matched_key = next((k for k in matches if k.lower() == car_name.lower()), None)
        if matched_key:
            show_car_details(matched_key)
            finalize_purchase(matched_key)
        else:
            print("Invalid input. That car isn't in the list for your budget.")


if __name__ == "__main__":
    main()
