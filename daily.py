import random

member = ["Graham", 'Alex', "Melenie"]
def band_notices(member, band_name):
    text = f"""
    kia Ora,
    Greeting to you all,
    we will announce our band {band_name}, our performer are: {member}
    we will have a performance coming in next month
    """
    return text

professor = ["Graham", "Alex", "Melenie"]

for member in "performer":
    print(band_notices("performer", band_name="Hello Rock"))


def calculate_ticket_price(category):  
    if category == "standard":
       return 50.00
    elif category == "premium":
       return 75.00
    elif category == "vip":
        return 100.00
    else: 
        return "Invalid category" 


ticket_price = calculate_ticket_price("premium")
print("ticket_price:",ticket_price)

