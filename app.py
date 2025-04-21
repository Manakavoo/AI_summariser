#app.py
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from extractive_summarization import extractive_sum
from abstractive_summarization import abstractive_sum
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = "secret_key"  # Required for session handling
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Root route - redirect to login page
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login_page'))

# Login page route (GET) - renders the login template
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Login API endpoint (POST) - handles authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        session['user_id'] = user.id
        return jsonify({"Msg": "login-success"})
    return jsonify({"Msg": "login-failed", "error": "Invalid email or password"}), 401

# Registration API endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"Msg": "register-failed", "error": "Email already exists"}), 400

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"Msg": "register-success"})

# Home page (protected)
@app.route('/home')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            return render_template('home.html', user_name=user.name)
    return redirect(url_for('login_page'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login_page'))

# Example: Update error handling in the summarize route
@app.route('/summarize', methods=['POST'])
def summarize():
    logging.info("Connected to summarize endpoint")
    try:
        data = request.json
        text = data.get('text', '')
        summary_type = data.get('type')
        summary_size = data.get('size')
        
        if not text:
            logging.error("No text provided")
            return jsonify({
                'error': 'No text provided',
                'summary': ''
            }), 400

        if summary_type == 'extractive':
            summary = extractive_sum(text, summary_percentage=int(summary_size))
        elif summary_type == 'abstractive':
            summary = abstractive_sum(text, summary_percentage=int(summary_size))
        else:
            logging.error("Invalid summary type")
            return jsonify({
                'error': 'Invalid summary type',
                'summary': ''
            }), 400

        logging.info("Summarization successful")
        return jsonify({
            'summary': summary,
            'original_length': len(text.split()),
            'summary_length': len(summary.split())
        })

    except Exception as e:
        logging.exception("Error while summarizing")
        return jsonify({
            'error': 'An error occurred during summarization',
            'details': str(e)
        }), 500



if __name__ == '__main__':
    # Create the database tables if they don't exist yet
    with app.app_context():
        db.create_all()

    # Run the application
    port = int(os.environ.get("PORT", 5000))  # Render sets the port via the PORT environment variable
    app.run(host='0.0.0.0', port=port)