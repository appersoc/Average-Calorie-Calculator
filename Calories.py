from flask import Flask, jsonify

app = Flask(__name__)


def parse_workouts(file_path):
    workouts = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 4:
                date, workout_name, duration, calories = parts
                workouts.append({
                    'date': date.strip(),
                    'workout_name': workout_name.strip(),
                    'duration': int(duration.strip()),
                    'calories': int(calories.strip())
                })
    return workouts


def calculate_average_calories(workouts):
    total_calories = sum(workout['calories'] for workout in workouts)
    num_workouts = len(workouts)
    if num_workouts == 0:
        return 0
    return total_calories / num_workouts


@app.route('/average_calories', methods=['GET'])
def get_average_calories():
    workouts = parse_workouts('workouts.txt')
    average_calories = calculate_average_calories(workouts)
    return jsonify({
        'average_calories': average_calories
    })


if __name__ == '__main__':
    app.run(debug=True)
