users: list=[
    {"name":"lukasz","location":"opoczno","posts": 89 },
    {"name":"michal","location":"debica","posts": 10 },
    {"name":"weronika","location":"opole","posts": 20 },
    {"name":"sabina","location":"opoczno","posts": 25 },

]


print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"twoj znajomy {user["name"]} z {user["location"]} opublikowal")



