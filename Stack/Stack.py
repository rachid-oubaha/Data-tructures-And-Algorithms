class Stack:
   def __init__(self):
      self.stack = []

   def push(self, value):
# Use list append method to push element
        self.stack.append(value)

# Use pop to remove element
   def pop(self):
        if len(self.stack) <= 0:
            return print("No element in the Stack")
        else:
            return self.stack.pop()