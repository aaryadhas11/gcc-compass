"""
ui_components.py
Reusable dashboard KPI metrics, charts, and budget cards.
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_top_stats():
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Active Tech Centers", value="2,100+", delta="India-wide")
    with c2:
        st.metric(label="Tech Workforce", value="2.4M+", delta="Engineers")
    with c3:
        st.metric(label="Average Launch Time", value="9.2 Months", delta="-3.5 Mo with Partner")
    with c4:
        st.metric(label="Cost Savings vs US/EU", value="62%", delta="Annual Average")

def render_budget_summary(budget: dict):
    st.markdown(f"""
        <div style="background: #0F172A; 
                    padding: 24px; border-radius: 14px; color: #FFFFFF; 
                    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2); 
                    margin-bottom: 20px; border: 1px solid #1E293B;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; color: #94A3B8; font-weight: 600;">
                    Projected Year-1 Expenditure
                </span>
                <span style="background: rgba(37, 99, 235, 0.25); color: #60A5FA; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(96, 165, 250, 0.3);">
                    Verified Benchmark
                </span>
            </div>
            <div style="font-size: 34px; font-weight: 800; margin: 10px 0 6px 0; letter-spacing: -0.03em;">
                ₹{budget['total_inr_lakhs']:,} Lakhs
                <span style="font-size: 20px; font-weight: 500; color: #94A3B8;"> (~${budget['total_usd']:,} USD)</span>
            </div>
            <div style="display: flex; gap: 24px; font-size: 13.5px; color: #CBD5E1; padding-top: 10px; border-top: 1px solid #1E293B; margin-top: 10px;">
                <div>📅 <b>Monthly Run-Rate:</b> ₹{round(budget['total_inr_lakhs'] / 12, 1):,} L/mo</div>
                <div>⚡ <b>One-Time Setup:</b> ₹{budget['setup_lakhs']:,} L</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("##### Annual Expense Breakdown")

    heads = ["Engineering Salaries", "Office & Desks", "Legal & Setup"]
    values = [budget["salaries_lakhs"], budget["rent_lakhs"], budget["setup_lakhs"]]
    colors = ["#2563EB", "#0D9488", "#F59E0B"]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=heads,
        y=values,
        text=[f"₹{v:,.1f} L" for v in values],
        textposition="outside",
        marker=dict(
            color=colors,
            line=dict(width=0)
        ),
        textfont=dict(size=13, color="#0F172A", family="sans-serif")
    ))

    ceiling = max(values) * 1.25

    fig.update_layout(
        height=260,
        margin=dict(t=30, b=10, l=10, r=10),
        yaxis=dict(
            range=[0, ceiling],
            showgrid=True,
            gridcolor="#E2E8F0",
            zeroline=False,
            title="Amount (₹ in Lakhs)"
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color="#334155")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    # Clean zero-scroll responsive summary card
    summary_html = f"""
    <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 14px; overflow: hidden; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);">
        <table style="width: 100%; border-collapse: collapse; font-family: 'Inter', -apple-system, sans-serif;">
            <thead>
                <tr style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0; color: #64748B; font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.04em;">
                    <th style="padding: 10px 14px; text-align: left; font-weight: 600;">Cost Head</th>
                    <th style="padding: 10px 14px; text-align: right; font-weight: 600;">Annual Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #F1F5F9;">
                    <td style="padding: 11px 14px; font-weight: 600; color: #0F172A; font-size: 13px;">Engineering Salaries (Annual)</td>
                    <td style="padding: 11px 14px; text-align: right; font-weight: 700; color: #2563EB; font-size: 13px;">₹{budget['salaries_lakhs']:,} Lakhs</td>
                </tr>
                <tr style="border-bottom: 1px solid #F1F5F9;">
                    <td style="padding: 11px 14px; font-weight: 600; color: #0F172A; font-size: 13px;">Office Space, Utilities & Tech Desks</td>
                    <td style="padding: 11px 14px; text-align: right; font-weight: 700; color: #0D9488; font-size: 13px;">₹{budget['rent_lakhs']:,} Lakhs</td>
                </tr>
                <tr>
                    <td style="padding: 11px 14px; font-weight: 600; color: #0F172A; font-size: 13px;">Legal Registration & Compliance</td>
                    <td style="padding: 11px 14px; text-align: right; font-weight: 700; color: #F59E0B; font-size: 13px;">₹{budget['setup_lakhs']:,} Lakhs</td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    st.markdown(summary_html, unsafe_allow_html=True)

    table_data = pd.DataFrame({
        "Cost Head": [
            "Engineering Salaries (Annual)", 
            "Office Space, Utilities & Tech Desks", 
            "Legal Registration & Compliance"
        ],
        "Annual Amount (₹ Lakhs)": [
            f"₹{budget['salaries_lakhs']:,} Lakhs",
            f"₹{budget['rent_lakhs']:,} Lakhs",
            f"₹{budget['setup_lakhs']:,} Lakhs"
        ]
    })

    csv_bytes = table_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Budget Summary (CSV)",
        data=csv_bytes,
        file_name="gcc_cost_breakdown.csv",
        mime="text/csv"
    )