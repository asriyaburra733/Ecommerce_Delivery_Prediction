import streamlit as st
import requests
st.title("Ecommerce Delivery Predictions")

### Input Widgets
customer_gender = st.radio("Select Gender",['Male' ,'Female', 'Other'])
customer_city = st.selectbox("Select Customer City",['Los Angeles', 'San Diego', 'Dallas', 'Phoenix', 'San Antonio', 'Chicago',
 'New York', 'Philadelphia', 'Houston'])
customer_state = st.selectbox("Select Customer State",['CA' ,'TX' ,'AZ', 'IL', 'NY', 'PA'])
product_category = st.selectbox("Select Product Category",['Clothing', 'Books', 'Automotive','Toys', 'Home & Kitchen', 'Beauty',
 'Electronics', 'Sports'])
payment_method = st.selectbox("Select Payment Method",['Debit Card', 'Credit Card', 'UPI', 'Cash on Delivery', 'PayPal'])
order_priority = st.selectbox("Select Order Priority",['Medium', 'High', 'Low', 'Critical'])
seller_city = st.selectbox("Select Seller City",['Houston', 'Phoenix', 'San Antonio', 'New York', 'Dallas', 'Philadelphia',
 'San Diego', 'Los Angeles', 'Chicago'])
shipping_method = st.selectbox("Select Shipping Method",['Same-Day', 'Standard', 'Express', 'Economy'])
carrier = st.selectbox("Select Carrier",['OnTrac', 'UPS', 'USPS', 'DHL', 'FedEx'])
weather_condition = st.selectbox("Select Weather Condition",['Clear', 'Fog', 'Storm', 'Rain', 'Snow'])
traffic_level = st.selectbox("Select Traffic Level",['Low', 'Medium', 'Jam', 'High'])

customer_age=st.number_input("Customer Age",min_value=18,max_value=69,value=45,step=1)
customer_income=st.number_input("Customer Income",min_value=5210.84,max_value=461493.44,value=42718.80,step=0.1)
customer_rating=st.number_input("Customer Rating",min_value=1.0,max_value=5.0,value=2.9,step=0.1)
product_price=st.number_input("Product Price",min_value=5.0,max_value=575.81,value=137.54,step=0.1)
quantity=st.number_input("Quantity",min_value=1,max_value=9,value=1,step=1)
discount_percent=st.number_input("Discount Percent",min_value=0,max_value=30,value=0,step=1)
order_value=st.number_input("Order Value",min_value=3.5,max_value=1927.52,value=137.54,step=0.1)
seller_rating=st.number_input("Seller Rating",min_value=2.0,max_value=5.0,value=3.7,step=0.1)
seller_experience_years=st.number_input("Seller Experience Years",min_value=1,max_value=14,value=7,step=1)
seller_reliability_score=st.number_input("Seller Reliability Score",min_value=28.0,max_value=100.0,value=74.4,step=0.1)
warehouse_distance_km=st.number_input("Warehouse Distance in KM", min_value=10.0,max_value=3000.0,value=400.7,step=0.1)
package_weight_kg=st.number_input("Package Weight",min_value=0.1,max_value=40.05,value=2.66,step=0.1)
package_volume=st.number_input("Package Volume",min_value=20.0,max_value=17343.1,value=677.3,step=0.1)
processing_time_hours=st.number_input("Processing Time Hours",min_value=2.0,max_value=96.0,value=2.1,step=0.1)
dispatch_delay_hours=st.number_input("Dispatch Delay Hours",min_value=0.0,max_value=46.2,value=2.3,step=0.1)
estimated_delivery_days=st.number_input("Estimated Delivery Days",min_value=1,max_value=13,value=1,step=1)
holiday_period=st.number_input("Holiday Period",min_value=0,max_value=1,value=0,step=1)
weekend_order=st.number_input("Weekend Order",min_value=0,max_value=1,value=0,step=1)
peak_season=st.number_input("Peak Season",min_value=0,max_value=1,value=0,step=1)
distance_to_delivery_ratio=st.number_input("Distance to Delivery Ratio",min_value=1.43,max_value=499.95,value=400.7,step=0.1)
shipping_risk_score=st.number_input("Shipping Risk Score",min_value=0.2,max_value=37.0,value=3.4,step=0.1)
seller_performance_score=st.number_input("Seller Performance Score",min_value=31.6,max_value=100.0,value=74.3,step=0.1)
customer_order_frequency=st.number_input("Customer Order Frequency",min_value=1,max_value=15,value=3,step=1)
delivery_efficiency_score=st.number_input("Delivery Efficiency Score",min_value=22.4,max_value=99.0,value=97.3,step=0.1)
order_year=st.number_input(
    "Order Year",
    min_value=2020,
    max_value=2025,
    value=2025,
    step=1
)
order_month=st.number_input("Order Month",min_value=1,max_value=12,value=4,step=1)
order_day=st.number_input("Order Day",min_value=1,max_value=31,value=8,step=1)
order_dayofweek=st.number_input("Order Dayofweek",min_value=0,max_value=6,value=1,step=1)

###Prediction
if st.button("Delivery Prediction"):
    data={
     "customer_age":customer_age,
     "customer_gender":customer_gender,
     "customer_city":customer_city,
     "customer_state":customer_state,
     "customer_income":customer_income,
     "customer_rating":customer_rating,
     "product_category":product_category,
     "product_price":product_price,
     "quantity":quantity,
     "discount_percent":discount_percent,
     "order_value":order_value,
     "payment_method":payment_method,
     "order_priority":order_priority,
     "seller_rating":seller_rating,
     "seller_experience_years":seller_experience_years,
     "seller_city":seller_city,
     "seller_reliability_score":seller_reliability_score,
     "warehouse_distance_km":warehouse_distance_km,
     "shipping_method":shipping_method,
     "carrier":carrier,
     "package_weight_kg":package_weight_kg,
     "package_volume":package_volume,
     "processing_time_hours":processing_time_hours,
     "dispatch_delay_hours":dispatch_delay_hours,
     "estimated_delivery_days":estimated_delivery_days,
     "weather_condition":weather_condition,
     "traffic_level":traffic_level,
     "holiday_period":holiday_period,
     "weekend_order":weekend_order,
     "peak_season":peak_season,
     "distance_to_delivery_ratio":distance_to_delivery_ratio,
     "shipping_risk_score":shipping_risk_score,
     "seller_performance_score":seller_performance_score,
     "customer_order_frequency":customer_order_frequency,
     "delivery_efficiency_score":delivery_efficiency_score,
     "order_year":order_year,
     "order_month":order_month,
     "order_day":order_day,
     "order_dayofweek":order_dayofweek
    }

    try:
        response = requests.post(
                    "http://127.0.0.1:8000/predict",
                     json=data
            )
        if response.status_code==200:
            result=response.json()

            if result["prediction"]==1:
                st.warning("Late Delivery")
            else:
                st.success("On-Time Delivery")
    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running")
        