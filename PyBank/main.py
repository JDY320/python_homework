import pandas as pd
import numpy as np

budget_data = pd.read_csv('budget_data.txt')

dates = list(budget_data['Date'])
pnl = list(budget_data['Profit/Losses'])
total_months = len(dates)

def pnl_change(old_pnl,new_pnl):
    return new_pnl - old_pnl

daily_change = []

for i in range(0,len(pnl)-1):
    output = pnl_change(pnl[i],pnl[i+1])
    daily_change.append(output)

avg_change = round(sum(daily_change) / len(daily_change),2)

# insert a space to make columns equal length
daily_change.insert(0,'')

# create change df
change_df = pd.DataFrame({'Date':dates,'Change':daily_change})

# convert 'Change' to a numeric format
change_df['Change'] = pd.to_numeric(change_df['Change'])


change_df.loc[change_df['Change'].idxmax()]

max_change = change_df[change_df.Change == change_df.Change.max()]
min_change = change_df[change_df.Change == change_df.Change.min()]

print(f"Financial Analysis\n-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total PnL: ${sum(pnl)}")
print(f"Average Change: ${avg_change}")
print(f"Greatest increase in profits: \n{max_change}")

print(f"\nGreatest decrease in profits:\n{min_change}")



with open('pybank_output.txt', 'w') as f:
    f.write(f"Financial Analysis\n-------------------------------")
    f.write(f"\nTotal Months: {total_months}")
    f.write(f"\nTotal PnL: ${sum(pnl)}")
    f.write(f"\nAverage Change: ${avg_change}")
    f.write(f"\nGreatest increase in profits: \n{max_change}")
    f.write(f"\nGreatest decrease in profits:\n{min_change}")