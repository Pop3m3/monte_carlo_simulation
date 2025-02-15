import pytest
import json
from libs.strategies import monte_carlo_simulation

def load_test_parameters():
    with open('tests/test_parameters.json') as f:
        return json.load(f)

@pytest.mark.parametrize("test_case", load_test_parameters()["test_cases"])
def test_monte_carlo_simulation(test_case):
    balance, balances, results = monte_carlo_simulation(
        test_case["initial_balance"],
        test_case["risk_percentage"],
        test_case["win_rate"],
        test_case["reward_to_risk_ratio"],
        test_case["num_trades"],
        strategy=test_case["strategy"]
    )
    assert len(balances) == test_case["num_trades"] + 1  # initial balance + number of trades