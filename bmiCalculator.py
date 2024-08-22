def calculateBmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        print("Error: Height cannot be zero.")
        return None

def classifyBmi(bmi):
    if bmi is None:
        return None
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Very overweight"

def main():
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        bmi = calculateBmi(weight, height)
        if bmi is not None:
            category = classifyBmi(bmi)
            print(f"Your BMI is {bmi:.2f} ({category}).")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
