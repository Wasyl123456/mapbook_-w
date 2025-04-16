users: list= [
    {"name":"lukasz","location":"opoczno","posts": 89 },
]


print(users)


def remove_user(users_data:list) -> None:
    users_name=input("Podaj imię znajomego do usunięcia:")
    for user in users_data:
        if user["name"] == users_name:
            users.data.remove(user)

remove_user(users)
print(users)



