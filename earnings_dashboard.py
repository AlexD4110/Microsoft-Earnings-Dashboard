import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

msft = yf.Ticker("MSFT")
income_stmt = msft.financials.T

# Display the income statement data
print(income_stmt)

# Extract relevant columns, such as Net Income, Total Revenue, etc.
relevant_data = income_stmt[['Net Income', 'Total Revenue', 'Operating Income']]

# Reset the index to include the dates in the data frame
relevant_data.reset_index(inplace=True)

# Save the data to a CSV file
relevant_data.to_csv('msft_earnings.csv', index=False)