from twilio.rest import Client

account_sid = "AC44851c6e37f6fedea28ca497df856691"
auth_token = "a98259fa0418f8ac251d5393edfb7d6b"
call = client.calls.create(
    twilml="<Response><Say>Hello rinku</Say></Response>",
    to ="+918279805775",
    from="+91733587527"
)
print(call.sid)