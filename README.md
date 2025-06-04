# 🌆 Foodie Tour AI Workflow

Generate one-day foodie tours for major Indian cities combining real-time weather, iconic dishes, and top-rated restaurants, tailored for indoor or outdoor dining.

---

## 🚀 Features

- Fetches today’s weather via API
- Suggests indoor/outdoor dining based on weather
- Selects 3 iconic local dishes per city (Breakfast, Lunch, Dinner)
- Finds top-rated restaurants for each dish
- Adds local beverages, festivals, landmarks & clothing tips

---

## 🧠 How It Works

1. Uses a predefined city list
2. Fetches current weather data for each city
3. Determines dining setting (indoor/outdoor)
4. Matches dishes and restaurants per meal
5. Prints an itinerary with ratings and cultural info

---

## 🗂️ File Structure

- `main.py` — Orchestrates the workflow
- `weather.py` — Fetches weather data
- `tour_planner.py` — Contains restaurant info
- `foodie_utils.py` — Provides cultural info (beverages, festivals, landmarks, clothing)
- `cities.txt` (optional) — List of cities

---

## 🔧 Quick Start

```bash
git clone <repo-url>
cd foodie-tour-julep

# (Optional) create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt

python main.py
