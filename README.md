# Monte Carlo Simulation

This project implements a Monte Carlo simulation for trading strategies. The simulation allows you to input various parameters such as initial balance, risk percentage, win rate, reward-to-risk ratio, and the number of trades to simulate the performance of a trading strategy over a series of trades.

## Features

- Simulate trading strategies with customizable parameters
- Bilingual support (English and Persian)
- Visualize balance changes over trades using Matplotlib
- Export simulation results to an Excel file

## Requirements

- Python 3.12 or higher
- Matplotlib
- Pandas
- Openpyxl
- Arabic-reshaper
- Python-bidi

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/xx/monte_carlo_simulation.git
   cd monte_carlo_simulation
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

## Usage

Run the simulation with the following command:
```sh
poetry run python src/main.py --lang en --strategy fixed --show-plot
```

To run the simulation in Persian:
```sh
poetry run python src/main.py --lang fa --strategy variable --show-plot
```

## Parameters

- `initial_balance`: The initial trading balance.
- `risk_percentage`: The risk percentage per trade (as a percentage of the initial balance).
- `win_rate`: The win rate (e.g., 0.6 for 60%).
- `reward_to_risk_ratio`: The reward-to-risk ratio.
- `num_trades`: The number of trades.
- `num_simulations`: The number of simulations.
- `strategy`: The trading strategy to use (`fixed` or `variable`).

## Example

```sh
poetry run python src/main.py --lang en --strategy fixed --show-plot
```

Follow the prompts to enter the parameters and view the results.

## Project Structure

```
monte_carlo_simulation/
├── libs/
│   ├── __init__.py
│   └── strategies.py
├── src/
│   └── main.py
├── tests/
│   ├── test_parameters.json
│   └── test_simulation.py
├── pyproject.toml
└── README.md
```

## License

This project is licensed under the MIT License.
