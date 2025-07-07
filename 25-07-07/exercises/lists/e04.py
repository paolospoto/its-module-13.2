# Backup
# RULES:
# - Use a list to manage occupied rooms in a hospital
# - Save a backup copy and clear the list
occupied_rooms = ["Room 1", "Room 2", "Room 3"]

occupied_rooms_2 = occupied_rooms.copy()

occupied_rooms.clear()

print(occupied_rooms)
