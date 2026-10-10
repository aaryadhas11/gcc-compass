"""
calculator_engine.py
Financial modeling engine for Year-1 GCC expansion budgets.
"""
from typing import Dict, Any

SALARY_BY_CITY = {
    "Bengaluru": 28.5,
    "Hyderabad": 24.0,
    "Pune": 22.0,
    "Delhi-NCR (Gurugram)": 26.0,
    "Chennai": 21.5
}

RENT_BY_CITY = {
    "Bengaluru": 145,
    "Hyderabad": 95,
    "Pune": 85,
    "Delhi-NCR (Gurugram)": 115,
    "Chennai": 80
}

USD_EXCHANGE_RATE = 86.5
SQ_FT_PER_PERSON = 90

def calculate_budget(city: str, team_size: int, hire_via_partner: bool) -> Dict[str, Any]:
    """
    Calculates Year-1 budget:
    Total = Team Salaries + Office Lease + Legal/Setup
    """
    annual_salaries = team_size * SALARY_BY_CITY.get(city, 25.0)
    annual_rent = (team_size * SQ_FT_PER_PERSON * RENT_BY_CITY.get(city, 100) * 12) / 100000.0
    
    legal_setup_cost = 15.0 if hire_via_partner else 45.0
    
    total_inr = annual_salaries + annual_rent + legal_setup_cost
    total_usd = (total_inr * 100000.0) / USD_EXCHANGE_RATE
    
    return {
        "salaries_lakhs": round(annual_salaries, 1),
        "rent_lakhs": round(annual_rent, 1),
        "setup_lakhs": round(legal_setup_cost, 1),
        "total_inr_lakhs": round(total_inr, 1),
        "total_usd": int(total_usd)
    }