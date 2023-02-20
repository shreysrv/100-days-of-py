travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    log = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(log)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
