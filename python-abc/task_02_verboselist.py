class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {[item]} from the list.")

    def pop(self, value=-1):
        pop_value = super().pop(value)
        print(f"Popped {[pop_value]} from the list.")

    def extend(self, value):
        super().extend(value)
        print(f"Extended the list with {[len(value)]} items.")
