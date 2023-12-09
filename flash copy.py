from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# In a real application, you'd use a database (e.g., SQLAlchemy) instead of an in-memory list.
matches = [
    {"id": 1, "team_a": "Team A", "team_b": "Team B", "score_a": 0, "score_b": 0, "events": []},
    {"id": 2, "team_a": "Team X", "team_b": "Team Y", "score_a": 0, "score_b": 0, "events": []},
]

@app.route('/')
def index():
    return render_template('index.html', matches=matches)

@app.route('/update_scores/<int:match_id>')
def update_scores(match_id):
    match = next((match for match in matches if match["id"] == match_id), None)

    if match:
        new_score_a = match["score_a"] + random.randint(0, 5)
        new_score_b = match["score_b"] + random.randint(0, 5)

        # Simulate match events
        events = ['Goal by Team A', 'Yellow card for Team B', 'Substitution for Team A']
        random_event = random.choice(events)

        match["score_a"] = new_score_a
        match["score_b"] = new_score_b
        match["events"].insert(0, f'{datetime.now().strftime("%H:%M:%S")} - {random_event}')

        return jsonify({
            'teamAScore': new_score_a,
            'teamBScore': new_score_b,
            'matchEvents': match["events"]
        })

    return jsonify({"error": "Match not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
