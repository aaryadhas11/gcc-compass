"""
data_store.py
Stores real-world benchmark data across India's top 5 GCC hubs,
upcoming market intelligence pipeline, and verified service partners.
"""
import pandas as pd

def get_city_benchmarks() -> pd.DataFrame:
    """Returns grounded cost, talent, and government support for top Indian cities."""
    return pd.DataFrame([
        {
            "City": "Bengaluru",
            "Active Tech Centers": "920+",
            "Office Rent (₹/sq ft/month)": 145,
            "Senior Dev Salary (₹ LPA)": 28.5,
            "Core Talent Strength": "AI, DeepTech & Core Product",
            "Government Support": "Karnataka KATALYST (Tax breaks & power subsidies)"
        },
        {
            "City": "Hyderabad",
            "Active Tech Centers": "485+",
            "Office Rent (₹/sq ft/month)": 95,
            "Senior Dev Salary (₹ LPA)": 24.0,
            "Core Talent Strength": "Cloud Platforms & Enterprise SaaS",
            "Government Support": "Telangana ICT Policy (Fast-track permits & patents)"
        },
        {
            "City": "Pune",
            "Active Tech Centers": "295+",
            "Office Rent (₹/sq ft/month)": 85,
            "Senior Dev Salary (₹ LPA)": 22.0,
            "Core Talent Strength": "AutoTech & Embedded Software",
            "Government Support": "Maharashtra IT Policy (Lease discounts & stamp duty)"
        },
        {
            "City": "Delhi-NCR (Gurugram)",
            "Active Tech Centers": "330+",
            "Office Rent (₹/sq ft/month)": 115,
            "Senior Dev Salary (₹ LPA)": 26.0,
            "Core Talent Strength": "FinTech & Data Analytics",
            "Government Support": "Haryana IT Policy (Local employment incentives)"
        },
        {
            "City": "Chennai",
            "Active Tech Centers": "240+",
            "Office Rent (₹/sq ft/month)": 80,
            "Senior Dev Salary (₹ LPA)": 21.5,
            "Core Talent Strength": "SaaS Products & Automotive R&D",
            "Government Support": "Tamil Nadu R&D Policy (Direct setup grants)"
        }
    ])

def get_upcoming_gcc_pipeline() -> pd.DataFrame:
    """Intelligence tracking recent announcements and verified foreign company registrations."""
    return pd.DataFrame([
        {
            "Company / Parent": "Arm Holdings",
            "Target City": "Bengaluru",
            "Focus Area": "Semiconductor & Edge AI R&D",
            "Planned Headcount": "500 Engineers",
            "Status": "Hiring Leadership"
        },
        {
            "Company / Parent": "Lloyds Banking Group",
            "Target City": "Hyderabad",
            "Focus Area": "Core Banking Platforms & Cloud",
            "Planned Headcount": "1,200 Tech Roles",
            "Status": "Office Build-out"
        },
        {
            "Company / Parent": "Mercedes-Benz Tech",
            "Target City": "Pune",
            "Focus Area": "Vehicle OS & Embedded Firmware",
            "Planned Headcount": "450 Engineers",
            "Status": "Operational (Expanding)"
        },
        {
            "Company / Parent": "Booking Holdings",
            "Target City": "Bengaluru",
            "Focus Area": "FinTech & Real-time Pricing Engines",
            "Planned Headcount": "300 Engineers",
            "Status": "Site Finalized"
        },
        {
            "Company / Parent": "Maersk Technology",
            "Target City": "Chennai",
            "Focus Area": "Global Logistics Optimization & AI",
            "Planned Headcount": "400 Engineers",
            "Status": "Entity Registered"
        }
    ])

def get_vendor_directory() -> pd.DataFrame:
    """Returns verified service partners across all operational pillars."""
    return pd.DataFrame([
        # Tech Talent & EOR
        {
            "Partner Name": "Flexiple Network",
            "Category": "Tech Hiring & EOR",
            "Locations": "Pan-India",
            "Track Record": "120+ Teams Built",
            "Rating": "4.9 / 5.0"
        },
        {
            "Partner Name": "Deel India",
            "Category": "Tech Hiring & EOR",
            "Locations": "Pan-India",
            "Track Record": "85+ Global Entrants",
            "Rating": "4.7 / 5.0"
        },
        {
            "Partner Name": "Multiplier",
            "Category": "Tech Hiring & EOR",
            "Locations": "Pan-India",
            "Track Record": "60+ Tech Clients",
            "Rating": "4.5 / 5.0"
        },

        # Managed Workspaces & Real Estate
        {
            "Partner Name": "Awfis Enterprise",
            "Category": "Managed Workspaces",
            "Locations": "Bengaluru, Hyderabad, Pune, Delhi-NCR, Chennai",
            "Track Record": "45+ Tech Centers",
            "Rating": "4.8 / 5.0"
        },
        {
            "Partner Name": "IndiQube",
            "Category": "Managed Workspaces",
            "Locations": "Bengaluru, Pune, Chennai",
            "Track Record": "50+ Dedicated Offices",
            "Rating": "4.9 / 5.0"
        },
        {
            "Partner Name": "Table Space",
            "Category": "Managed Workspaces",
            "Locations": "Bengaluru, Hyderabad, Pune, Gurugram",
            "Track Record": "35+ Premium GCC Campuses",
            "Rating": "4.8 / 5.0"
        },
        {
            "Partner Name": "Smartworks",
            "Category": "Managed Workspaces",
            "Locations": "Delhi-NCR, Pune, Bengaluru, Hyderabad",
            "Track Record": "40+ Enterprise Hubs",
            "Rating": "4.6 / 5.0"
        },

        # Legal & Company Registration
        {
            "Partner Name": "Fox Mandal & Associates",
            "Category": "Legal & Registration",
            "Locations": "Bengaluru, Hyderabad, Chennai",
            "Track Record": "45+ Entities Registered",
            "Rating": "4.8 / 5.0"
        },
        {
            "Partner Name": "Kochhar & Co.",
            "Category": "Legal & Registration",
            "Locations": "Delhi-NCR, Bengaluru, Chennai, Hyderabad",
            "Track Record": "60+ Global Subsidiaries",
            "Rating": "4.7 / 5.0"
        },
        {
            "Partner Name": "Vakilsearch Enterprise",
            "Category": "Legal & Registration",
            "Locations": "Pan-India",
            "Track Record": "200+ Corporate Filings",
            "Rating": "4.3 / 5.0"
        },

        # IT Hardware & Logistics
        {
            "Partner Name": "RentAlpha Enterprise",
            "Category": "IT Hardware & Devices",
            "Locations": "Bengaluru, Hyderabad, Pune, Delhi-NCR, Chennai",
            "Track Record": "80+ Tech Client Fleets",
            "Rating": "4.6 / 5.0"
        },
        {
            "Partner Name": "Hofmann Global Logistics",
            "Category": "IT Hardware & Devices",
            "Locations": "Pan-India",
            "Track Record": "50k+ Devices Deployed",
            "Rating": "4.4 / 5.0"
        },

        # Full Advisory
        {
            "Partner Name": "ANSR Advisory",
            "Category": "Full-Lifecycle Setup",
            "Locations": "Pan-India",
            "Track Record": "110+ Tech Centers Launched",
            "Rating": "4.8 / 5.0"
        }
    ])