from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt

# Load the earnings data
earnings_df = pd.read_csv("msft_earnings.csv")

# Define the UI
app_ui = ui.page_fluid(
    ui.h2("Microsoft Earnings Dashboard"),
    ui.output_plot("revenue_plot")
)

# Define the server logic
def server(input, output, session):

    @output
    @render.plot
    def revenue_plot():
        plt.figure(figsize=(10, 6))
        plt.plot(pd.to_datetime(earnings_df['index']), earnings_df['Total Revenue'], color="blue")
        plt.title('Total Revenue Over Time')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        plt.grid(True)
        return plt.gcf()

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
