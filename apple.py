class Apple:

    def __init__(self, color, taste, harvest, name, weight):
        self.color = color
        self.taste = taste
        self.harvest = harvest
        self.name = name
        self.weight = weight

    def __repr__(self):

        return "name:{0} \ncolor: {1} \nweight: {2}".format(self.name, self.color, self.weight)
        #return "name:{name} \ncolor: {color} \nweight: {weight}".format(name = self.name, color = self.color, weight = self.weight)
    #ef Eat(self):
        #return 'bite right in'

class CandyApple(Apple):

    def __init__(self, color, taste, harvest, name, weight, drizzle):
        #initialize parent first 
        #super()
        Apple.__init__(self,color, taste, harvest, name, weight)
        #set any local params second
        self.drizzle = drizzle



def main():
    fuji_apple = Apple('red', 'sweet', 'fall', 'fuji' , '2oz')
    caramel_apple = Apple('green', 'sweet', 'summer', 'candy apple', '6oz')

    #print(fuji_apple.Eat())
    #print(caramel_apple.Eat())
    print(fuji_apple)
    print(caramel_apple


if __name__ == "__main__":
    main()
