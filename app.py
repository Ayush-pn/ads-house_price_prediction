# app.py
import gradio as gr
import util

util.load_saved_artifacts()

def predict_price(sqft, bath, bhk, location):
    return f"Estimated Price: ₹ {util.get_estimated_price(location, sqft, bhk, bath)} lakhs"

locations = util.get_location_names()

demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Total Sqft"),
        gr.Number(label="Bathrooms"),
        gr.Number(label="BHK"),
        gr.Dropdown(locations, label="Location")
    ],
    outputs=gr.Textbox(label="Estimated Price"),
    title="Bangalore Home Price Prediction",
    description="Enter the details of the property to get the estimated price."
)

demo.launch()
