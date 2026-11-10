def ask_user_info(name, age, address, phone):

    user_info = {
        "name": name,
        "age": age,
        "address": address,
        "phone": phone
    }

    print(user_info["name"], "is", user_info["age"], "years old, lives at", user_info["address"], "and their phone number is", user_info["phone"])

    return user_info

if __name__ == "__main__":

    ask_user_info("Arion", "17", "123 Main St", "555-1234")
