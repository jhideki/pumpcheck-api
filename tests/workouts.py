import json
import requests

base_url = 'http://ec2-3-129-61-246.us-east-2.compute.amazonaws.com:5000/workouts'  # Update with your server's URL

def test_get_workouts():
    url = f'{base_url}/api/getworkouts'
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

def test_get_workout():
    url = f'{base_url}/api/getworkout/2'
    response = requests.get(url)
    print(response.json())

def test_create_workout():
    url = f'{base_url}/api/createworkout'
    data = {'user_id': 11, 'date': '2023-01-01', 'time': '12:00 PM'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.status_code)
    print(response.json())

def test_get_exercises():
    url = f'{base_url}/api/getexercise'
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

def test_create_exercise():
    url = f'{base_url}/api/createexercise'
    data = {'workout_id': 1, 'exercise_name': 'Push-ups', 'number_of_reps': 10, 'weight': 20}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.status_code)
    print(response.json())

if __name__ == '__main__':
    #test_create_workout()

    test_get_workout()
    #test_get_exercises()
    #test_create_exercise()
