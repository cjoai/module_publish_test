
class Star_print:

    def __init__(self):
        self.contents = "*"*100

    def print_star(self):
        print(self.contents)

    def print_multiple(self, number_print):
        for i in range(number_print):
            self.print_star()