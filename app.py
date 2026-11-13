from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app=FastAPI(title="Ecommerce Delivery Predictions")

model=joblib.load("ecommerce_delivery_predictions.pkl")

class Ecommerce_delivery(BaseModel):
    customer_age:int
    customer_gender:str
    customer_city:str
    customer_state:str
    customer_income:float
    customer_rating:float
    product_category:str
    product_price:float
    quantity:int
    discount_percent:int
    order_value:float
    payment_method:str
    order_priority:str
    seller_rating:float
    seller_experience_years:int
    seller_city:str
    seller_reliability_score:float
    warehouse_distance_km:float
    shipping_method:str
    carrier:str
    package_weight_kg:float
    package_volume:float
    processing_time_hours:float
    dispatch_delay_hours:float
    estimated_delivery_days:int
    weather_condition:str
    traffic_level:str
    holiday_period:int
    weekend_order:int
    peak_season:int
    distance_to_delivery_ratio:float
    shipping_risk_score:float
    seller_performance_score:float
    customer_order_frequency:int
    delivery_efficiency_score:float
    order_year:int
    order_month:int
    order_day:int
    order_dayofweek:int

    ### Prediction 
@app.get("/")
def home():
    return {
        "message": "Welcome to Ecommerce Delivery Prediction API",
        "status": "FastAPI is running successfully"
    }
@app.post("/predict")
def predict(data:Ecommerce_delivery):
        input_data = pd.DataFrame([{
            "customer_age": data.customer_age,
            "customer_gender": data.customer_gender,
            "customer_city": data.customer_city,
            "customer_state": data.customer_state,
            "customer_income": data.customer_income,
            "customer_rating": data.customer_rating,
            "product_category": data.product_category,
            "product_price": data.product_price,
            "quantity": data.quantity,
            "discount_percent": data.discount_percent,
            "order_value": data.order_value,
            "payment_method": data.payment_method,
            "order_priority": data.order_priority,
            "seller_rating": data.seller_rating,
            "seller_experience_years": data.seller_experience_years,
            "seller_city": data.seller_city,
            "seller_reliability_score": data.seller_reliability_score,
            "warehouse_distance_km": data.warehouse_distance_km,
            "shipping_method": data.shipping_method,
            "carrier": data.carrier,
            "package_weight_kg": data.package_weight_kg,
            "package_volume": data.package_volume,
            "processing_time_hours": data.processing_time_hours,
            "dispatch_delay_hours": data.dispatch_delay_hours,
            "estimated_delivery_days": data.estimated_delivery_days,
            "weather_condition": data.weather_condition,
            "traffic_level": data.traffic_level,
            "holiday_period": data.holiday_period,
            "weekend_order": data.weekend_order,
            "peak_season": data.peak_season,
            "distance_to_delivery_ratio": data.distance_to_delivery_ratio,
            "shipping_risk_score": data.shipping_risk_score,
            "seller_performance_score": data.seller_performance_score,
            "customer_order_frequency": data.customer_order_frequency,
            "delivery_efficiency_score": data.delivery_efficiency_score,
            "order_year": data.order_year,
            "order_month": data.order_month,
            "order_day": data.order_day,
            "order_dayofweek": data.order_dayofweek
}])
        prediction = int(model.predict(input_data)[0])

        print("Prediction:", prediction)

        result = "Late Delivery" if prediction == 1 else "On-Time Delivery"

        print("Result:", result)

        return {
    "prediction": prediction,
    "result": result
    }
