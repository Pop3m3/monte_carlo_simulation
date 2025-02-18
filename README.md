# Monte Carlo Simulation

This project implements a Monte Carlo simulation for trading strategies. The simulation allows you to input various parameters such as initial balance, risk percentage, win rate, reward-to-risk ratio, and the number of trades to simulate the performance of a trading strategy over a series of trades.

## Features

- Simulate trading strategies with customizable parameters
- Bilingual support (English and Persian)
- Visualize balance changes over trades using Matplotlib
- Export simulation results to an Excel file
- Export simulation results to a CSV file

## Requirements

- Python 3.12 or higher
- Matplotlib
- Pandas
- Openpyxl
- Arabic-reshaper
- Python-bidi
- Black
- Pylint
- Pre-commit
- Pydocstyle

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

3. Install pre-commit hooks:
   ```sh
   pre-commit install
   ```

4. Install `pydocstyle` manually:
   ```sh
   poetry add --dev pydocstyle
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

To export the results to a CSV file:
```sh
poetry run python src/main.py --lang en --strategy fixed --export-csv results.csv
```

## Code Formatting and Linting

This project uses `black` for code formatting, `pylint` for linting, and `pydocstyle` for docstring conventions. To format and lint your code, run the following commands:

To format the code:
```sh
black .
```

To lint the code:
```sh
pylint src/ libs/ tests/
```

To check docstring conventions:
```sh
pydocstyle src/ libs/ tests/
```

Pre-commit hooks are used to ensure code quality before committing changes. To run the pre-commit hooks manually, use:
```sh
pre-commit run --all-files
```

## Branch Name and Commit Message Conventions

This project enforces branch name styles and commit message conventions using `pre-commit` hooks and `commitizen`.

### Branch Name Convention

Branch names must follow the convention:
```
<type>/<description>
```
Where `<type>` is one of `feature`, `bugfix`, `hotfix`, or `release`, and `<description>` is a lowercase alphanumeric string with optional dots, underscores, or hyphens.

### Commit Message Convention

Commit messages must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification and include the author's initials.

To create a commit message, use:
```sh
cz commit --author-initials <initials>
```

To check the commit messages, use:
```sh
cz check
```

To bump the version based on commit messages, use:
```sh
cz bump
```

## Commitizen

This project uses Commitizen for conventional commits. To check your commit messages and bump the version, follow these steps:

### Check Commit Messages

To check if your commit messages follow the conventional commit format, run:

```bash
cz check
```

### Bump Version

To bump the version based on your commit messages, run:

```bash
cz bump
```

This will update the version in your project and create a new commit with the version bump.

## Parameters

- `initial_balance`: The initial trading balance.
- `risk_percentage`: The risk percentage per trade (as a percentage of the initial balance).
- `win_rate`: The win rate (e.g., 0.6 for 60%).
- `reward_to_risk_ratio`: The reward-to-risk ratio.
- `num_trades`: The number of trades.
- `num_simulations`: The number of simulations.
- `strategy`: The trading strategy to use (`fixed` or `variable`).
- `--export-csv`: Optional argument to specify the CSV file path to export the results.

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
