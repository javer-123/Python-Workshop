class Person: 
 def owner(self): 
  item = str(input("Enter the item: ")) 
  print(f"Owner has {item}.") 
if __name__ == "_main_": 
  person = input("Who are you? ") 
if Person.lower() == "owner": 
 owner_person = Person() 
owner_person.owner()
