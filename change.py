def calculate_change(amount, fee_percentage):
    fee = amount * (fee_percentage / 100)
    remaining_amount = amount - fee
    return remaining_amount

def dispense_change(amount):
    dollar_units = [100, 50, 20, 10, 5, 1]
    change_units = [25, 10, 5, 1]
    coin_labels = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    dollars = int(amount)
    cents = round((amount - dollars) * 100)

    change_distribution = {'dollars': {}, 'cents': {}}
    
    for unit in dollar_units:
        if dollars >= unit:
            count = dollars // unit
            change_distribution['dollars'][unit] = count
            dollars -= unit * count
    
    for unit in change_units:
        if cents >= unit:
            count = cents // unit
            change_distribution['cents'][unit] = count
            cents -= unit * count
    
    return change_distribution, coin_labels

def main():
    amount = float(input("Enter the amount of change (e.g., 102.00): "))
    fee_percentage = float(input("Enter the fee percentage (1 or 2): "))

    remaining_amount = calculate_change(amount, fee_percentage)
    change_distribution, coin_labels = dispense_change(remaining_amount)
    
    print(f"Original amount: ${amount:.2f}")
    print(f"Fee percentage: {fee_percentage}%")
    print(f"Amount after fee: ${remaining_amount:.2f}\n")
    print("Change distribution:")
    print("Dollars:")
    for unit, count in change_distribution['dollars'].items():
        print(f"  ${unit}: {count}")
    print("Cents:")
    for unit, count in change_distribution['cents'].items():
        label = coin_labels[unit] if count == 1 else coin_labels[unit][:-1]
        print(f"  {label}: {count}")

if __name__ == "__main__":
    main()