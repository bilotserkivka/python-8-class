user_name = input("Як тебе звати? ")
user_age = int(input("Скільки тобі років? "))


if user_age == 41:
    if user_name == "Богдан":
        print("Нам однаково років і ми тезки")
    else:
        print("Нам однаково років, але звати тебе інакше")
else:
    print("Ми різного віку")
    if user_name == "Олександр":
        print("Тебе звати як мого батька")