class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.age = age 
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend")
        return self

yuzuha = User("Yuzuha", "Shibata", "yuzuha48@gmail.com", 22)

# yuzuha.display_info()
# yuzuha.enroll()
# yuzuha.spend_points(50)
# yuzuha.display_info()
# yuzuha.enroll()

yuzuha.enroll().spend_points(50).display_info().enroll()

jackson = User("Jackson", "Muehlbauer", "jmuehl@umn.edu", 24)

# jackson.enroll()
# jackson.spend_points(80)
# jackson.display_info()

jackson.enroll().spend_points(80).display_info()

michiru = User("Michiru", "Sasaki", "yuzulemon@hotmail.com", 49)

# michiru.display_info()
# michiru.spend_points(40)

michiru.display_info().spend_points(40)
