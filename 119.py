class Restaurant:
    def __init__(self, res_name, res_cuisine):
        self.res_name = res_name
        self.res_cuisine = res_cuisine
        
    def res_description(self):
        print("The name of this restaurant is " + self.res_name.title() + '.')
        print("It is a " + self.res_cuisine.title() + " restaurant.")

class Ice_Cream_Stand(Restaurant):
    def __init__(self, res_name, res_cuisine):
        super().__init__(res_name, res_cuisine)
        self.flavours = ['chocolate','vanila','black current']
            
    def get_flavours(self):
        print ("This restaurant has following flavours:")
        for flavour in self.flavours:
            print (flavour)

my_ice_cream = Ice_Cream_Stand('robbiins','french')
my_ice_cream.res_description()
my_ice_cream.get_flavours()
