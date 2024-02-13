from collections import defaultdict

def find_captains_room(group_size, room_numbers):
	room_count = defaultdict(int)

	print(room_count)

	for room in room_numbers:
		room_count[room] += 1

	print(room_count)

	for room, count in room_count.items():
		if count == 1:
			return room

group_size = int(input())
room_numbers = list(map(int, input().split()))

captains_room = find_captains_room(group_size, room_numbers)
print(captains_room)

