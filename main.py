import random
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_simulation(initial_balance, risk_percentage, win_rate, reward_to_risk_ratio, num_trades):
    balance = initial_balance
    balances = [balance]  # لیستی برای ذخیره مقادیر بالانس در هر معامله
    results = []  # لیست برای ذخیره جزئیات هر معامله

    for trade in range(1, num_trades + 1):
        # تعیین مقدار ریسک بر اساس بالانس
        if balance < initial_balance:
            risk_amount = 0.0025 * initial_balance  # 0.25 درصد از بالانس اولیه
            reward_amount = 1.5 * risk_amount  # سود 1.5 برابر ریسک
        else:
            risk_amount = risk_percentage / 100 * initial_balance  # محاسبه مقدار ریسک
            reward_amount = reward_to_risk_ratio * risk_amount  # سود بر اساس نسبت سود به ریسک

        if random.random() < win_rate:  # معامله برد
            balance += reward_amount  # افزایش بالانس به میزان 1.5 برابر ریسک
            result = "Win"
            amount = reward_amount
        else:  # معامله باخت
            balance -= risk_amount  # کاهش بالانس به میزان ریسک
            result = "Loss"
            amount = -risk_amount

        # ذخیره جزئیات معامله
        results.append({
            'Trade Number': trade,
            'Result': result,
            'Change in Balance': amount,
            'New Balance': balance
        })
        balances.append(balance)  # ذخیره بالانس جدید

    return balance, balances, results

def main():
    initial_balance = float(input("مقدار اولیه بالانس تجاری را وارد کنید: "))
    risk_percentage = float(input("مقدار ریسک در هر معامله (درصدی از بالانس اولیه) را وارد کنید: "))
    win_rate = float(input("نرخ برد را وارد کنید (مثلاً 0.6 برای 60%): "))
    reward_to_risk_ratio = float(input("نسبت سود به ریسک را وارد کنید: "))
    num_trades = int(input("تعداد معاملات را وارد کنید: "))
    num_simulations = int(input("تعداد شبیه‌سازی‌ها را وارد کنید: "))  # تعداد شبیه‌سازی‌ها

    all_balances = []  # لیست برای ذخیره بالانس‌ها از تمام شبیه‌سازی‌ها
    sample_results = []  # لیست برای ذخیره جزئیات یک شبیه‌سازی نمونه

    for simulation in range(num_simulations):
        final_balance, balances, results = monte_carlo_simulation(initial_balance, risk_percentage, win_rate, reward_to_risk_ratio, num_trades)
        all_balances.append(balances)  # ذخیره بالانس‌های این شبیه‌سازی
        if simulation == 0:  # فقط جزئیات اولین شبیه‌سازی را ذخیره می‌کنیم
            sample_results = results

    # رسم نمودار برای تمام شبیه‌سازی‌ها
    plt.figure(figsize=(10, 5))
    for balances in all_balances:
        plt.plot(balances, marker='o', alpha=0.5)  # نمودار هر شبیه‌سازی با شفافیت کم
    plt.title('تغییرات بالانس در طول معاملات (تمام شبیه‌سازی‌ها)')
    plt.xlabel('تعداد معاملات')
    plt.ylabel('بالانس')
    plt.grid(True)
    plt.axhline(initial_balance, color='red', linestyle='--', label='بالانس اولیه')
    plt.legend()
    plt.show()

    # ذخیره جزئیات یک شبیه‌سازی نمونه در فایل اکسل
    df_sample_results = pd.DataFrame(sample_results)
    df_sample_results.to_excel("monte_carlo_sample_results.xlsx", index=False)  # ذخیره نتایج نمونه

if __name__ == "__main__":
    main()
