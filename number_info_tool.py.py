import phonenumbers
from phonenumbers import timezone, geocoder, carrier

try:
    phone = input("Enter your number with country code (e.g., +91xxxxxxxxx): ")
    number = phonenumbers.parse(phone)

    # Basic info extraction
    time = timezone.time_zones_for_number(number)
    cari = carrier.name_for_number(number, "en")
    registered = geocoder.description_for_number(number, "en")

    print(f"\n--- Phone Number Details ---")
    print(f"Parsed Number: {number}")
    print(f"Time Zone: {time}")
    print(f"Carrier/Operator: {cari}")
    print(f"Location: {registered}")

except Exception as e:
    print(f"Error: Could not parse the number. Please check the format. ({e})")