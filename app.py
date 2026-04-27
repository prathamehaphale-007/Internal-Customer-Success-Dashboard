import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ClearQuote CS Dashboard", layout="wide")
st.title("ClearQuote Customer Success Dashboard")

@st.cache_data
def load_data():
    file_path = r"C:\Users\Prathmesh Aphale\Downloads\Internal_Customer_Success_Dashboard\CQ Product Analyst Assignment Apr 2026.xlsx"
    customers = pd.read_excel(file_path, sheet_name='Customers')
    usage = pd.read_excel(file_path, sheet_name='Usage')
    tickets = pd.read_excel(file_path, sheet_name='Tickets')
    fleet = pd.read_excel(file_path, sheet_name='Fleet')
    
    return customers, usage, tickets, fleet

customers, usage, tickets, fleet = load_data()

tab1, tab2, tab3, tab4 = st.tabs(["Customer Overview", "Usage Metrics", "Support & Comms", "Fleet Distribution"])

with tab1:
    st.header("Customer Overview")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", len(customers))
    col2.metric("Total MRR", f"${customers['MRR (USD)'].sum():,}")
    col3.metric("Churned Customers", len(customers[customers['Status'] == 'Churned']))
    
    st.subheader("Customer Locations")
    st.map(customers, latitude='Latitude', longitude='Longitude')
    
    st.subheader("Customer Directory")
    st.dataframe(customers[['Customer ID', 'Company Name', 'Status', 'Tier', 'MRR (USD)', 'CSM', 'City', 'State']], use_container_width=True)

with tab2:
    st.header("Usage Metrics")
    
    selected_customer = st.selectbox("Select a Customer to view usage:", ['All'] + list(usage['Company Name'].unique()))
    
    if selected_customer != 'All':
        filtered_usage = usage[usage['Company Name'] == selected_customer]
    else:
        filtered_usage = usage.groupby('Month', as_index=False).sum(numeric_only=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_insp = px.line(filtered_usage, x='Month', y='Inspections', title="Monthly Inspections", markers=True)
        st.plotly_chart(fig_insp, use_container_width=True)
        
    with col2:
        if selected_customer != 'All':
            y_col = 'Damage Rate (%)'
        else:
            filtered_usage['Damage Rate (%)'] = (filtered_usage['Damage Detected'] / filtered_usage['Inspections']) * 100
            y_col = 'Damage Rate (%)'
            
        fig_dmg = px.line(filtered_usage, x='Month', y=y_col, title="Damage Rate (%)", markers=True)
        st.plotly_chart(fig_dmg, use_container_width=True)
        
    st.subheader("API Calls & Logins")
    fig_api = px.bar(filtered_usage, x='Month', y=['API Calls', 'Logins'], title="API Usage & Platform Logins", barmode='group')
    st.plotly_chart(fig_api, use_container_width=True)

with tab3:
    st.header("Support Tickets")
    
    col1, col2 = st.columns(2)
    with col1:
        status_counts = tickets['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        fig_status = px.pie(status_counts, names='Status', values='Count', title="Tickets by Status")
        st.plotly_chart(fig_status, use_container_width=True)
        
    with col2:
        priority_counts = tickets['Priority'].value_counts().reset_index()
        priority_counts.columns = ['Priority', 'Count']
        fig_priority = px.bar(priority_counts, x='Priority', y='Count', title="Tickets by Priority")
        st.plotly_chart(fig_priority, use_container_width=True)
        
    st.subheader("Recent Open / Escalated Tickets")
    open_tickets = tickets[tickets['Status'].isin(['Open', 'In Progress', 'Escalated', 'Waiting on Customer'])]
    st.dataframe(open_tickets[['Ticket ID', 'Company Name', 'Subject', 'Priority', 'Status', 'Created Date', 'Assigned CSM']], use_container_width=True)

with tab4:
    st.header("Fleet Distribution")
    
    st.subheader("Vehicle Type Breakdown (Global)")
    vehicle_types = ['Cargo Van', 'Sprinter Van', 'Box Truck', 'Pickup Truck', 'Electric Van']
    vehicle_sums = fleet[vehicle_types].sum().reset_index()
    vehicle_sums.columns = ['Vehicle Type', 'Total']
    fig_vehicles = px.pie(vehicle_sums, names='Vehicle Type', values='Total', title="Overall Fleet Composition")
    st.plotly_chart(fig_vehicles, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        telematics = fleet['Telematics Provider'].value_counts().reset_index()
        telematics.columns = ['Provider', 'Count']
        fig_tel = px.bar(telematics, x='Provider', y='Count', title="Telematics Providers")
        st.plotly_chart(fig_tel, use_container_width=True)
        
    with col2:
        fms = fleet['FMS Platform'].value_counts().reset_index()
        fms.columns = ['Platform', 'Count']
        fig_fms = px.bar(fms, x='Platform', y='Count', title="FMS Platforms")
        st.plotly_chart(fig_fms, use_container_width=True)
        
    st.subheader("Fleet Directory")
    st.dataframe(fleet[['Company Name', 'Total Vehicles', 'Avg Vehicle Age (yrs)', 'Telematics Provider', 'FMS Platform', 'Primary Use Case']], use_container_width=True)