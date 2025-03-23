from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_number'

# Home route
@app.route('/')
def home():
    return render_template('scanner.html')

# Payment route
@app.route('/payment', methods=['GET'])
def payment():
    # Simulate payment
    cart = request.args.get('cart')
    total_price = request.args.get('total_price')

    # Send SMS
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your bill is ${total_price}. Thank you for dining with us!',
        from_=twilio_number,
        to='customer_phone_number'  # Replace with actual customer number
    )
    return "Payment successful! SMS sent."

if __name__ == '__main__':
    app.run(debug=True)