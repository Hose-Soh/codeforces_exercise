total_games = int(input())

game_track = input()

anton_total = len([i for i, char in enumerate(game_track) if char == 'A'])
danik_total = len([i for i, char in enumerate(game_track) if char == 'D'])

if anton_total>danik_total:
    print("Anton")
elif anton_total==danik_total:
    print("Friendship")
else:
    print("Danik")
