from twilio.rest import Client

#  gettting these keys from env file
account = "account_id"
token = "twillio_token"

client = Client(account, token)


def send_sms(number, message):
    try:
        sms = client.messages.create(to=str(number), from_="+xxxxxx", body=message)
        return sms
    except:
        return None


def group_sms(numbers, message):
    for number in numbers:
        try:
            sms = client.messages.create(to=str(number), from_="+xxxxxxx", body=message)
        except:
            continue
