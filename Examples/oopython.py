class MyClass():
  def __init__(self):
    self.count = 0 # create self.count and set it to 0
  def increment(self):
    self.count = self.count + 1 # increment the variable

myclass = MyClass();
myclass.increment();

print(myclass.count);