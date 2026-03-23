"""
Jeremy Francis
2026_02_17
Extra Credit | Compound Interest Formula
"""

def get_cif_info():
      principle_input = float(input("\nPlease enter the Principal (starting Amount): $"))
      rate_input = float(input("\nPlease enter the rate (Annual nominal interest rate as a decimal): "))
      number_periods_input = int(input("""\nPlease select compounding period:
(1) Daily
(2) Weekly 
(3) Biweekly
(4) Monthly
(5) Semimonthly
(6) Bimonthly
(7) Quarterly 
(8) Semiannually 
(9) Annually\n
"""))
      if number_periods_input == 1:
            number_periods_input = 365
      elif number_periods_input == 2:
            number_periods_input = 52
      elif number_periods_input == 3:
            number_periods_input = 26
      elif number_periods_input == 4:
            number_periods_input = 12
      elif number_periods_input == 5:
            number_periods_input = 24
      elif number_periods_input == 6:
            number_periods_input = 6
      elif number_periods_input == 7:
            number_periods_input = 4
      elif number_periods_input == 8:
            number_periods_input = 2
      elif number_periods_input == 9:
            number_periods_input = 1 
      else:
           print("\nInvalid choice. Please run the program again.")
           exit()
      time_input = float(input("\nPlease enter the time in months (Number of months): "))/12   
      return principle_input, rate_input, number_periods_input, time_input

def compound_interest():
      p,r,n,t = get_cif_info()
      calculated_interest = p*(1+r/n)**(n*t)
      print(f"\nYour calculated interest would be: ${calculated_interest}")
      return calculated_interest

# START OF PROGRAM
def main():
      compound_interest()

main()