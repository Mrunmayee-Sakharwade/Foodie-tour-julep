from tour_planner import restaurant_info
from weather import get_weather, is_outdoor_friendly
from foodie_utils import get_local_beverages, get_local_festivals, get_landmarks, get_clothing_advice
import random  # Move import here at top
from weather import get_weather_mood_quote
import shutil

# The dishes by city dict should be here or imported similarly
dishes_by_city = {
    "Mumbai": ["Vada Pav", "Pav Bhaji", "Bombay Sandwich"],
    "Delhi": ["Paratha", "Chole Bhature", "Butter Chicken"],
    "Chennai": ["Idli", "Dosa", "Chettinad Chicken"],
    "Kolkata": ["Luchi", "Shorshe Ilish", "Mutton Kosha"],
    "Bangalore": ["Masala Dosa", "Bisi Bele Bath", "Mysore Pak"],
    "Hyderabad": ["Hyderabadi Biryani", "Mirchi ka Salan", "Double ka Meetha"],
    "Pune": ["Misal Pav", "Bhakarwadi", "Sabudana Khichdi"],
    "Jaipur": ["Kachori", "Dal Baati Churma", "Laal Maas"],
    "Lucknow": ["Tunday Kababi", "Lucknawi Biryani", "Kulfi"],
    "Amritsar": ["Amritsari Kulcha", "Makki di Roti Sarson da Saag", "Lassi"],
    "Goa": ["Poi Bhaji", "Goan Prawn Curry", "Bebinca"],
    "Udaipur": ["Dal Baati Churma", "Gatte ki Sabzi", "Lal Maas"],
    "Varanasi": ["Kachori Sabzi", "Tamatar Chaat", "Malaiyo"],
    "Mysore": ["Mysore Masala Dosa", "Ragi Mudde", "Mysore Pak"],
    "Shimla": ["Channa Madra", "Babru", "Sidu"]
}


def create_foodie_tour(city, weather, city_dishes, restaurants):
    is_outdoor = is_outdoor_friendly(weather)
    setting = "outdoor dining" if is_outdoor else "indoor dining"
    mood_quote = get_weather_mood_quote(weather["condition"])

    print(f"\n{'═' * 60}")
    print(f"         🍴  FOODIE TOUR: \033[1m{city.upper()}\033[0m  🍴")
    print(f"{'═' * 60}\n")

    print(f"🌤️  Weather: {weather['condition']} | {weather['temp']}°C")
    print(f"💬 Mood: {mood_quote}\n")

    print("🍽️  MEAL PLAN")
    print("----------------------------------------------------")

    for i, meal in enumerate(["BREAKFAST", "LUNCH", "DINNER"]):
        dish = city_dishes[i] if i < len(city_dishes) else "Dish"
        restaurant = restaurants[i] if i < len(restaurants) else {"name": "Local Eatery", "map_link": "#", "rating": "N/A"}
        rating = restaurant.get("rating", "N/A")
        print(f"🍳 {meal}")
        print(f"   • Dish       : {dish}")
        print(f"   • Restaurant : {restaurant['name']} ({rating}⭐)")
        print(f"   • Setting    : Ideal for {setting}")
        print(f"   • 📍 Map Link : {restaurant['map_link']}\n")

    print("🧃 LOCAL BEVERAGES")
    print("----------------------------------------------------")
    for drink in get_local_beverages(city):
        print(f"• {drink}")

    print("\n🎊 FESTIVAL SPOTLIGHT")
    print("----------------------------------------------------")
    print(f"• {get_local_festivals(city)}")

    print("\n📍 LANDMARKS TO VISIT")
    print("----------------------------------------------------")
    print(f"• {get_landmarks(city)}")

    print("\n👗 CLOTHING TIP")
    print("----------------------------------------------------")
    print(f"• {get_clothing_advice(weather)}")

    print(f"\n{'═' * 60}\n")


if __name__ == "__main__":
    # List of cities without states (or you can keep states if get_weather needs full names)
    cities = [
        "Mumbai", "Delhi", "Chennai", "Kolkata", "Bangalore",
        "Hyderabad", "Pune", "Jaipur", "Lucknow", "Amritsar",
        "Goa", "Udaipur", "Varanasi", "Mysore", "Shimla"
    ]

    for city in cities:
        weather = get_weather(city)
        city_dishes = dishes_by_city.get(city, ["Dish1", "Dish2", "Dish3"])

        # Get restaurants and assign random rating if missing
        raw_restaurants = restaurant_info.get(city, [
            {"name": "Local Eatery", "map_link": "#"} for _ in range(3)
        ])
        restaurants = []
        for r in raw_restaurants:
            rating = r.get("rating") or round(random.uniform(3.9, 4.4), 1)
            restaurants.append({
                "name": r["name"],
                "map_link": r["map_link"],
                "rating": rating
            })

        create_foodie_tour(city, weather, city_dishes, restaurants)
