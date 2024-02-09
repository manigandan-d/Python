from collections import defaultdict

def find_captains_room(group_size, room_numbers):
    room_count = defaultdict(int)
    
    # Count the occurrences of each room number
    for room in room_numbers:
        room_count[room] += 1
    
    # Find the room number with a count of 1
    for room, count in room_count.items():
        if count == 1:
            return room

# Input
group_size = int(input())
room_numbers = list(map(int, input().split()))

# Output
captains_room = find_captains_room(group_size, room_numbers)
print(captains_room)
