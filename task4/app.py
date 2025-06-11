from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kurama_0723@localhost/task4_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String, default='new')

@app.route("/")
def index():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    return render_template("index.html", incidents=incidents)

@app.route("/create", methods=["POST"])
def create_incident():
    data = request.form
    new_incident = Incident(
        title=data["title"],
        description=data["description"]
    )
    db.session.add(new_incident)
    db.session.commit()
    return jsonify(success=True)


@app.route("/resolve/<int:incident_id>", methods=["POST"])
def resolve_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    incident.status = "resolved"
    db.session.commit()
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
