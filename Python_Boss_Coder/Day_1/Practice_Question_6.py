# Calculate the compound interest for a given principal amount, interest rate, and time period
# formula = [ci = (p(1 + r/100)^ t) - p]
# ci = compound interest, p = princiapl, r = rate of interest, t = time.

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

amount = principal * (pow((1 + rate/100), time))
ci = amount - principal

print(f"Coumpound Interest is {ci}.")
