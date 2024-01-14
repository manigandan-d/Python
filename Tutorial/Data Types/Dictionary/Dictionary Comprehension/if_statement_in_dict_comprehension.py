data = {"Durai": 50, "Kalai": 40, "Keerai": 30, "Mani": 20, "Anbu": 10}

modData = {key: value + 10 for key, value in data.items() if value > 30}

print(modData)
