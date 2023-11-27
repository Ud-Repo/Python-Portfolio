# Initial amount of fried chicken in pounds
total_fried_chicken = 20

# Amount of fried chicken eaten on day 1 in pounds
daily_consumption = 1

# Percentage increase in consumption each day
increase_percentage = 5 / 100

# Variable to keep track of the total days
days = 1

# Calculate the number of days until he runs out of fried chicken
while total_fried_chicken > 0:
    # Skip day 7 (stomach ache day)
    if days != 7:
        # Print the amount of fried chicken eaten and remaining for the current day
        print(f"Day {days}: Ate {daily_consumption:.2f} pounds, Remaining {total_fried_chicken:.2f} pounds")
        
        # Increase the daily consumption by 5% for the next day
        daily_consumption += daily_consumption * increase_percentage
        
        # Subtract the daily consumption from the total fried chicken
        total_fried_chicken -= daily_consumption
        
        # Round the values to 2 decimal places
        daily_consumption = round(daily_consumption, 2)
        total_fried_chicken = round(total_fried_chicken, 2)
    
    # Increment the day counter
    days += 1

# Output the total number of days it took to run out of fried chicken
print(f"Out of fried chicken on Day {days - 1}")
