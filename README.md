# 📈 Stock Visualize

> A lightweight CLI tool for viewing real-time and historical stock charts directly in your terminal.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Roadmap](#roadmap)
- [Configuration](#configuration)
- [License](#license)

---

## Overview

`stock_charts.py` is a terminal-based stock chart viewer for developers, traders, and power users who prefer to stay in the command line. Enter any valid stock ticker and get an instant ASCII/CLI chart without ever leaving your terminal.

---

## Features

- 📊 View stock charts for any ticker symbol directly in the CLI
- 🕐 Support for multiple intervals (Day, Week, Month, Year)
- ⚡ Fast and lightweight — no GUI or browser required
- 🔎 Historical data display
- 🛠️ Easy to extend and customize

---

## Requirements

- Python 3.13+
- pip or uv (Python package manager)

**Dependencies:**
```
alpaca-py>=0.43.2
dotenv>=0.9.9
pandas>=3.0.0
plotext>=5.3.2
pytz>=2025.2
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ghostnomad/stock_visualize
   cd stock_visualize
   ```

2. **Install dependencies:**

   Using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   Using [`uv`](https://github.com/astral-sh/uv) (faster alternative):
   ```bash
   # Install uv if you don't have it
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install dependencies
   uv pip install -r requirements.txt
   ```

   > 💡 `uv` is a fast Python package manager written in Rust. It's a drop-in replacement for `pip` and is significantly faster for dependency resolution and installation.

---

## Usage

Simply run the script and follow the interactive prompts:

```bash
python stock_charts.py
```

The tool will guide you through the options (such as ticker symbol and timeframe) directly in the terminal.

---

## Examples

**Start the tool:**
```bash
python stock_charts.py
```

```
Enter the stock ticker symbol (or type exit to quit): AAPL
Enter Interval (Min, Hour, Day, Week) [Q to Quit]: Day
```

---

## Roadmap

The following CLI argument support is planned for a future release:

| Flag              | Description                              | Default  |
|-------------------|------------------------------------------|----------|
| `--ticker`        | Stock ticker symbol (e.g., AAPL, TSLA)  | —        |
| `--timeframe`     | Chart timeframe (1d, 1w, 1m, 1y)        | `1m`     |
| `--interval`      | Data interval (1m, 5m, 1h, 1d)          | `1d`     |

Passing arguments directly will allow the tool to be used in scripts and automated workflows without interactive prompts.

---

## Configuration

Configuration is handled via a `.env` file in the project root. Create one based on the example below:

```
ALPACA_API_KEY=your_alpaca_api_key
ALPACA_SECRET_KEY=your_alpaca_secret_key
```

> ⚠️ Never commit your `.env` file to version control. Make sure `.env` is listed in your `.gitignore`.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- [alpaca-py](https://github.com/alpacahq/alpaca-py) — for market data and trading API access
- [plotext](https://github.com/piccolomo/plotext) — for terminal-based chart rendering
- [pandas](https://github.com/pandas-dev/pandas) — for data manipulation and analysis
- [pytz](https://pythonhosted.org/pytz/) — for timezone handling
- [dotenv](https://github.com/theskumar/python-dotenv) — for environment variable management

---

*Built for terminal lovers. 🖥️*