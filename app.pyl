from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Your packages
PACKAGES = {
    15: {"name": "1 Hour", "duration": "1 Hour"},
    30: {"name": "3 Hours", "duration": "3 Hours"},
    50: {"name": "12 Hours", "duration": "12 Hours"},
    100: {"name": "24 Hours", "duration": "24 Hours"},
    250: {"name": "Weekly", "duration": "7 Days"}
}

# Function to send ORDINARY SMS (not promo)
def send_ordinary_sms(phone, message):
    try:
        if phone.startswith("0"):
            phone = "+254" + phone[1:]
        print(f"=== SMS TO {phone}: {message} ===")
        return True
    except Exception as e:
        print(f"SMS Error: {e}")
        return False

@app.route("/")
def home():
    return "LantechWifi Bot LIVE - Till 6684090 Ready!"

@app.route("/validation", methods=["POST"])
def validation():
    data = request.get_json()
    print(f"VALIDATION: {data}")
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})

@app.route("/confirmation", methods=["POST"])
def confirmation():
    data = request.get_json()
    print(f"CONFIRMATION: {data}")
    try:
        amount = int(float(data.get("TransAmount", 0)))
        phone = data.get("MSISDN", "")
        trans_id = data.get("TransID", "")
        first_name = data.get("FirstName", "Customer")

        pkg = PACKAGES.get(amount)
        if not pkg:
            msg = f"Hi {first_name}, LantechWifi got KES{amount} but package not found. Call 0726xxxxxx. {trans_id}"
            send_ordinary_sms(phone, msg)
            return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})

        password = f"{phone[-4:]}{amount}"
        
        msg = f"Hi {first_name}, LantechWifi: KES{amount} received. Package: {pkg['name']} ({pkg['duration']}). Voucher: {password}. Connect to LantechWifi WiFi to browse. {trans_id}"
        send_ordinary_sms(phone, msg)
        
    except Exception as e:
        print(f"Error: {e}")
    
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
