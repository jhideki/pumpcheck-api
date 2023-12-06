# workouts_routes.py
from flask import Blueprint, request, jsonify
from models import Workout, Exercise
from extensions import db

workouts_blueprint = Blueprint('workouts', __name__)

@workouts_blueprint.route('/api/getworkouts', methods=['GET'])
def get_workouts():
    # Retrieve all workouts
    workouts = Workout.query.all()
    return jsonify([workout.serialize() for workout in workouts])
    
@workouts_blueprint.route('/api/getworkout/<int:workout_id>', methods=['GET'])
def get_workout(workout_id):
    print(f"Received request for workout ID: {workout_id}")
    workout = Workout.query.get(workout_id)
    if workout:
        print(f"Found workout: {workout.serialize()}")
        return jsonify(workout.serialize()), 200
    else:
        print("Workout not found")
        return jsonify({'message': 'workout not retrieved'}), 404


@workouts_blueprint.route('/api/createworkout', methods=['POST'])
def create_workout():
    data = request.json
    print(data)
    user_id = data['user_id']
    date = data['date']
    time = data.get('time')

    workout = Workout(user_id=user_id, date=date, time=time)
    db.session.add(workout)
    db.session.commit()
    return jsonify({'message': 'Workout created successfully'})

@workouts_blueprint.route('/api/getexercise', methods=['GET'])
def get_exercises():
    # Retrieve all exercises
    exercises = Exercise.query.all()
    return jsonify([exercise.serialize() for exercise in exercises])

@workouts_blueprint.route('/api/createexercise', methods=['POST'])
def create_exercise():
    data = request.json
    workout_id = data['workout_id']
    exercise_name = data['exercise_name']
    number_of_reps = data.get('number_of_reps')
    weight = data.get('weight')

    exercise = Exercise(workout_id=workout_id, exercise_name=exercise_name, number_of_reps=number_of_reps, weight=weight)
    db.session.add(exercise)
    db.session.commit()
    return jsonify({'message': 'Exercise created successfully'})


