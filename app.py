from flask import Flask, request, jsonify
import requests, base64

app = Flask(__name__)

CONSUMER_KEY = "h5C5wS3HKTv9bVqvgbqc1yU9MZPzuZ0yvBBHELNbUbutjC8Y"
CONSUMER_SECRET = "esmv2jvAFiAi8JLDGaguPvJPaSoMyZ10ZaJcqVf3iy2oFCjdOGZFb9tonGs9MKjY"
SHORTCODE = "6684090"
CONFIRMATION_URL = "https://lantechwifi-bot.onrender.com/confirmation"
VALIDATION_URL = "https://lantechwifi-bot.onrender.com/validation"

@app.route('/')
def home():
    return "LantechWifi Bot LIVE - Till 6684090 Ready! Go to /register"

@app.route('/validation', methods=['POST'])
def validation():
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})

@app.route('/confirmation', methods=['POST'])
def confirmation():
    data = request.json
    print("MPESA DATA:", data)
    return jsonify({"ResultCode": 0, "ResultDesc": "Success"})

@app.route('/register')
def register_urls():
    try:
        auth = base64.b64encode(f"{CONSUMER_KEY}:{CONSUMER_SECRET}".encode()).decode()
        r = requests.get("https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",
                         headers={"Authorization": f"Basic {auth}"})
        token = r.json().get('access_token')
        if not token:
            return r.json()
        payload = {
            "ShortCode": SHORTCODE,
            "ResponseType": "Completed",
            "ConfirmationURL": CONFIRMATION_URL,
            "ValidationURL": VALIDATION_URL
        }
        r2 = requests.post("https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl",
                           json=payload,
                           headers={"Authorization": f"Bearer {token}"})
        return r2.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
