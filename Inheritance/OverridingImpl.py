class Phone:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def callingPhone(self):
        print("calling to your loved ones")


    def messaingPhone(self):
        print("messaging to your loved ones")


    def browsingPhone(self):
        print("calling to your loved ones")


class MotorolaPhone(Phone):

    def __init__(self, make, model, year, ringer):
        super().__init__(make,model,year)
        self.ringer = ringer


    def messaingPhone(self):
        print("message is sent")

motorolaphone = MotorolaPhone("motorols", "motorols", "2003", True)
print(motorolaphone.make)
print(motorolaphone.model)
print(motorolaphone.year)
print(motorolaphone.ringer)
print(motorolaphone.messaingPhone())







