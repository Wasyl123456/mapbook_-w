users: list= [
    {"name":"lukasz","location":"opoczno","posts": 89 },
    {"name":"michal","location":"dębica","posts": 78 },
]



print(users)


def update_user(users_data:list) -> None:
    users_name=input("Podaj imię znajomego do aktualizacji: ")
    for user in users_data:
        if user["name"] == users_name:
                user["name"]=input("Podaj nowe imie znajomego:")
                user["location"]=input("Podaj nową miejscowość:")
                user["posts"]=input(input("Podaj nową liczbę postów:"))

update_user(users)
print(users)



