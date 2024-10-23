import pickle
import json

with open('Car_Prediction_linear_reg_model.pkl', 'rb') as f:
    linear_model = pickle.load(f)

with open('column_data.json', 'r') as f:
    column_data = json.load(f)

def get_car_price(data):

    print("Data : ", data)

    Car_ID = float(data['Car ID'])
    # Brand = data['Car ID']
    Year = float(data['Year'])
    Engine_Size = float(data['Engine Size'])
    # Fuel_Type = data['Fuel Type']
    # Transmission =data['Transmission']
    Mileage = float(data['Mileage'])
    # Condition = data['Condition']
    # Model = eval(data['Model'])
    # Additional_Column = eval(data['Additional Column'])

     # Map categorical values using column_data.json
    Brand = column_data["Brand"][data['Brand']]
    Fuel_Type = column_data["Fuel Type"][data['Fuel Type']]
    Transmission = column_data["Transmission"][data['Transmission']]
    Condition = column_data["Condition"][data['Condition']]
    Model = column_data["Model"][data['Model']]
    
    test_array = [[Car_ID,Brand,Year,Engine_Size,Fuel_Type,Transmission,Mileage,Condition,Model]]
    price = linear_model.predict(test_array)[0]

    return price