from twilio.rest import Client
from django.conf import settings
import random
import os


# TWILIO_ACCOUNT_SID='AC323e8a44cca08c00d9243baa4095c5c9'
# TWILIO_AUTH_TOKEN='6e2ee5526bb8ff2d3f20c3824d654457'
# TWILIO_PHONE_NUMBER='+19852443536'

account_sid = 'AC323e8a44cca08c00d9243baa4095c5c9'
auth_token = '8cd941acb629b17e7550062fc1301f1a'

# secret = 'mJH6Y7BrSe08oS3O9H6G44yVQLbeWfBR'

twilio_phone_number = "+19852443536"



def send_otp(phone_number, otp):
    client = Client(account_sid, auth_token)

    message_body = f"Your one time OTP is: {otp}"

    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"OTP sent successfully to {phone_number}")
    except Exception as e:
        print(f"Failed to send OTP to {phone_number}. Error: {str(e)}")

    return message

# # Example usage
# phone_number = "+1234567890"  # Replace with the recipient's phone number
# otp = "123456"  # Replace with the generated OTP

# send_otp(phone_number, otp)
