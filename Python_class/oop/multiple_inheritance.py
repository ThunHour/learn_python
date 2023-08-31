class Mother:
    def eye_color(self):
        print("Eyes color is brown")

    def skin_color(self):
        print("Skin tone is black")


class Father:
    def height(self):
        print("I am 6.5 tall")

    def skin_color(self):
        print("Skin tone is white")


class Son(Mother,Father):
    pass


son = Son()
son.eye_color()
son.height()
son.skin_color() #give more priory to mother since Mother stay in the upper line compare to Father


# father = Father()
# father.eyecolor() #Error, because Father is both rank as Mother

# mother = Mother()
# mother.height() #Error, because Mother is both rank as Mother