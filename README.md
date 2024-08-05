# Average Calorie Burned Calculator Microservice
This microservice calculates the average calories burned from workouts logged in a workouts.txt file. It provides an endpoint to retrieve this average in JSON format.

# Overview
The microservice reads data from a workouts.txt file and calculates the average calories burned across all workouts. It exposes a single endpoint to request this data.

# Request Instructions
To programmatically request the average calories burned, send an HTTP GET request to the following endpoint:

Endpoint
```
GET http://localhost:5000/average_calories
```

# Example Request
Here is an example of how to make this request using python
```
import requests

response = requests.get('http://localhost:5000/average_calories')
print(response.json())  # Prints the JSON response
```

# Response Instructions
The microservice responds with a JSON object containing the calculated average calories burned. The JSON response has the following format:

```
Copy code
{
    "average_calories": 125.0
}
```
average_calories: A floating-point number representing the average calories burned from all workouts in the workouts.txt file.

# Example Call
Below is a complete example of requesting and receiving data from the microservice using Python:

```
import requests

# Send a GET request to the microservice
response = requests.get('http://localhost:5000/average_calories')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(f"Average calories burned: {data['average_calories']:.2f}")
else:
    print("Failed to retrieve data from the microservice.")

```
    
# UML Sequence Diagram

![UML](https://github.com/user-attachments/assets/752954da-0cf4-4d64-a9d1-7ef918831d96)

