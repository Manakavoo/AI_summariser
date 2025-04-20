
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from extractive_summarization import extractive_sum

from abstractive_summarization import abstractive_sum
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
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

# Home Page
@app.route('/')
def index():
    {"Response": "connected sucessfully"}
    # return render_template('login.html')


# Registration Route
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

# Login Route
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

# Protected Home Page (After Login)
@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

# Logout Route
@app.route('/logout')
def logout():
    print("logout")
    session.clear()
    session.pop('user_id', None)
    return redirect(url_for('index'))
    # return render_template('login.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    print("connected to summarize")
    data = request.json
    
    text = data.get('text', '')
    summary_type = data.get('type')
    summary_size = data.get('size')
    print(summary_type,summary_size)
    if not text:
        return jsonify({
            'error': 'No text provided',
            'summary': ''
        }), 400
    
    if summary_type == 'extractive':
        summary = extractive_sum(text,summary_percentage=int(summary_size))

    elif summary_type == 'abstractive':
        summary = abstractive_sum(text,summary_percentage=int(summary_size))

    else:
        return jsonify({
            'error': 'Invalid summary type',
            'summary': ''
        }), 400
    
    return jsonify({
        'summary': summary,
        'original_length': len(text.split()),
        'summary_length': len(summary.split())
    })

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  
#     app.run(debug=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host='0.0.0.0', port=port, debug=True)

