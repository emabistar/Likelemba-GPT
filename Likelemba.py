
def calculate_loan(people, amount, position):
    position = int(position)
    people = int(people)
    amount = int(amount)

    results = []
    for i in range(1, people + 1):
        # Calculate the loan for each user
        loan = amount * (people - i)

        # Calculate the investment for each user
        invest = (i - 1) * amount

        # Calculate the profit based on the initial investment
        profit = invest * 0.10
        adjusted_invest = invest + profit

        # Adjust the loan based on profit
        adjusted_loan = loan - loan * 0.10

        # Calculate the total result for each user
        result = adjusted_invest + adjusted_loan

        results.append((result, loan, adjusted_invest))

    return results

# Function to print colored text
def print_colored(text, color):
    colors = {
        'green': '\033[92m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

# Example usage
people = int(input("Enter the number of people: "))
amount = int(input("Enter the amount: "))

for position in range(1, people + 1):
    user_results = calculate_loan(people, amount, position)
    print(print_colored(f"Iteration {position} (User {position}):", 'green'))
    for i, user_result in enumerate(user_results, 1):
        result, loan, adjusted_invest = user_result
        if position == i:
            print(print_colored(f"User {i}:", 'green'))
            print(print_colored(f"Result: ${result}", 'green'))
        else:
            print(f"User {i}:")
            print(f"Result: ${result}")
        print(f"Loan: ${loan}")
        print(f"Adjusted Investment: ${adjusted_invest}")
        print()
