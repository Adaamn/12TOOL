import requests

def pubIPCheck():
    try:
        getInfo = (f"https://ipwho.is/")
        publicIP = requests.get(getInfo, timeout=10)
        data = publicIP.json()

        ip = data.get("ip")
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        connection = data.get("connection")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        print("\n--- PUBLIC INFO ---")
        print(f"\nYour public IP: {ip}")
        print(f"Your location: {latitude}, {longitude}")
        print(f"Your city: {city}, {region}, {country}")
        print(f"Your ISP: {connection['isp']}, {connection['domain']}")
        print(f"Map link: {maps_url}")


    except requests.exceptions.ConnectionError:
        print("You are offline.")
    except requests.exceptions.Timeout:
        print("Server is responding too slowly.")
    except Exception as e:
        print(f"There is something wrong - {e}")