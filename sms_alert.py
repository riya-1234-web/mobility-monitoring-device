from twilio.rest import Client

def send_sms_alert(to_number):
    account_sid = 'AC458a0ba2f6dbdf7666b60678226a6cea'
    auth_token = 'f1a727245654cdbb922b8070f9a4b839'
    twilio_number = '+19705928750'  # Your Twilio number

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="⚠️ Fall detected! Please check on the individual.",
        from_=twilio_number,
        to=to_number
    )

    print(f"SMS sent: {message.sid}")