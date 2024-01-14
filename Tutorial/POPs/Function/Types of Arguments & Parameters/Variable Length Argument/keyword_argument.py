def details(**data):
    for key, value in data.items():
        print(key, end=":")
        print(value)


details(Name="Mani", Age=22, Gender='M')
