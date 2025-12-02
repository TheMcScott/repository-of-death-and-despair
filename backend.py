from flask import Flask, render_template

app = Flask(__name__)

# yeah i just hardcoded the table in, idek what to put tho 😭
fixtures = [
    {"date": "2025-12-06", "opponent": "zurt", "venue": "Home", "time": "14:00"},
    {"date": "2025-12-13", "opponent": "jurt", "venue": "Away", "time": "15:00"},
    {"date": "2025-12-20", "opponent": "gurt", "venue": "Home", "time": "14:30"},
]

@app.route("/")
def fixtures_page():
    return render_template("fixtures.html", fixtures=fixtures)

if __name__ == "__main__":
    app.run(debug=True)
