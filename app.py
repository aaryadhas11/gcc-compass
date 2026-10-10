import streamlit as st
import data_store
import calculator_engine
import ui_components

st.set_page_config(
    page_title="GCC Compass | India Setup Hub",
    page_icon="🧭",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stApp {
    background-color: #F8FAFC !important;
    color: #0F172A !important;
}

[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    padding: 16px !important;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08) !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid #E2E8F0;
}

.stTabs [data-baseweb="tab"] {
    padding: 10px 18px;
    font-weight: 500;
    color: #64748B;
    border-radius: 8px 8px 0 0;
}

.stTabs [aria-selected="true"] {
    color: #062217 !important;
    font-weight: 700 !important;
    border-bottom: 2px solid #062217 !important;
}

.proof-badge {
    background: #FFFFFF;
    color: #0F172A;
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.8);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: default;
}

.proof-badge:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
    background: #FFFFFF;
}

.table-wrap {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    margin-bottom: 12px;
    overflow: hidden;
}

.clean-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-family: 'Inter', -apple-system, sans-serif;
}

.clean-table th {
    background: #F8FAFC;
    padding: 12px 14px;
    color: #64748B;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-weight: 600;
    border-bottom: 1px solid #E2E8F0;
}

.clean-table td {
    padding: 12px 14px;
    border-bottom: 1px solid #F1F5F9;
    font-size: 13px;
    color: #334155;
    vertical-align: middle;
}

.clean-table tr:last-child td {
    border-bottom: none;
}

.clean-table tr:hover {
    background-color: #F8FAFC;
}
</style>
""", unsafe_allow_html=True)

hero_html = """<div style="background: #062217; border-radius: 20px; padding: 42px 24px 36px 24px; text-align: center; color: #FFFFFF; margin-bottom: 24px; border: 1px solid #0F3827;">
<div style="display: inline-flex; align-items: center; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 999px; padding: 6px 16px; font-size: 13px; font-weight: 500; margin-bottom: 18px;">
✨ 100+ Global Tech Hubs Built in India
</div>
<h1 style="font-family: Georgia, 'Times New Roman', serif; font-size: 38px; font-weight: 700; color: #FFFFFF; line-height: 1.25; margin-bottom: 14px;">
Your <span style="background: #D4F973; color: #062217; padding: 2px 14px; border-radius: 999px; font-style: italic;">India tech hub,</span> planned in minutes.
</h1>
<p style="font-size: 15px; color: #A3C2B3; max-width: 620px; margin: 0 auto 28px auto; line-height: 1.5;">
Direct benchmarks for developer salaries, Grade-A office leases, and verified setup partners across India's top 5 tech cities.
</p>
<div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
<div class="proof-badge">
🏢 Bengaluru office lease completed
</div>
<div class="proof-badge">
💰 May engineering payroll cleared
</div>
<div class="proof-badge">
⚡ MCA legal entity filing approved
</div>
</div>
</div>"""

st.markdown(hero_html, unsafe_allow_html=True)

ui_components.render_top_stats()
st.write("")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 City Benchmarks", 
    "📡 Expansion Tracker",
    "🧮 Cost Estimator", 
    "🤝 Verified Partners"
])

# -------------------------------------------------------------
# TAB 1: City Benchmarks
# -------------------------------------------------------------
with tab1:
    st.subheader("Compare Tech Hubs in India")
    st.write("Compare commercial office rent, developer salaries, and state policy support across top destinations:")
    
    city_df = data_store.get_city_benchmarks()
    
    city_rows = "".join([
        f"<tr>"
        f"<td style='font-weight:700; color:#0F172A;'>📍 {r['City']}</td>"
        f"<td style='font-weight:600; color:#2563EB;'>{r['Active Tech Centers']}</td>"
        f"<td style='font-weight:600;'>₹{r['Office Rent (₹/sq ft/month)']}</td>"
        f"<td style='font-weight:600;'>₹{r['Senior Dev Salary (₹ LPA)']} LPA</td>"
        f"<td><span style='background:#F1F5F9; color:#334155; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:500;'>{r['Core Talent Strength']}</span></td>"
        f"<td style='font-size:12px; color:#475569;'>{r['Government Support']}</td>"
        f"</tr>"
        for _, r in city_df.iterrows()
    ])
    
    table_city_html = (
        '<div class="table-wrap">'
        '<table class="clean-table">'
        '<thead><tr>'
        '<th>City Hub</th>'
        '<th>Active GCCs</th>'
        '<th>Rent / Mo</th>'
        '<th>Sr. Dev CTC</th>'
        '<th>Core Specialization</th>'
        '<th>State Incentives</th>'
        '</tr></thead>'
        f'<tbody>{city_rows}</tbody>'
        '</table></div>'
    )
    st.markdown(table_city_html, unsafe_allow_html=True)
    
    st.info("💡 Quick Takeaway: While Bengaluru has the highest concentration of specialized AI and product talent, hubs like Pune, Hyderabad, and Chennai offer 30–45% lower commercial office rent with strong engineering density.")

# -------------------------------------------------------------
# TAB 2: Upcoming GCC Tracker
# -------------------------------------------------------------
with tab2:
    st.subheader("Recent & Upcoming Tech Hub Setups")
    st.write("Verified market pipeline tracking international corporate filings and new site announcements:")
    
    pipeline_df = data_store.get_upcoming_gcc_pipeline()

    status_badges = {
        "Hiring Leadership": "background: #EFF6FF; color: #1D4ED8; border: 1px solid #BFDBFE;",
        "Office Build-out": "background: #FEF3C7; color: #B45309; border: 1px solid #FDE68A;",
        "Operational (Expanding)": "background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0;",
        "Site Finalized": "background: #F5F3FF; color: #6D28D9; border: 1px solid #DDD6FE;",
        "Entity Registered": "background: #F1F5F9; color: #334155; border: 1px solid #CBD5E1;"
    }

    pipe_rows = "".join([
        f"<tr>"
        f"<td style='font-weight:700; color:#0F172A;'>🏢 {r['Company / Parent']}</td>"
        f"<td><span style='background:#F8FAFC; color:#475569; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:600; border:1px solid #E2E8F0;'>📍 {r['Target City']}</span></td>"
        f"<td>{r['Focus Area']}</td>"
        f"<td style='font-weight:600; color:#0F172A;'>👥 {r['Planned Headcount']}</td>"
        f"<td><span style='padding:3px 9px; border-radius:999px; font-size:12px; font-weight:600; {status_badges.get(r['Status'], '')}'>● {r['Status']}</span></td>"
        f"</tr>"
        for _, r in pipeline_df.iterrows()
    ])

    table_pipe_html = (
        '<div class="table-wrap">'
        '<table class="clean-table">'
        '<thead><tr>'
        '<th>Company / Entity</th>'
        '<th>Target Hub</th>'
        '<th>Focus Domain</th>'
        '<th>Planned Scale</th>'
        '<th>Current Status</th>'
        '</tr></thead>'
        f'<tbody>{pipe_rows}</tbody>'
        '</table></div>'
    )
    st.markdown(table_pipe_html, unsafe_allow_html=True)
    st.caption("🔒 Verified across MCA corporate filings, SEZ lease allocations, and public disclosures.")

# -------------------------------------------------------------
# TAB 3: Cost Estimator
# -------------------------------------------------------------
with tab3:
    st.subheader("Estimate Your Year-1 Launch Budget")
    st.write("Adjust team size and location to see estimated annual expenses:")
    
    col_input, col_output = st.columns([1, 1], gap="large")
    
    with col_input:
        st.markdown("#### Setup Choices")
        city_options = ["Bengaluru", "Hyderabad", "Pune", "Delhi-NCR (Gurugram)", "Chennai"]
        selected_city = st.selectbox("Choose Target City", city_options)
        
        st.markdown("**Target Team Size (Engineers)**")
        col_type, col_slide = st.columns([1, 2])
        with col_type:
            team_size = st.number_input(
                "Type Number", 
                min_value=5, 
                max_value=300, 
                value=50, 
                step=5, 
                label_visibility="collapsed"
            )
        with col_slide:
            st.caption(f"Configured: **{team_size} Engineers**")
        
        hiring_model = st.radio("Hiring & Office Strategy", [
            "Start Fast via Partner (Hire talent & space through partner first)",
            "Direct Entity Setup (Register new Indian company on Day 1)"
        ])
        
        hire_via_partner = "Partner" in hiring_model
        
        budget = calculator_engine.calculate_budget(
            city=selected_city,
            team_size=team_size,
            hire_via_partner=hire_via_partner
        )

    with col_output:
        st.markdown("#### Estimated Expenses")
        ui_components.render_budget_summary(budget)

# -------------------------------------------------------------
# TAB 4: Verified Partner Directory
# -------------------------------------------------------------
with tab4:
    st.subheader("Verified Service Partners Directory")
    st.write("Find trusted partners for office spaces, hiring, payroll, and company setup.")
    
    vendor_df = data_store.get_vendor_directory()
    
    col_filter, col_results = st.columns([1, 2.5], gap="large")
    
    with col_filter:
        st.markdown("### 🔍 Filters")
        
        search_query = st.text_input("Search by Name", placeholder="e.g. Flexiple, Awfis, Smartworks...")
        
        all_categories = ["All Services"] + sorted(vendor_df["Category"].unique().tolist())
        selected_category = st.selectbox("Service Type", all_categories)
        
        location_options = ["All Locations", "Bengaluru", "Hyderabad", "Pune", "Delhi-NCR", "Chennai", "Pan-India"]
        selected_location = st.selectbox("Location / Presence", location_options)
        
        min_rating_choice = st.radio(
            "Customer Rating",
            [
                "All Ratings",
                "4.5 ★ & above (Top Rated)",
                "4.0 ★ – 4.4 ★ (High Rated)",
                "Below 4.0 ★"
            ],
            index=0
        )
        
        st.markdown("---")
        st.caption("🔒 All partners have verified corporate credentials and proven enterprise delivery records.")

    with col_results:
        filtered = vendor_df.copy()
        
        if search_query:
            filtered = filtered[filtered["Partner Name"].str.contains(search_query, case=False, na=False)]
            
        if selected_category != "All Services":
            filtered = filtered[filtered["Category"] == selected_category]
            
        if selected_location != "All Locations":
            filtered = filtered[filtered["Locations"].str.contains(selected_location, case=False, na=False)]
            
        def get_score(val):
            try:
                return float(str(val).split("/")[0].strip())
            except Exception:
                return 0.0

        if min_rating_choice == "4.5 ★ & above (Top Rated)":
            filtered = filtered[filtered["Rating"].apply(get_score) >= 4.5]
        elif min_rating_choice == "4.0 ★ – 4.4 ★ (High Rated)":
            filtered = filtered[filtered["Rating"].apply(get_score).between(4.0, 4.49)]
        elif min_rating_choice == "Below 4.0 ★":
            filtered = filtered[filtered["Rating"].apply(get_score) < 4.0]
            
        st.markdown(f"**Showing {len(filtered)} of {len(vendor_df)} Verified Partners**")
        
        if len(filtered) > 0:
            vendor_rows = "".join([
                f"<tr>"
                f"<td style='font-weight:700; color:#0F172A;'>{r['Partner Name']}</td>"
                f"<td><span style='background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:600;'>{r['Category']}</span></td>"
                f"<td style='font-size:13px;'>{r['Locations']}</td>"
                f"<td style='font-weight:600; color:#0F172A;'>{r['Track Record']}</td>"
                f"<td><span style='background:#ECFDF5; color:#047857; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:700; border:1px solid #A7F3D0;'>★ {r['Rating']}</span></td>"
                f"</tr>"
                for _, r in filtered.iterrows()
            ])
            
            table_vendor_html = (
                '<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; '
                'max-height:480px; overflow-y:auto; overflow-x:hidden; box-shadow:0 1px 3px rgba(15,23,42,0.04); margin-bottom:12px;">'
                '<table class="clean-table" style="width:100%; border-collapse:collapse;">'
                '<thead style="position:sticky; top:0; z-index:2; background:#F8FAFC;"><tr>'
                '<th>Partner Name</th>'
                '<th>Pillar / Category</th>'
                '<th>Presence</th>'
                '<th>Audited Track Record</th>'
                '<th>Verified Rating</th>'
                '</tr></thead>'
                f'<tbody>{vendor_rows}</tbody>'
                '</table></div>'
            )
            st.markdown(table_vendor_html, unsafe_allow_html=True)
        else:
            st.warning("No partners match your selected filters. Try adjusting your service or rating selection.")