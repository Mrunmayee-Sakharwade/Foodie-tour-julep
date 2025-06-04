def create_foodie_tour(city, weather, dishes, restaurant_info):
    condition = weather.get("condition", "Unknown").lower()
    temp = weather.get("temp", 25)
    dining_type = "outdoor" if condition in ["sunny", "clear", "partly cloudy"] and temp < 35 else "indoor"

    meals = ["Breakfast", "Lunch", "Dinner"]
    restaurants = restaurant_info.get(city, [
        {"name": f"{dish} Restaurant", "map_link": f"https://www.google.com/maps/search/{dish.replace(' ', '+')}+in+{city.replace(' ', '+')}"}
        for dish in dishes
    ])

    tour_html = f"<h2>🍽️ Foodie Tour for {city}</h2>\n"
    tour_html += f"<p>🌤️ Weather: {weather['condition']}, {weather['temp']}°C</p>\n"
    tour_html += "<ul>\n"

    for i in range(3):
        meal = meals[i]
        dish = dishes[i]
        restaurant = restaurants[i]

        tour_html += (
            f"<li><b>{meal}</b>: Enjoy <b>{dish}</b> at <i>{restaurant['name']}</i> (4.8⭐), "
            f"ideal for {dining_type} dining. "
            f"<a href=\"{restaurant['map_link']}\" target=\"_blank\">📍 Map Link</a></li>\n"
        )

    tour_html += "</ul>\n"
    return tour_html



restaurant_info = {
    "Mumbai": [
        {"name": "Priym The Taste of Spices Best Vada Pav & Chana Poha with Original taste", "map_link": "https://www.google.co.in/maps/place/Priym+The+Taste+of+Spices+Best+Vada+Pav+%26+Chana+Poha+with+Original+taste/@21.1166921,79.0509363,15z/data=!4m10!1m2!2m1!1sfamous+vada+pav!3m6!1s0x3bd4bfef79318dbf:0x5eae042440daffdd!8m2!3d21.1166921!4d79.0699907!15sCg9mYW1vdXMgdmFkYSBwYXZaESIPZmFtb3VzIHZhZGEgcGF2kgEKcmVzdGF1cmFudKoBYgoJL20vMDNqejJxCgkvbS8wZmc2Nl8QASoTIg9mYW1vdXMgdmFkYSBwYXYoADIeEAEiGottYqKbpfU-oYpDP4pNVLl348U55b4pKGymMhMQAiIPZmFtb3VzIHZhZGEgcGF24AEA!16s%2Fg%2F11w382dm8_?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "The Breakfast Story", "map_link": "https://www.google.co.in/maps/place/The+Breakfast+Story/@21.1232894,79.0298492,15z/data=!4m10!1m2!2m1!1spav+bhaji!3m6!1s0x3bd4c009231b7585:0x5a99384c6b8cbda7!8m2!3d21.1232894!4d79.0386039!15sCglwYXYgYmhhamlaCyIJcGF2IGJoYWppkgEUYnJlYWtmYXN0X3Jlc3RhdXJhbnSqAWAKCS9tLzA3MXhicwoIL20vMDk3MjgKCS9tLzBjampiNxABKg0iCXBhdiBiaGFqaSgAMh4QASIaCnAoZ2LYwNi298NAmadTLbkWhw0xR0j7Ys0yDRACIglwYXYgYmhhamngAQA!16s%2Fg%2F1pycnqtlm?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Haldiram Express", "map_link": "https://www.google.co.in/maps/place/Haldirams+Express/@21.1185182,79.0097158,15z/data=!4m10!1m2!2m1!1sbombay+sandwich!3m6!1s0x3bd4eaaabd9ad69d:0x832404469f3e59cc!8m2!3d21.1185182!4d79.0184705!15sCg9ib21iYXkgc2FuZHdpY2haESIPYm9tYmF5IHNhbmR3aWNokgERZmFtaWx5X3Jlc3RhdXJhbnSqAU8KCC9tLzBsNTE1EAEqDCIIc2FuZHdpY2goADIeEAEiGsC_aVOawARwXPhGLlhB_BvVXNZCZ1oomOuLMhMQAiIPYm9tYmF5IHNhbmR3aWNo4AEA!16s%2Fg%2F11g8n3_1kh?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Delhi": [
        {"name": "Moti Mahal", "map_link": "https://www.google.co.in/maps/place/Moti+Mahal+Restaurant/@28.6464743,77.2401149,17z/data=!3m1!4b1!4m6!3m5!1s0x390cfd2076d5d8a7:0xfc425590701a73a6!8m2!3d28.6464743!4d77.2401149!16s%2Fg%2F11b6nvwh1v?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Sita Ram Diwan Chand", "map_link": "https://www.google.co.in/maps/place/Sita+Ram+Diwan+Chand/@28.6423797,77.2104046,3a,75y,90t/data=!3m8!1e2!3m6!1sCIHM0ogKEICAgICBsJ_WvQE!2e10!3e12!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-cs-s%2FAC9h4np4Py5X27PHfxv2qYf7gXA1YYFn1asUpfrxGTNk8AKRMUUFQNmCfCmNWiLjbJ_7hxMKvFbuQAsqjZ7A7L90L-J_bVpGcVl6_2WQC4rLNqDOTqGBd0uYT1mNw_a8NJUNglGT6QRgvg%3Dw109-h195-k-no!7i2268!8i4032!4m7!3m6!1s0x390cfd3ec19dcea9:0x16328da9306ecf22!8m2!3d28.6423777!4d77.210355!10e9!16s%2Fg%2F1tffh4fw?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Khan Chacha", "map_link": "https://www.google.co.in/maps/place/Khan+Chacha/@28.6423797,77.2104046,15z/data=!4m10!1m2!2m1!1sKhan+Chacha!3m6!1s0x390cfd37718406f3:0x2a7b2700fac0652a!8m2!3d28.6340784!4d77.2208397!15sCgtLaGFuIENoYWNoYVoNIgtraGFuIGNoYWNoYZIBEWluZGlhbl9yZXN0YXVyYW50qgFDCg0vZy8xMWR4OF9qMWZuEAEyHxABIhvBQjCYhuekSgeemw0OImwEK9TXJzJCA4V9FoMyDxACIgtraGFuIGNoYWNoYeABAA!16s%2Fg%2F11g6xtxwds?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],

    "Chennai": [
        {"name": "Murgan Idli Shop", "map_link": "https://www.google.co.in/maps/place/Murugan+Idli+Shop/@13.0453721,80.1628196,12z/data=!4m10!1m2!2m1!1smurugan+idli+shop+chennai!3m6!1s0x3a526657e647c8df:0x2daa5507e1a5bf4d!8m2!3d13.0453721!4d80.2328574!15sChltdXJ1Z2FuIGlkbGkgc2hvcCBjaGVubmFpWhsiGW11cnVnYW4gaWRsaSBzaG9wIGNoZW5uYWmSARdzb3V0aF9pbmRpYW5fcmVzdGF1cmFudKoBWBABKhUiEW11cnVnYW4gaWRsaSBzaG9wKAAyHhABIhp_976sFWx5mmDT1_kzUqDh9cXCMMiZxn8fLDIdEAIiGW11cnVnYW4gaWRsaSBzaG9wIGNoZW5uYWngAQA!16s%2Fg%2F1wn_4jk0?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Sree Dosa", "map_link": "https://www.google.co.in/maps/place/Shri+Balaajee+Bhavan/@13.0453721,80.1628196,12z/data=!4m10!1m2!2m1!1ssree+dosa+chennai!3m6!1s0x3a52665655555555:0xd9bf90d1c96d17f7!8m2!3d13.040914!4d80.2379507!15sChFzcmVlIGRvc2EgY2hlbm5haVoTIhFzcmVlIGRvc2EgY2hlbm5haZIBF3NvdXRoX2luZGlhbl9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVF0TFZrM1NHbFJSUkFCqgFEEAEqCCIEZG9zYSgAMh8QASIbwbP0zD3GDWpQfbaWWWz_sc3V8af2Qo1c5gm-MhUQAiIRc3JlZSBkb3NhIGNoZW5uYWngAQD6AQQILxBM!16s%2Fg%2F1tdw6gr0?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Chettinad Chicken", "map_link": "https://www.google.co.in/maps/place/Kaaraikudi+Chettinad+Restaurant/@13.0448004,80.1943792,12z/data=!3m1!5s0x3a526631cb13a23d:0x9acedb0fa34c9da7!4m10!1m2!2m1!1schettinad+chicken+chennai!3m6!1s0x3a5267f64eb6a935:0xba839228a7996f6c!8m2!3d13.0448004!4d80.264417!15sChljaGV0dGluYWQgY2hpY2tlbiBjaGVubmFpWhsiGWNoZXR0aW5hZCBjaGlja2VuIGNoZW5uYWmSARVjaGV0dGluYWRfcmVzdGF1cnRhbnSqAXAKCy9tLzAxMHI1bnJiCggvbS8wOWI1dBABKhUiEWNoZXR0aW5hZCBjaGlja2VuKAAyHxABIhs-cyAZL3Ow6m3IdYzjoiVcWWgL8-SsgnjqthkyHRACIhljaGV0dGluYWQgY2hpY2tlbiBjaGVubmFp4AEA!16s%2Fg%2F11rtmw7ts_?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Kolkata": [
        {"name": "Arsalan", "map_link": "https://www.google.co.in/maps/place/Arsalan+Restaurant+%26+Caterer/@22.5541333,88.2842361,12z/data=!4m10!1m2!2m1!1sarsalan+kolkata!3m6!1s0x3a0277056d20d12b:0x8b33d02863c817fb!8m2!3d22.5541333!4d88.3542739!15sCg9hcnNhbGFuIGtvbGthdGEiA4gBAVoRIg9hcnNhbGFuIGtvbGthdGGSARJtdWdobGFpX3Jlc3RhdXJhbnSqAVMKDS9nLzExaDE1eHl0aHgQASoLIgdhcnNhbGFuKAAyHhABIhrJBtfvdk47x8PiRCUettLmJJ1HFaZDV35QuDITEAIiD2Fyc2FsYW4ga29sa2F0YeABAA!16s%2Fg%2F1q5gnh9g6?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Bhojohori Manna", "map_link": "https://www.google.co.in/maps/place/Bhojohori+Manna/@22.5537772,88.2844047,12z/data=!4m10!1m2!2m1!1sbhojohori+manna+kolkata!3m6!1s0x3a02772a4595e8c1:0xaa0897d79fc6df80!8m2!3d22.5203221!4d88.3610458!15sChdiaG9qb2hvcmkgbWFubmEga29sa2F0YSIDiAEBWhkiF2Job2pvaG9yaSBtYW5uYSBrb2xrYXRhkgESYmVuZ2FsaV9yZXN0YXVyYW50qgFxCg0vZy8xMWI4MjV4azVqCgwvZy8xcHp4OHo1bGMQASoTIg9iaG9qb2hvcmkgbWFubmEoADIeEAEiGroUEnqF8kN45hMwBAgHSkbAtUW8ynz18I-PMhsQAiIXYmhvam9ob3JpIG1hbm5hIGtvbGthdGHgAQA!16s%2Fg%2F1tf38z1g?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "6 Ballygunge Place", "map_link": "https://www.google.co.in/maps/place/6+Ballygunge+Place/@22.5277856,88.3665365,17z/data=!4m10!1m2!2m1!1s6+Ballygunge+Place!3m6!1s0x3a0276d0a2583ccf:0xf1efff5c088752e2!8m2!3d22.5277856!4d88.3687252!15sChI2IEJhbGx5Z3VuZ2UgUGxhY2UiA4gBAVoUIhI2IGJhbGx5Z3VuZ2UgcGxhY2WSARJiZW5nYWxpX3Jlc3RhdXJhbnSqAUkKDS9nLzExZmxsN3dwaGcQATIeEAEiGuFUZAB2pgGdGcH-HOSUOqvCQ_wwqLj0Mrc0MhYQAiISNiBiYWxseWd1bmdlIHBsYWNl4AEA!16s%2Fg%2F11ggs2h1nl?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],

    "Bangalore": [
        {"name": "CTR (Central Tiffin Room)", "map_link": "https://www.google.co.in/maps/place/Central+Tiffin+Room/@12.9980955,77.569557,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae1625bc6a63f3:0x6941d824e3c07d0b!8m2!3d12.9980955!4d77.569557!16s%2Fm%2F0gfdq9p?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "MTR", "map_link": "https://www.google.co.in/maps/place/MTR/@12.9551821,77.5855569,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae15dda4a3a569:0xde94c3a7899fc902!8m2!3d12.9551821!4d77.5855569!16s%2Fg%2F1td_93bg?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Guru Sweets", "map_link": "https://www.google.co.in/maps/place/Sri+Guru+Sweets+Mart+(SGS)/@12.9752478,77.6247552,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae169958905677:0xf17cea86509ecc06!8m2!3d12.9752478!4d77.6247552!16s%2Fg%2F11bbrhtp9x?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Hyderabad": [
        {"name": "Paradise Biryani", "map_link": "https://www.google.co.in/maps/place/Paradise+Biryani+%7C+Secunderabad/@17.4417141,78.3471397,11z/data=!4m10!1m2!2m1!1sparadise+biryani+hyderabad!3m6!1s0x3bcb9a0f8cf1fd1b:0x386e919f25da1d16!8m2!3d17.4417141!4d78.4872154!15sChpwYXJhZGlzZSBiaXJ5YW5pIGh5ZGVyYWJhZCIDiAEBWhwiGnBhcmFkaXNlIGJpcnlhbmkgaHlkZXJhYmFkkgERZmFtaWx5X3Jlc3RhdXJhbnSqAXIKDS9nLzExaDE1eHhybHEKCS9tLzA3NGN2ZBABKhQiEHBhcmFkaXNlIGJpcnlhbmkoADIeEAEiGqBT3WO6KKOlbCMeJVJiriQ-5imdDVmOGfQmMh4QAiIacGFyYWRpc2UgYmlyeWFuaSBoeWRlcmFiYWTgAQA!16s%2Fg%2F1tfrkt3d?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Cafe Bahar", "map_link": "https://www.google.co.in/maps/place/Cafe+Bahar/@17.3997904,78.4785849,17z/data=!3m1!4b1!4m6!3m5!1s0x3bcb99dedd100a5f:0x11db7ba676dd7b7!8m2!3d17.3997904!4d78.4785849!16s%2Fm%2F0h3m8qm?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Bawarchi", "map_link": "https://www.google.co.in/maps/place/Bawarchi+Restaurant/@17.406627,78.4976861,17z/data=!3m1!4b1!4m6!3m5!1s0x3bcb99eab388910b:0x7c7c5b397008290!8m2!3d17.406627!4d78.4976861!16s%2Fg%2F1td4sr1c?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],

    "Pune": [
        {"name": "Bedekar Tea Stall", "map_link": "https://www.google.co.in/maps/place/Bedekar+Misal/@18.5148471,73.8499297,17z/data=!3m1!4b1!4m6!3m5!1s0x3bc2c0712045a1c9:0x23a1942274e443f0!8m2!3d18.5148471!4d73.8499297!16s%2Fg%2F1trswfwh?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Chitale Bandhu", "map_link": "https://www.google.co.in/maps/place/Chitale+Bandhu+-+Bajirao+Road/@18.5135379,73.8449411,15z/data=!4m10!1m2!2m1!1schitle+bandhu+pune!3m6!1s0x3bc2c071715bae3f:0xdc65d78bb4762a95!8m2!3d18.5135379!4d73.8536958!15sChNjaGl0YWxlIGJhbmRodSBwdW5lIgOIAQFaFSITY2hpdGFsZSBiYW5kaHUgcHVuZZIBC2NhbmR5X3N0b3JlqgFeCg0vZy8xMWJ5bDdybnR6EAEqEiIOY2hpdGFsZSBiYW5kaHUoADIeEAEiGuITDsTq9ajzKuJQOPdLEeOcGq8UZmDkmUNrMhcQAiITY2hpdGFsZSBiYW5kaHUgcHVuZeABAA!16s%2Fg%2F124yljf2_?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Vaishali", "map_link": "https://www.google.co.in/maps/place/Vaishali+Restaurant/@18.5208838,73.841237,17z/data=!3m1!4b1!4m6!3m5!1s0x3bc2bf0f2dfc1f77:0x91569070e0816020!8m2!3d18.5208838!4d73.841237!16s%2Fg%2F11j10vz1k5?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Jaipur": [
        {"name": "Rawat Mishtan Bhandar", "map_link": "https://www.google.co.in/maps/place/Rawat+Misthan+Bhandar/@26.9212614,75.7967221,17z/data=!3m1!4b1!4m6!3m5!1s0x396db3f91b850137:0xaf74b3b2dba5af20!8m2!3d26.9212614!4d75.7967221!16s%2Fg%2F11d_xhhbsf?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Chokhi Dhani", "map_link": "https://www.google.co.in/maps/place/Chokhi+Dhani,+Jaipur/@26.7674657,75.8361692,17z/data=!4m9!3m8!1s0x396dc96e5f04f419:0x7987ca41bab6342a!5m2!4m1!1i2!8m2!3d26.7674657!4d75.8361692!16s%2Fg%2F11tmwbcrc3?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Laxmi Misthan Bhanda", "map_link": "https://www.google.co.in/maps/place/Laxmi+Misthan+Bhandar/@26.9196187,75.8256378,17z/data=!3m1!4b1!4m6!3m5!1s0x396db6b48d1fcebf:0x4cf65b572c487042!8m2!3d26.9196187!4d75.8256378!16s%2Fg%2F1td5_3v1?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],

    "Lucknow": [
        {"name": "Tunday Kababi", "map_link": "https://www.google.co.in/maps/place/Tunday+Kababi,+Aminabad/@26.8482869,80.9272873,17z/data=!3m1!4b1!4m6!3m5!1s0x399bfdba3bc2fc11:0x2c78bfb2bb175a1c!8m2!3d26.8482869!4d80.9272873!16s%2Fg%2F119wpqrtc?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Rahim's Kulcha", "map_link": "https://www.google.co.in/maps/place/Raheems+Kulcha-Nahari/@26.8595694,80.9063963,17z/data=!3m1!4b1!4m6!3m5!1s0x399bfde703cd2785:0xe0b5f937c23a8726!8m2!3d26.8595694!4d80.9063963!16s%2Fg%2F1tqpxnlw?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Ram Asrey Kulfi", "map_link": "https://www.google.co.in/maps/place/Ram+Asrey/@26.8664979,80.8888876,14z/data=!4m10!1m2!2m1!1sRam+Asrey+Kulfi+lucknow!3m6!1s0x399bfde4ef81ef5d:0xbecca2f545c893fb!8m2!3d26.8664979!4d80.9063971!15sChdSYW0gQXNyZXkgS3VsZmkgbHVja25vd1oZIhdyYW0gYXNyZXkga3VsZmkgbHVja25vd5IBC2NhbmR5X3N0b3JlmgEjQ2haRFNVaE5NRzluUzBWSlEwRm5UVVJSTjNCMWJraG5FQUWqAV8KCS9tLzAza2gyMRABKhMiD3JhbSBhc3JleSBrdWxmaSgAMh4QASIak_uFnL7x3Jq8gmmSDy59vgP3TioQBroornsyGxACIhdyYW0gYXNyZXkga3VsZmkgbHVja25vd-ABAPoBBAgAECM!16s%2Fg%2F1tfrvxgz?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Amritsar": [
        {"name": "Kesar Da Dhaba", "map_link": "https://www.google.co.in/maps/place/Kesar+Da+Dhaba/@31.6242351,74.8729981,17z/data=!3m1!4b1!4m6!3m5!1s0x39197caa7727941f:0xfcde6f886bfa4e16!8m2!3d31.6242351!4d74.8729981!16s%2Fg%2F1q62fn9t0?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Bharawan Da Dhaba", "map_link": "https://www.google.co.in/maps/place/Bharawan+Da+Dhaba/@31.6260072,74.8426069,13z/data=!4m10!1m2!2m1!1sbharawan+da+dhaba+amritsar!3m6!1s0x39197cab07b59fcb:0xd2d0e0c334c6ff65!8m2!3d31.6260072!4d74.8776258!15sChpiaGFyYXdhbiBkYSBkaGFiYSBhbXJpdHNhclocIhpiaGFyYXdhbiBkYSBkaGFiYSBhbXJpdHNhcpIBBWRoYWJhqgFCEAEyHhABIhrjU7TvXmeVj_4KvHuPBkQIQFchsHpUEPSx9jIeEAIiGmJoYXJhd2FuIGRhIGRoYWJhIGFtcml0c2Fy4AEA!16s%2Fg%2F1hjgmfx66?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Kulcha Land", "map_link": "https://www.google.co.in/maps/place/Kulcha+Land/@31.6530963,74.828886,13z/data=!4m10!1m2!2m1!1skulcha+land+amritsar!3m6!1s0x39197cb026db0cd1:0xda04e4171c611987!8m2!3d31.6530963!4d74.8639049!15sChRrdWxjaGEgbGFuZCBhbXJpdHNhcloWIhRrdWxjaGEgbGFuZCBhbXJpdHNhcpIBEnB1bmphYmlfcmVzdGF1cmFudKoBTAoNL2cvMTFjbTN3OTQzbRABMh8QASIbst57NcaASpvfGo09VcNmYwALo_3Axy5c165fMhgQAiIUa3VsY2hhIGxhbmQgYW1yaXRzYXLgAQA!16s%2Fg%2F11cm3w943m?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],

    "Goa": [
        {"name": "Vinayak Family Restaurant", "map_link": "https://www.google.co.in/maps/place/Vinayak+Family+Restaurant/@15.5973233,73.7726749,17z/data=!3m1!4b1!4m6!3m5!1s0x3bbfebb60afe758b:0x9415a104acf05113!8m2!3d15.5973233!4d73.7726749!16s%2Fg%2F11b6f11g3r?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Mum’s Kitchen", "map_link": "https://www.google.co.in/maps/place/Mums+Kitchen/@15.4871348,73.8128064,17z/data=!3m1!4b1!4m6!3m5!1s0x3bbfc0ec02fca9d3:0x4b20a0c64329fdf4!8m2!3d15.4871348!4d73.8128064!16s%2Fg%2F1tdl94tk?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Anand Bar and Restaurant", "map_link": "https://www.google.co.in/maps/place/Anand+Sea+Food+bar+%26+restaurant+anjuna/@15.595796,73.7257791,13z/data=!4m10!1m2!2m1!1sAnand+Bar+and+Restaurant+goa!3m6!1s0x3bbfe98187d3dba5:0xc0e5955b9098b0db!8m2!3d15.595796!4d73.760798!15sChxBbmFuZCBCYXIgYW5kIFJlc3RhdXJhbnQgZ29hWh4iHGFuYW5kIGJhciBhbmQgcmVzdGF1cmFudCBnb2GSARJzZWFmb29kX3Jlc3RhdXJhbnSqAVMKDC9nLzEycWg5YmY5dhABMh8QASIbxP5dcLaVdu2AkIU-FAoj8cSYETtD-__IsrwiMiAQAiIcYW5hbmQgYmFyIGFuZCByZXN0YXVyYW50IGdvYeABAA!16s%2Fg%2F12qh9bf9v?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Udaipur": [
        {"name": "Natraj Dining Hall", "map_link": "https://www.google.co.in/maps/place/Natraj+Dining+Hall+And+Restaurant/@24.5723618,73.6952872,16z/data=!4m10!1m2!2m1!1snatraj+dining+hall+udaipur!3m6!1s0x3967ef800976dedd:0x3b17ab8dfbc69b2!8m2!3d24.5723618!4d73.6996646!15sChpuYXRyYWogZGluaW5nIGhhbGwgdWRhaXB1clocIhpuYXRyYWogZGluaW5nIGhhbGwgdWRhaXB1cpIBFXJhamFzdGhhbmlfcmVzdGF1cmFudKoBQxABMh8QASIb9XmqY-XNAHkplSCcYpkyJknQZ-I5F8ZUYOSWMh4QAiIabmF0cmFqIGRpbmluZyBoYWxsIHVkYWlwdXLgAQA!16s%2Fg%2F1hhgwfzs3?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Santosh Bhojnalaya", "map_link": "https://www.google.co.in/maps/place/New+Santosh+Bhojnalaya+%26+Restaurant/@24.5786047,73.6960369,17z/data=!3m1!4b1!4m6!3m5!1s0x3967e579410f693d:0xfcaa33f297269e4c!8m2!3d24.5786047!4d73.6960369!16s%2Fg%2F1v299f48?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Mewari Bhojnalaya", "map_link": "https://www.google.co.in/maps/place/Mewari+Restaurant+%26+Bar/@24.5974505,73.673965,14z/data=!4m10!1m2!2m1!1sMewari+Bhojnalaya+udaipur!3m6!1s0x3967e57dd5fd5bd1:0x761fdafabf8528e9!8m2!3d24.5974505!4d73.6914745!15sChlNZXdhcmkgQmhvam5hbGF5YSB1ZGFpcHVyWhsiGW1ld2FyaSBiaG9qbmFsYXlhIHVkYWlwdXKSARdub3J0aF9pbmRpYW5fcmVzdGF1cmFudKoBWRABKhUiEW1ld2FyaSBiaG9qbmFsYXlhKAAyHxABIhvigF90L7_w3H7uGVzaF4mfNuJFEU5sGkCUoEwyHRACIhltZXdhcmkgYmhvam5hbGF5YSB1ZGFpcHVy4AEA!16s%2Fg%2F11s3y3s1t0?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],

    "Varanasi": [
        {"name": "Kachori Gali", "map_link": "https://www.google.co.in/maps/place/Kachaudi+Gali,+Lahori+Tola,+Varanasi,+Uttar+Pradesh+221001/@25.3125132,83.0113045,17z/data=!4m6!3m5!1s0x398e2e1ec336c637:0x265abb10d45f74e0!8m2!3d25.3125132!4d83.0113045!16s%2Fg%2F1hjhb4pk0?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Deena Chat Bhandar", "map_link": "https://www.google.co.in/maps/place/Deena+Chaat+Bhandar/@25.3090364,83.0023819,17z/data=!3m1!4b1!4m6!3m5!1s0x398e2e02ea4baf71:0x55cd387d275b3854!8m2!3d25.3090364!4d83.0023819!16s%2Fg%2F1260d7xq0?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Kashi Chaat Bhandar", "map_link": "https://www.google.co.in/maps/place/Kashi+Chat+Bhandar/@25.3094215,83.0060588,17z/data=!3m1!4b1!4m6!3m5!1s0x398e2e1d0e6c52cd:0xa8a3678baea40336!8m2!3d25.3094215!4d83.0060588!16s%2Fg%2F1261fcgyd?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
    ],
    "Mysore": [
        {"name": "Mysore Masala Dosa House", "map_link": "https://www.google.co.in/maps/place/GURU+DARSHINI+-DOSA+PALACE/@12.3221925,76.5991021,13z/data=!4m10!1m2!2m1!1sMysore+Masala+Dosa+House+mysore!3m6!1s0x3baf7a9b6b4695e9:0xdc30d6fe9b995364!8m2!3d12.3221925!4d76.634121!15sCh9NeXNvcmUgTWFzYWxhIERvc2EgSG91c2UgbXlzb3JlWiEiH215c29yZSBtYXNhbGEgZG9zYSBob3VzZSBteXNvcmWSARdzb3V0aF9pbmRpYW5fcmVzdGF1cmFudJoBI0NoWkRTVWhOTUc5blMwVkpRMEZuU1VRM01sQmxSazlSRUFFqgF-CgsvZy8xMjF3dDJwOQoJL20vMDFfN2N6EAEqHCIYbWFzYWxhIGRvc2EgaG91c2UgbXlzb3JlKAAyHxABIhvVcZASETjGAfqw19uBiDAhyNfeTx4hbmshOM8yIxACIh9teXNvcmUgbWFzYWxhIGRvc2EgaG91c2UgbXlzb3Jl4AEA-gEECBMQSg!16s%2Fg%2F11dxm548sv?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Ragi Mudde Center", "map_link": "https://www.google.co.in/maps/place/Lakshman+Mess/@12.3043113,76.0910247,9z/data=!4m10!1m2!2m1!1sRagi+Mudde+Center+mysore!3m6!1s0x3baf700fb81830a3:0xc0809b37c45f3b74!8m2!3d12.3043113!4d76.6513274!15sChhSYWdpIE11ZGRlIENlbnRlciBteXNvcmVaGiIYcmFnaSBtdWRkZSBjZW50ZXIgbXlzb3JlkgESYmlyeWFuaV9yZXN0YXVyYW50qgFkCgovbS8wMnFueXQ5EAEqFSIRcmFnaSBtdWRkZSBjZW50ZXIoADIfEAEiG5YuExwH1rolBKhsJe_PZ58V4876R9-7GiU9SjIcEAIiGHJhZ2kgbXVkZGUgY2VudGVyIG15c29yZeABAA!16s%2Fg%2F11c1q9jq38?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Guru Sweets", "map_link": "https://www.google.co.in/maps/place/Guru+Sweet+Mart/@12.3099037,76.6525953,17z/data=!3m1!4b1!4m6!3m5!1s0x3baf700d897521a9:0x11f6c39d349dabb9!8m2!3d12.3099037!4d76.6525953!16s%2Fg%2F124ykmkdn?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ],
    "Shimla": [
        {"name": "Ashiana & Goofa", "map_link": "https://www.google.co.in/maps/place/Goofa+Ashiana+Restaurant/@31.1045697,77.1742262,17z/data=!3m1!4b1!4m6!3m5!1s0x39057971dfdd1dab:0x49b8d733e760f843!8m2!3d31.1045697!4d77.1742262!16s%2Fg%2F1vqtf55d?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Wake & Bake Cafe", "map_link": "https://www.google.co.in/maps/place/Wake+%26+Bake+-+Best+Family+Cafe+Restaurants+in+Shimla%2FBest+Food%2FBest+Coffee+in+Restaurant+in+Shimla/@31.1046448,77.1729818,17z/data=!3m1!4b1!4m6!3m5!1s0x3905789368714221:0xe1b50f1cb899a2bd!8m2!3d31.1046448!4d77.1729818!16s%2Fg%2F1tf6d_zy?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"},
        {"name": "Cafe Shimla Times", "map_link": "https://www.google.co.in/maps/place/Cafe+Simla+Times+:+Cafe,+Biergarten+%26+Bar+on+the+Mall+Road+Shimla+/@31.1009306,77.1763075,17z/data=!3m1!4b1!4m6!3m5!1s0x390578958cdc7cd9:0x70198a4280fc511a!8m2!3d31.1009306!4d77.1763075!16s%2Fg%2F11btx07f70?entry=ttu&g_ep=EgoyMDI1MDYwMS4wIKXMDSoASAFQAw%3D%3D"}
    ]
}