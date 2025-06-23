import random
import math
import matplotlib.pyplot as plt

def simulate_week(season_factor_customers, season_factor_spend,marketing_factor=1.0):
    base_customers=50
    mu_cust=base_customers * season_factor_customers * marketing_factor
    num_customers=int(round(random.gauss(mu_cust, 2 * math.sqrt(mu_cust))))
    if num_customers<0:
        num_customers=0
    base_spend=80.0*season_factor_spend*marketing_factor
    total_revenue=0.0
    for i in range(num_customers):
        spend=random.gauss(base_spend, 0.5*base_spend)
        if spend<0:
            spend=0
        total_revenue+=spend
    fix_costs=1000.0
    costs_pro_customer=20.0
    total_costs=fix_costs+costs_pro_customer+num_customers
    return total_revenue, total_costs

print("Die Monte-Carlo Simulation startet")
weeks_in_year=52  
season_factors_customers=[]
season_factors_spend=[]
winter_werbung=True
for i in range(1, weeks_in_year+1):
    if 1<=i<=13: # - Winter (w1-w13):factor_customers=0.8, factor_spend=0.9
            season_factors_customers.append(0.8)
            season_factors_spend.append(0.9)
    elif 14<=i<= 26: #Fruehling (w14-w26):factor_customers=1.0, factor_spend=1.0
            season_factors_customers.append(1.0)
            season_factors_spend.append(1.0)
    elif 27<=i<= 39: #Sommer(w27-w39):factor_customers=1.3, factor_spend=1.2
            season_factors_customers.append(1.3)
            season_factors_spend.append(1.2)
    else:#Herbst(w40-w52):factor_customers=0.9, factor_spend=1.0
            season_factors_customers.append(0.9)
            season_factors_spend.append(1.0)
monte_carlo_runs=5000
weekly_revenue_sum = [0.0] * weeks_in_year
weekly_profit_sum = [0.0]  * weeks_in_year
for run in range(monte_carlo_runs):
    if (run+1) % 1000 == 0:
        print(f"...Zwischenstand: {run+1} von {monte_carlo_runs} Durchläufen erledigt...")
    for w in range(weeks_in_year):
        marketing_factor = 1.0
        extra_marketing_cost = 0.0
        if winter_werbung and (w+1 <= 13):
            marketing_factor = 1.2
            extra_marketing_cost = 300.0  
        rev, costs = simulate_week(
            season_factors_customers[w],
            season_factors_spend[w],
            marketing_factor
        )
        total_costs = costs + extra_marketing_cost
        profit = rev - total_costs
        weekly_revenue_sum[w] += rev
        weekly_profit_sum[w]  += profit
weekly_revenue_avg = [val / monte_carlo_runs for val in weekly_revenue_sum]
weekly_profit_avg  = [val / monte_carlo_runs for val in weekly_profit_sum]
year_revenue = sum(weekly_revenue_avg)
year_profit  = sum(weekly_profit_avg)
print("\n--- Simulation abgeschlossen! ---\n")
print("Wöchentlicher Durchschnitt (Umsatz / Profit):")
for w in range(weeks_in_year):
    print(f"  Woche {w+1:2d} | Umsatz: {weekly_revenue_avg[w]:8.2f} lv | Profit: {weekly_profit_avg[w]:8.2f} lv")
    
print(f"\nGesamtumsatz Jahr: {year_revenue:8.2f} lv")
print(f"Gesamtprofit Jahr: {year_profit:8.2f} lv")
weeks = list(range(1, weeks_in_year + 1))
    
plt.figure(figsize=(10,6))
plt.plot(weeks, weekly_revenue_avg, label="Durchschn. Umsatz")
plt.plot(weeks, weekly_profit_avg, label="Durchschn. Profit")
plt.title("Erwarteter Umsatz und Profit pro Woche")
plt.xlabel("Woche")
plt.ylabel("EUR")
plt.legend()
plt.grid(True)
plt.show()