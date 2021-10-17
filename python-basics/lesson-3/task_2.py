def user(name=None, surname=None, birth=None, city=None, email=None, tel=None):
    args = name.title(), surname.title(), birth, city.title(), email, tel
    print(", ".join(args))


name = input("Enter your name: ")
surname = input("Enter your surname: ")
birth = input("Enter your birthday: ")
city = input("Enter your city: ")
email = input("Enter your email address: ")
tel = input("Enter your phone number: ")
user(name, surname, birth, city, email, tel)
