bicycles=['trek','cannodale','redline','specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])
message=f"My first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles=[]
motorcycles.append("yamaha")
motorcycles.append("suzuki")
motorcycles.append("honda")

print(motorcycles)

motorcycles.insert(0,"ducati")
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned=motorcycles.pop(0)
print(first_owned)

motorcycles=['honda','yamaha','suzuki','yamaha']
motorcycles.remove('yamaha')
print("removed\n")
print(motorcycles)

guest_list=['babu','yazhini','vishrudh','someone']
invitation="Please come to the dinner"
print(f"{guest_list[0].title()}, {invitation}")
print(f"{guest_list[1].title()}, {invitation}")
print(f"{guest_list[2].title()}, {invitation}")
print(f"{guest_list[3].title()}, {invitation}")
guest_notcoming = guest_list.pop()
print(f"{guest_notcoming.title()}, not able to come")
guest_list.append("yyy")
print(f"{guest_list[0].title()}, {invitation}")
print(f"{guest_list[1].title()}, {invitation}")
print(f"{guest_list[2].title()}, {invitation}")
print(f"{guest_list[3].title()}, {invitation}")
print("I found a bigger dinner table!")
guest_list.insert(0,"Daddy")
guest_list.insert(3,"Mummy")
guest_list.append("KKKK")
print(guest_list)
print("I can invite only two people, Sorry!")
print(f"{guest_list.pop()}, Sorry I can't invite to dinner")
print(f"{guest_list.pop()}, Sorry I can't invite to dinner")
print(f"{guest_list.pop(0)}, Sorry I can't invite to dinner")
print(f"{guest_list.pop(0)}, Sorry I can't invite to dinner")
print(f"{guest_list.pop(1)}, Sorry I can't invite to dinner")
print(guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)

cars=['nissan','bmw','toyota','mercedes']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars=['nissan','bmw','toyota','mercedes']
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))

visit_places=['melbourne','canada','italy','singapore','himalaya']
print(visit_places)
print(sorted(visit_places))
print(visit_places)
print(sorted(visit_places,reverse=True))
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.sort()
print(visit_places)
visit_places.sort(reverse=True)
print(visit_places)
print(len(visit_places))



