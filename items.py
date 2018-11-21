class Item(object):

    def items_main(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        print(f"Your items are = {name}, {description}, {value}")

        for name in Item:
            Item.append(name)