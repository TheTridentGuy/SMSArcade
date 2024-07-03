import TNAPI

client = TNAPI.Client("email", "pass", "Test")

client.send_sms("pn", "Hello World!")
