def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"twoj znajomy {user["name"]} z {user["location"]} opublikowal ")

def add_user(users_data: list)->None:
    new_name= input("podaj imię: ")
    new_location= input("podaj miejsce: ")
    new_posts= input("podaj liczbe postow: ")
    users_data.append( {"name": new_name,"location":"debica","posts": new_posts } )


def remove_user(users_data:list) -> None:
    users_name=input("Podaj imię znajomego do usunięcia:")
    for user in users_data:
        if user["name"] == users_name:
            users.data.remove(user)