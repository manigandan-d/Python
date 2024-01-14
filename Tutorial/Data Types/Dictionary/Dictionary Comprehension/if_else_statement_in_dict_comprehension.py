data = {"Durai": 50, "Kalai": 40, "Keerai": 30, "Mani": 20, "Anbu": 10}

modData = {key: value + 10 if value > 30 else value + 5 for key, value in data.items()}

print(modData)
