def get_iconic_dishes(city_state):
    city = city_state.split(",")[0].strip()

    city_dishes = {
        "Mumbai": ["Vada Pav", "Pav Bhaji", "Bombay Sandwich"],
        "Delhi": ["Chole Bhature", "Butter Chicken", "Paranthas"],
        "Chennai": ["Dosa", "Idli", "Filter Coffee"],
        "Kolkata": ["Rosogolla", "Mishti Doi", "Kathi Roll"],
        "Bangalore": ["Mysore Masala Dosa", "Bisi Bele Bath", "Ragi Mudde"],
        "Hyderabad": ["Biryani", "Haleem", "Mirchi ka Salan"],
        "Pune": ["Misal Pav", "Sabudana Khichdi", "Bhakarwadi"],
        "Jaipur": ["Dal Baati Churma", "Ghewar", "Pyaaz Kachori"],
        "Lucknow": ["Tunday Kababi", "Korma", "Sheermal"],
        "Amritsar": ["Amritsari Kulcha", "Lassi", "Chole Kulche"],
        "Goa": ["Goan Fish Curry", "Feni", "Prawn Balchao"],
        "Udaipur": ["Dal Baati", "Gatte ki Sabzi", "Laal Maas"],
        "Varanasi": ["Kachori Sabzi", "Malaiyo", "Banarasi Paan"],
        "Mysore": ["Mysore Pak", "Ragi Roti", "Bisi Bele Bath"],
        "Shimla": ["Chana Madra", "Sidu", "Babru"]
    }
    return city_dishes.get(city, ["Local Dish 1", "Local Dish 2", "Local Dish 3"])

def get_local_beverages(city_state):
    city = city_state.split(",")[0].strip()

    beverages = {
        "Mumbai": ["Cutting Chai", "Sol Kadhi"],
        "Delhi": ["Lassi", "Nimbu Pani"],
        "Chennai": ["Filter Coffee", "Tender Coconut Water"],
        "Kolkata": ["Tea", "Aam Panna"],
        "Bangalore": ["Mysore Coffee", "Neer Mor"],
        "Hyderabad": ["Irani Chai", "Thandai"],
        "Pune": ["Masala Chai", "Sol Kadhi"],
        "Jaipur": ["Chaas", "Thandai"],
        "Lucknow": ["Khus Sherbet", "Thandai"],
        "Amritsar": ["Lassi", "Chaas"],
        "Goa": ["Feni", "Coconut Water"],
        "Udaipur": ["Jal Jeera", "Thandai"],
        "Varanasi": ["Banarasi Thandai", "Masala Chai"],
        "Mysore": ["Filter Coffee", "Butter Milk"],
        "Shimla": ["Apple Cider", "Ginger Tea"]
    }
    return beverages.get(city, ["Water", "Tea"])

def get_local_festivals(city_state):
    city = city_state.split(",")[0].strip()

    festivals = {
        "Mumbai": "Ganesh Chaturthi",
        "Delhi": "Diwali, Republic Day Parade",
        "Chennai": "Pongal",
        "Kolkata": "Durga Puja",
        "Bangalore": "Karaga Festival",
        "Hyderabad": "Bonalu",
        "Pune": "Ganesh Chaturthi",
        "Jaipur": "Teej Festival",
        "Lucknow": "Lucknow Mahotsav",
        "Amritsar": "Baisakhi",
        "Goa": "Carnival",
        "Udaipur": "Mewar Festival",
        "Varanasi": "Dev Deepawali",
        "Mysore": "Dasara",
        "Shimla": "Shimla Summer Festival"
    }
    return festivals.get(city, "Local Festival")

def get_landmarks(city_state):
    city = city_state.split(",")[0].strip()

    landmarks = {
        "Mumbai": "Gateway of India, Marine Drive",
        "Delhi": "Red Fort, India Gate",
        "Chennai": "Marina Beach, Kapaleeshwarar Temple",
        "Kolkata": "Victoria Memorial, Howrah Bridge",
        "Bangalore": "Lalbagh Botanical Garden, Bangalore Palace",
        "Hyderabad": "Charminar, Golconda Fort",
        "Pune": "Shaniwar Wada, Aga Khan Palace",
        "Jaipur": "Hawa Mahal, Amber Fort",
        "Lucknow": "Bara Imambara, Rumi Darwaza",
        "Amritsar": "Golden Temple, Jallianwala Bagh",
        "Goa": "Baga Beach, Basilica of Bom Jesus",
        "Udaipur": "City Palace, Lake Pichola",
        "Varanasi": "Kashi Vishwanath Temple, Ghats",
        "Mysore": "Mysore Palace, Chamundi Hill",
        "Shimla": "The Ridge, Jakhoo Temple"
    }
    return landmarks.get(city, "Famous local spots")

def get_clothing_advice(weather):
    temp = weather.get("temp", 25)  # Celsius
    condition = weather.get("condition", "").lower()

    if temp >= 30:
        advice = "Light cotton clothes, sunscreen, and a hat."
    elif 20 <= temp < 30:
        advice = "Comfortable casuals, light jacket for evenings."
    elif 10 <= temp < 20:
        advice = "Warm clothes like sweaters and jackets."
    else:
        advice = "Heavy woolens, scarves, and gloves."

    if "rain" in condition:
        advice += " Don't forget an umbrella or raincoat!"

    return advice
