class Item():
    def items_main(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return str ("value").format(self.name, self.description, self.value)