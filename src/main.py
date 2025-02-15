import random
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import arabic_reshaper
from bidi.algorithm import get_display
import time

def monte_carlo_simulation(initial_balance, risk_percentage, win_rate, reward_to_risk_ratio, num_trades, strategy="fixed"):
    balance = initial_balance
    balances = [balance]
    results = []

    for trade in range(1, num_trades + 1):
        if strategy == "fixed":
            risk_amount = risk_percentage / 100 * initial_balance
        elif strategy == "variable":
            risk_amount = risk_percentage / 100 * balance
        else:
            raise ValueError("Unknown strategy")

        reward_amount = reward_to_risk_ratio * risk_amount

        if random.random() < win_rate:
            balance += reward_amount
            result = "Win"
            amount = reward_amount
        else:
            balance -= risk_amount
            result = "Loss"
            amount = -risk_amount

        results.append({
            'Trade Number': trade,
            'Result': result,
            'Change in Balance': amount,
            'New Balance': balance
        })
        balances.append(balance)

    return balance, balances, results

def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

def plot_results(all_balances, initial_balance, prompts):
    plt.figure(figsize=(10, 5))
    for balances in all_balances:
        plt.plot(balances, marker='o', alpha=0.5)
    plt.title(prompts["plot_title"])
    plt.xlabel('Number of Trades')
    plt.ylabel('Balance')
    plt.grid(True)
    plt.axhline(initial_balance, color='red', linestyle='--', label=prompts["initial_balance_label"])
    plt.legend()
    plt.show(block=False)  # Non-blocking show
    time.sleep(1)  # Small delay to ensure the plot window renders

def main():
    parser = argparse.ArgumentParser(description="Monte Carlo Simulation")
    parser.add_argument('--lang', choices=['en', 'fa'], default='en', help='Language for the application (en or fa)')
    parser.add_argument('--show-plot', action='store_true', help='Show the plot after simulation')
    parser.add_argument('--strategy', choices=['fixed', 'variable'], default='fixed', help='Trading strategy to use')
    args = parser.parse_args()

    if args.lang == 'fa':
        prompts = {
            "initial_balance": reshape_text("مقدار اولیه بالانس تجاری را وارد کنید: "),
            "risk_percentage": reshape_text("مقدار ریسک در هر معامله (درصدی از بالانس اولیه) را وارد کنید: "),
            "win_rate": reshape_text("نرخ برد را وارد کنید (مثلاً 0.6 برای 60%): "),
            "reward_to_risk_ratio": reshape_text("نسبت سود به ریسک را وارد کنید: "),
            "num_trades": reshape_text("تعداد معاملات را وارد کنید: "),
            "num_simulations": reshape_text("تعداد شبیه‌سازی‌ها را وارد کنید: "),
            "plot_title": reshape_text("تغییرات بالانس در طول معاملات (تمام شبیه‌سازی‌ها)"),
            "initial_balance_label": reshape_text("بالانس اولیه")
        }
    else:
        prompts = {
            "initial_balance": "Enter the initial trading balance: ",
            "risk_percentage": "Enter the risk percentage per trade (as a percentage of the initial balance): ",
            "win_rate": "Enter the win rate (e.g., 0.6 for 60%): ",
            "reward_to_risk_ratio": "Enter the reward-to-risk ratio: ",
            "num_trades": "Enter the number of trades: ",
            "num_simulations": "Enter the number of simulations: ",
            "plot_title": "Balance Changes Over Trades (All Simulations)",
            "initial_balance_label": "Initial Balance"
        }

    initial_balance = float(input(prompts["initial_balance"]))
    risk_percentage = float(input(prompts["risk_percentage"]))
    win_rate = float(input(prompts["win_rate"]))
    reward_to_risk_ratio = float(input(prompts["reward_to_risk_ratio"]))
    num_trades = int(input(prompts["num_trades"]))
    num_simulations = int(input(prompts["num_simulations"]))

    all_balances = []
    sample_results = []

    for simulation in range(num_simulations):
        final_balance, balances, results = monte_carlo_simulation(initial_balance, risk_percentage, win_rate, reward_to_risk_ratio, num_trades, args.strategy)
        all_balances.append(balances)
        if simulation == 0:
            sample_results = results

    df_sample_results = pd.DataFrame(sample_results)
    df_sample_results.to_excel("monte_carlo_sample_results.xlsx", index=False)

    return all_balances, initial_balance, prompts, args.show_plot

if __name__ == "__main__":
    all_balances, initial_balance, prompts, show_plot = main()
    if show_plot:
        plot_results(all_balances, initial_balance, prompts)