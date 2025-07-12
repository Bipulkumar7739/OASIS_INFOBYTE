def calculate_bmi(weight, height):
    """formula."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_positive_float(prompt):
    """user a positive float value with input validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the BMI Calculator!\n")

    #input validation
    weight = get_positive_float("Enter your weight in kilograms (KG): ")
    height = get_positive_float("Enter your height in meters (M): ")
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    #results
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Health Category: {category}")

if __name__ == "__main__":
    main()