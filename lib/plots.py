from datetime import datetime
import plotext as plt

def show_plots (bars,symbol):
    # 1. Reset the index so 'timestamp' becomes a normal column instead of an index
    plot_df = bars.df.reset_index()

    # 2. Format the timestamp into a standard string format that Plotext can handle
    # Using 'd/m/Y' matches the default expectation of many terminal plotters
    x_axis = plot_df['timestamp'].dt.strftime('%d/%m/%Y')
    y_axis = plot_df['close']

    # --- CHART CONFIGURATION ---
    plt.clear_data()

    # Use plt.date_form to tell Plotext exactly how to read the x_axis strings
    # Note: In Plotext, we use 'd/m/Y' without the '%' symbols
    plt.date_form('d/m/Y') 

    # Create the line chart
    # 'marker' adds dots at each data point, 'color' sets the line color
    plt.plot(x_axis, y_axis, marker="dot", color="green", label=f"{symbol} Close Price")

    # Add chart metadata
    plt.title(f"Price History: {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")

    # Enable the grid to make it easier to read prices in the terminal
    plt.grid(True)

    # --- FINAL RENDER ---
    return plt.show()

