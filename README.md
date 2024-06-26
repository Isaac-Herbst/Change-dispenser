# Change Dispenser Program

## Overview
The Change Dispenser program calculates the remaining amount after deducting a specified fee from a given amount of money. It then provides the change using the fewest possible number of dollar bills and coins. This program is particularly useful for cash handling systems, financial applications, and any scenario where precise change calculation and dispensing are required.

## Features
- Calculates remaining amount after applying a 1% or 2% fee.
- Dispenses change using the fewest number of bills and coins.
- Supports dollar denominations of $1, $5, $10, $20, $50, and $100.
- Supports coin denominations of 1¢ (pennies), 5¢ (nickels), 10¢ (dimes), and 25¢ (quarters).

## Usage
1. **Enter the amount of change**: Provide the total amount of money you need to dispense change for (e.g., `100.00`).
2. **Enter the fee percentage**: Choose either 1% or 2% fee to be deducted from the total amount.

### Example
```plaintext
Enter the amount of change (e.g., 100.00): 569.12
Enter the fee percentage (1 or 2): 2

Original amount: $569.12
Fee percentage: 2.0%
Amount after fee: $557.74

Change distribution:
Dollars:
  $100: 5
  $50: 1
  $5: 1
  $1: 2
Cents:
  quarters: 2
  dimes: 2
  pennies: 4
```

## Planned Additions
- Full, working GUI
- Make an executable, rather than a python script

## Known Issues
- Fee calculation rounds to the nearest cent, when it should be floored
- No restrictions on the input (eg, the percentage could be `100`, and no change would ever return)
- `quarter` should be `quarters`

## How to run
1. Clone the Repository:
```plaintext
git clone 
https://github.com/Isaac-Herbst/change-dispenser.git
cd change-dispenser
```

2. Run the Program:
Use Python to run the script: `python change.py` (or: `py -m change`)

## Dependencies
- Python 3.X

Make sure Python is installed on your machine. You can download it from [python.org](python.org).