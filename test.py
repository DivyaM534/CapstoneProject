import requests
 
# Example car specs
car = {
    "cylinders": 6,
    "displacement": 200.0,
    "horsepower": 105.0,
    "weight": 3100.0,
    "acceleration": 14.2,
    "model_year": 78,
    "origin": 2
}
 
url = 'http://localhost:9696/predict'
response = requests.post(url, json=car)
 
print("Prediction response:", response.json())