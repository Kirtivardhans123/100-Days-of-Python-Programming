def life_in_weeks():
    # Get the current age from the user
    current_age = int(input("What is your current age? "))

    # Calculate the remaining time
    max_age = 90
    years_left = max_age - current_age
    weeks_left = years_left * 52  # 52 weeks in a year

    # Print the result using f-strings
    print(f"You have {weeks_left} weeks left.")
life_in_weeks()