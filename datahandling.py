import json
import dbms

# Prepare notes data
notes_data = [
    {"name": "Note 1", "createdAt": "2024-01-01"},
    {"name": "Note 2", "createdAt": "2024-01-02"},
    {"name": "Note 3", "createdAt": "2024-01-03"},
    {"name": "Note 4", "createdAt": "2024-01-04"},
    {"name": "Note 5", "createdAt": "2024-01-05"},
    {"name": "Note 6", "createdAt": "2024-01-06"},
    {"name": "Note 7", "createdAt": "2024-01-07"},
    {"name": "Note 8", "createdAt": "2024-01-08"},
    {"name": "Note 9", "createdAt": "2024-01-09"},
    {"name": "Note 10", "createdAt": "2024-01-10"},
    {"name": "Note 11", "createdAt": "2024-01-11"},
    {"name": "Note 12", "createdAt": "2024-01-12"},
    {"name": "Note 13", "createdAt": "2024-01-13"},
    {"name": "Note 14", "createdAt": "2024-01-14"},
    {"name": "Note 15", "createdAt": "2024-01-15"},
    {"name": "Note 16", "createdAt": "2024-01-16"},
    {"name": "Note 17", "createdAt": "2024-01-17"},
    {"name": "Note 18", "createdAt": "2024-01-18"},
    {"name": "Note 19", "createdAt": "2024-01-19"},
    {"name": "Note 20", "createdAt": "2024-01-20"},
]

# Insert notes data into the "notes" collection
for note in notes_data:
    try:
        dbms.insert_data("notes", note)
    except Exception as e:
        print(f"Error inserting data: {e}")

# Prepare notifications data
notifications_data = [
    {"name": "Notification 1", "date": "2024-01-01"},
    {"name": "Notification 2", "date": "2024-01-02"},
    {"name": "Notification 3", "date": "2024-01-03"},
    {"name": "Notification 4", "date": "2024-01-04"},
]

# Insert notifications data into the "notifications" collection
for notification in notifications_data:
    try:
        dbms.insert_data("notifications", notification)
    except Exception as e:
        print(f"Error inserting data: {e}")
