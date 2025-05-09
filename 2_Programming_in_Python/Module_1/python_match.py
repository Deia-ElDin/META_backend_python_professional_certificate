http_status = 200

print ("\nUsing if else statements:")
if http_status == 200 or http_status == 201:
    print("Success")
elif http_status == 400:
    print("Bad Request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500 or http_status == 501:
    print("Server Error")
else:
    print("Unknown")

print ("\nUsing match statements:")
match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")

print ("\nUsing a dictionary:")
status_messages = {
    200: "Success",
    201: "Success",
    400: "Bad Request",
    404: "Not Found",
    500: "Server Error",
    501: "Server Error",
}

print(status_messages.get(http_status, "Unknown"))

