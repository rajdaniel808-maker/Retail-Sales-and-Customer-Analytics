import streamlit as st
import pandas as pd
import plotly.express as px

#Page Configuration
st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)

#Custom CSS
st.markdown("""
    <style>
    /* MainBackground */
    .stApp{
          background-color:#0e1117;
          color:white;
}
/* Reduce vertical spacing between dashboard sections */
[data-testid="stVerticalBlock"] {
    gap: 0.5rem;
}
   /* MainContent Spacing */
  .block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}
   /* Sidebar */
   [data-testid = "stSidebar"]{

              background-color:#11182b;
              color:white
       }
    /* Make Streamlit top header Transparent */
    [data-testid = "stHeader"]{

                 background:transparent;   
    
    }
       /* Dashboard Title */
       h1,h2,h3{
           color:white;
           }
        /* KPI Cards */
        [data-testid = "stMetric"]{

           background:linear-gradient(
           135deg,
           #18243e,
           #111a2e
           );
            border: 1px solid #293957;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

/* KPI Labels */
[data-testid="stMetricLabel"] {
    color: #b8c5dc;
}

/* KPI Values */
[data-testid="stMetricValue"] {
    color: #ffffff;
    font-weight: bold;
}
/* Chart Containers */
[data-testid="stPlotlyChart"] {
    background-color: #111a2e;
    border: 1px solid #263550;
    border-radius: 10px;
    padding: 5px;
    box-sizing: border-box;
    overflow: hidden;
}
/* Sidebar Heading */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2 {
    color: white;
    font-weight: bold;
}

/* Sidebar buttons */
[data-testid="stSidebar"] button {
    background-color: #1e293b;
    color: white;
    border: 1px solid #3b82f6;
    border-radius: 8px;
}

/* Button hover effect */
[data-testid="stSidebar"] button:hover {
    background-color: #3b82f6;
    color: white;
    border: 1px solid #60a5fa;
}

</style>
""",unsafe_allow_html=True)
#Dashboard Title
st.title("📊Retail Sales And Customer Analytics")
st.subheader("Business Performance Dashboard")
st.markdown( """
<hr style="
      height:3px;
      border:None;
      background:linear-gradient(
           90deg,
           #3b82f6,
           #8b5cf6,
           #06b6d4
           );
           border-radius: 5px;
           ">
           """,unsafe_allow_html=True)

#Load The Dataset
sales_df = pd.read_csv("Documents/Projects/Retail Sales & Customer Analytics/notebooks/cleaned_retail_sales_data.csv")

#Side Bar 
st.sidebar.title("Filters")

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(sales_df["Country"].unique().tolist()),
    key="country_filter"
)

selected_month = st.sidebar.selectbox(
    "Select Month",
    ["All"] + sorted(sales_df["YearMonth"].unique().tolist()),
    key="month_filter"
)

def reset_filters():
    st.session_state["country_filter"] = "All"
    st.session_state["month_filter"] = "All"

st.sidebar.button(" Reset Filters", on_click=reset_filters)

filtered_df = sales_df.copy()
if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]
    
if selected_month != "All":
    filtered_df = filtered_df[filtered_df["YearMonth"] == selected_month]

st.sidebar.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_retail_sales.csv",
    mime="text/csv"
)
#Kpis
col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    total_revenue = filtered_df["Revenue"].sum()
    st.metric("💰Total Revenue:",f"£{total_revenue:,.2f}")
with col2:
    total_orders = filtered_df["InvoiceNo"].nunique()
    st.metric("📦Total Orders:",f"{total_orders:,}")
with col3:
    total_customers = filtered_df["CustomerID"].nunique()
    st.metric("👥Total Customers:",f"{total_customers:,}")
with col4:
    total_products = filtered_df["Description"].nunique()
    st.metric("🛍️Total Products:",f"{total_products:,}")
with col5:
    monthly_revenue = filtered_df.groupby("YearMonth")["Revenue"].sum().sort_index()
    if len(monthly_revenue) >= 2:
        current_month_sales = monthly_revenue.iloc[-1]

        previous_month_sales = monthly_revenue.iloc[-2]

        sales_growth = (
        (current_month_sales - previous_month_sales)
        / previous_month_sales
         ) * 100

    else:
      sales_growth = 0
    st.metric(
        "📈 Sales Growth",
        f"{sales_growth:.2f}%",
        delta=f"{sales_growth:.2f}%"
    )

#Monthly Sales & Top10 Products Box
colm1,colm2 = st.columns([1,1])
with colm1:
    monthly_sales = filtered_df.groupby("YearMonth")["Revenue"].sum()
    
    fig = px.line(
    monthly_sales,
    labels={
        "YearMonth": "Month",
        "value": "Revenue"
    },
         markers=True
    )
    fig.update_traces(
       line=dict(color="#3b82f6", width=3),
       marker=dict(size=7),
       hovertemplate=
       "Month: %{x}<br>" +
       "Revenue: £%{y:,.2f}" +
       "<extra></extra>"
     )
    fig.update_layout(
      paper_bgcolor="#111a2e",
      plot_bgcolor="#111a2e",
      font_color="white",
      xaxis_tickangle=0,
      xaxis_dtick="M1",
      yaxis_tickprefix="£",
      yaxis_tickformat=",",
      xaxis_title="Month",
      yaxis_title="Revenue",
      height=350,
      margin=dict(t = 100, l = 50, r = 20, b = 40),
      showlegend=False,
      title={
        "text": "📈 Monthly Sales Trends",
        "x": 0.05,
        "xanchor": "left",
        "font":{
            "color":"white",
            "size":30
    }
    },
        font = dict(color="white"),

        xaxis=dict(
            tickfont=dict(color="white"),
            title_font=dict(color="white")
        ),
        yaxis=dict(
            tickfont=dict(color="white"),
            title_font=dict(color="white")
        )
    )
    st.plotly_chart(fig, use_container_width=True)

with colm2:
    top_10_products = filtered_df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)

    fig_products = px.bar(
    top_10_products,
    orientation="h",
    title="Top 10 Products",
    text_auto=".2s",
    color_discrete_sequence=["#8b5cf6"]

    )
    fig_products.update_traces(
        textposition="outside",
        textfont=dict(color="white", size=12),
        hovertemplate=
              "Product: %{y}<br>" +
              "Revenue: £%{x:,.2f}" +
              "<extra></extra>"
    )                           
    fig_products.update_layout(
        xaxis_tickprefix="£",
        xaxis_tickformat=","
    )
    fig_products.update_layout(
      paper_bgcolor="#111a2e",
      plot_bgcolor="#111a2e",
      font_color="white",
      xaxis_tickprefix="£",
      xaxis_tickformat=",",
      yaxis_title=None,
      xaxis_title="Revenue",
      height=350,
      showlegend=False,
      title = {
          "text":"🏆 Top 10 Products by Revenue",
          "xanchor":"left",
          "x":0.05,
          "font" : {
              "color":"white",
              "size":30
    }
    },
        font = dict(color="white"),
        xaxis=dict(
            tickfont = dict(color="white"),
            title_font = dict(color="white")
        ),
        yaxis=dict(
            tickfont = dict(color="white"),
            title_font = dict(color="white")
            )
        

      ) 
    st.plotly_chart(fig_products, use_container_width=True)


#Country , Customer Analysis Customer Segmentation

#Country Sales
country_sales = sales_df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)
#Only Top4
top4countries = country_sales.head(4)
#Others into one "Other Section"
other_revenue = country_sales.iloc[4:].sum()
#Preapre Chart Data
country_chart_data = pd.concat([top4countries,pd.Series({"Others":other_revenue})]).rename_axis("Country").reset_index(name="Revenue")








colc1,colc2,colc3 = st.columns([1,1,1])

with colc1:
    fig_country = px.pie(
       country_chart_data,
       names="Country",
       values="Revenue",
       hole=0.5,
       title="Revenue By Country",
       color_discrete_sequence=[
        "#3b82f6",
        "#8b5cf6",
        "#06b6d4",
        "#f59e0b",
        "#64748b"
    ]
    )
    fig_country.update_traces(
       textinfo = "percent",
       textposition="inside",
        textfont=dict(
        color="white",
        size=13
    )
    )
    fig_country.update_layout(
      paper_bgcolor="#111a2e",
      plot_bgcolor="#111a2e",
      font_color="white",
      showlegend=True,
      height=375,
      legend_title_text="Country",
      title = {
        "text":"🌏Sales by Country",
        "xanchor":"left",
        "x":0.05,
        "font":{
             "color":"white",
             "size" :30
        
        }
    }
    )
    fig_country.update_layout(
        font = dict(color="white"),
        legend = dict(
            font=dict(color="white"),
            title = dict(font = dict(color="white"))
    )
    )

    st.plotly_chart(fig_country,use_container_width=True)

with colc2:
    # Customer Analysis
    customer_monthly_sales = filtered_df.groupby("YearMonth")["Revenue"].sum()
    average_order_value = filtered_df.groupby("InvoiceNo")["Revenue"].sum().mean()
    customer_lifetime_value = filtered_df.groupby("CustomerID")["Revenue"].sum().mean()
    st.subheader("👥Customer Analysis")
    colinc1,colinc2 = st.columns(2)
    with colinc1:
        st.metric("Average Order Value",f"£{average_order_value:,.2f}")
    with colinc2:
        st.metric("Customer Lifetime Value",f"£{customer_lifetime_value:,.2f}")
    

    fig_customer = px.line(
      customer_monthly_sales,
      markers=True
        
    )

    fig_customer.update_layout(
    paper_bgcolor="#111a2e",
    plot_bgcolor="#111a2e",
    font_color="white",
    height=200,
    showlegend=False,
    xaxis_title=None,
    yaxis_title=None,
    margin=dict(
        l=10,
        r=10,
        t=10,
        b=10
    ),
    title = {
        "text":"Monthly Customer Spending",
        "xanchor":"left",
        "x":0.05
    }
    )
    fig_customer.update_traces(
    line=dict(
        color="#a855f7",
        width=2
    ),
    marker=dict(size=4)
    )

    st.plotly_chart(
      fig_customer,
      use_container_width=True
    )

# Customer Segmentation
customer_revenue = filtered_df.groupby("CustomerID")["Revenue"].sum()        
customer_segments = pd.cut(
    customer_revenue,
    bins=[0, 100, 500, float("inf")],
    labels=["Occasional", "Regular", "Premium"]
)
segment_counts = customer_segments.value_counts()

with colc3:
    fig_segments = px.pie(
        segment_counts,
        names=segment_counts.index,
        values=segment_counts.values,
        color_discrete_sequence=[
        "#3b82f6",
        "#8b5cf6",
        "#06b6d4"
    ]
    )
    

    fig_segments.update_traces(
        textinfo="percent",
        textposition="inside",
        textfont=dict(
        color="white",
        size=13
    )
    )
    fig_segments.update_layout(
    paper_bgcolor="#111a2e",
    plot_bgcolor="#111a2e",
    font_color="white",
    showlegend=True,
    height=375,
    legend_title_text="Customer Segment",
    title = {
      "text":"👥 Customer Segmentation",
      "xanchor":"left",
      "x":0.05,
      "font":{
          "color":"white",
          "size":30
    }
    },
        font = dict(color="white"),
        legend = dict(
            title = dict(font = dict(color="white")),
            font = dict(color="white"))
    )

    st.plotly_chart(fig_segments, use_container_width=True)

st.markdown("---")

st.subheader("💡 Business Insights")

best_product = filtered_df.groupby("Description")["Revenue"].sum().idxmax()

best_country = filtered_df.groupby("Country")["Revenue"].sum().idxmax()

average_monthly_revenue = filtered_df.groupby("YearMonth")["Revenue"].sum().mean()

best_month = filtered_df.groupby("YearMonth")["Revenue"].sum().idxmax()

col1, col2 = st.columns(2)

with col1:

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #18243e, #111a2e);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 15px;
    ">
        <h4 style="color: #94a3b8;">🏆 Best Product</h4>
        <h3 style="color: white;">{best_product}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #18243e, #111a2e);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #06b6d4;
    ">
        <h4 style="color: #94a3b8;">🌍 Top Country</h4>
        <h2 style="color: white;">{best_country}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #18243e, #111a2e);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #8b5cf6;
        margin-bottom: 15px;
    ">
        <h4 style="color: #94a3b8;">📈 Best Sales Month</h4>
        <h2 style="color: white;">{best_month}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #18243e, #111a2e);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #f59e0b;
    ">
        <h4 style="color: #94a3b8;">💰 Average Monthly Revenue</h4>
        <h2 style="color: white;">£{average_monthly_revenue:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<hr>

<div style="text-align: center; color: #94a3b8; padding: 10px;">
    <p>Retail Sales & Customer Analytics Dashboard</p>
    <p>Built with Python, Pandas, Streamlit & Plotly</p>
</div>
""", unsafe_allow_html=True)