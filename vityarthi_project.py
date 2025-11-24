name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
gender = input("Enter your gender(M/F/O): ")
activity = input("Enetr your activity(sedentary/moderate/active/athlete): ")

if activity=="sedentary":
    protein = 1.0 * weight
    carbs = 3 * weight
    fats = 0.6 * weight
    calories = 28 * weight

elif activity=="moderate":
    protein = 1.3 * weight
    carbs = 4 * weight
    fats = 0.8 * weight
    calories = 30 * weight

elif activity=="active":
    protein = 1.6 * weight
    carbs = 5 * weight
    fats = 1.0 * weight
    calories = 33 * weight  

elif activity=="athlete":
    protein = 2.0 * weight
    carbs = 6.5 * weight
    fats = 1.2 * weight
    calories = 38 * weight

if gender=="M":
    vitamins = {"Iron": "8 mg", "Calcium": "1000 mg", "Vitamin C": "90 mg", "Vitamin D": "600 IU"}
elif gender=="F":
      vitamins = {"Iron": "18 mg", "Calcium": "1200 mg", "Vitamin C": "75 mg", "Vitamin D": "600 IU"}
else :
    vitamins = {"Iron": "10 mg", "Calcium": "1000 mg", "Vitamin C": "85 mg", "Vitamin D": "600 IU"}

bmi = round(weight / (height ** 2),2)
ideal_weight = round(22 * (height ** 2),2)
difference = round(weight - ideal_weight, 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

water_intake = (weight*0.033)

if 14 <= age <= 17:
    sleep = "8–10 hours"
elif 18 <= age <= 25:
    sleep = "7–9 hours"
else:
    sleep = "7–8 hours"

print("\n-------------------DAILY NUTRITION & HEALTH REPORT---------------------")
print(f"\nHello {name}, You Are Welcome to Our Daily Nutrition & Health Service!")

print(f"\nBMI:", {bmi,(category)})
print(f"Ideal Weight is: {ideal_weight}kg")
print(f"weight Difference: {difference}kg")
print(f"Protein Needed: {protein}g/day")
print(f"Carbohydrates Needed: {carbs}g/day")
print(f"Fats Needed: {fats}g/day")
print(f"Calories Required: {calories}Kcal/day")
print(f"Water Intake: {water_intake}L/day")
print(f"Sleep Needed: {sleep}")

print("\n----------------Vitamins & Mineral Recommendation---------------------")
for vitamin in vitamins:
    print(vitamin,":",vitamins[vitamin])

print(f"\nThank You,Take Care")
print(f"We are always available for your service.")

print("\n---------------------------------END-----------------------------------")
