from flask import Flask, request, redirect, url_for, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/booking')
def booking():
    return send_from_directory('.', 'booking.html')

@app.route('/book', methods=['POST'])
def book():
    data = request.form.to_dict()
    print('Booking request received:', data)
    return 'Thanks! Your booking request has been submitted. We will contact you soon.'

if __name__ == '__main__':
    app.run(debug=True)
