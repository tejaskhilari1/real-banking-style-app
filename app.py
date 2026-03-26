from flask import Flask, render_template, request, jsonify, session, redirect

app = Flask(__name__)
app.secret_key = "secret123"

users = []

@app.route('/')
def home():
    return render_template('index.html')

# REGISTER API
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json

    user = {
        'name': data['name'],
        'phone': data['phone'],
        'password': data['password'],
        'balance': 500000,
        'account_no': "065910110006425",
        'ifsc': "SBIN0001234",
        'bank': "State Bank of India",
        'loan': "No Loan"
    }

    users.append(user)
    return jsonify({'message': 'Registered Successfully ✅'})

# LOGIN API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json

    for user in users:
        if user['phone'] == data['phone'] and user['password'] == data['password']:
            session['user'] = user   # store user in session
            return jsonify({'message': 'Login Success'})

    return jsonify({'error': 'Invalid Login'}), 401


# DASHBOARD PAGE
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    
    user = session['user']
    return render_template('dashboard.html', user=user)


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)