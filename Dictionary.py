##############
#Dictionary
############## 
best_player = {
    "name": "Jayesh",
    "score": 1500,
    "date": "16.09.2025",
    "city": "Austin",
    "level": 5
}

print(best_player["name"])

best_player["score"] = 3000

print(best_player.get("city"))
print(best_player.get("country","USA")) #return default value as USA if it is not in the dict.

print(best_player.keys())
print(list(best_player.keys()))
print(list(best_player.values()))

print(best_player.items())
for key, value in best_player.items():
    print(f"{key}: {value}")

player_scores = {
    "A" : 1600,
    "B" : 2000,
    "C" : 800
}

best_player.pop("score") #remove the entry from score entry form dict.
best_player.pop("xyz", None) #remve the entry but if not found return none

more_info = {
    "age": 26,
    "lives": 4
}

best_player.update(more_info) #add more key value pair into dict/
print(best_player)
best_player.update(player_scores)
print(best_player)


##########
#example

car_pref = {}

alice = {
    "color" : "red",
    "doors" : 4
}

bob = {
    "brand" : "BMW",
    "Sunroof" : 1,
}

car_pref.update(alice)
car_pref.update(bob)
car_pref.update({"budget" : 150000})
car_pref["price"] = 200000
if car_pref["budget"] < car_pref["price"]:
    car_pref.pop("brand")
car_pref["price"] = 180000

for key, value in car_pref.items():
    print(f"{key}: {value}") 