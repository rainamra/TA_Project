guest = ["azel", "bunga", "cen"]
print(guest)

Invitation = "Hello " + guest[0] + "! You are invited to my dinner party!"
Invitation_1 = "Hello " + guest[1] + "! You are invited to my dinner party!"
Invitation_2 = "Hello " + guest[2] + "! You are invited to my dinner party!"
print(Invitation)
print(Invitation_1)
print(Invitation_2)

poped_guest = guest.pop(2)
print(poped_guest + " cant come to my dinner party")
print(guest)

guest.append("ali")
print(guest)
Invitation_2 = "Hello " + guest[2] + "! You are invited to my dinner party!"
print(Invitation)
print(Invitation_1)
print(Invitation_2)
print("i just found a bigger dinner table so im going to invite 3 more people")
guest.insert(0, "chelsea")
guest.insert(2, "jenni")
guest.append("glenn")
print(guest)
Invitation_ = "Hello " + guest[0] + "! You are invited to my dinner party!"
Invitation__1 = "Hello " + guest[1] + "! You are invited to my dinner party!"
Invitation__2 = "Hello " + guest[2] + "! You are invited to my dinner party!"
Invitation__3 = "Hello " + guest[3] + "! You are invited to my dinner party!"
Invitation__4= "Hello " + guest[4] + "! You are invited to my dinner party!"
Invitation__5 = "Hello " + guest[5] + "! You are invited to my dinner party!"
print(Invitation_)
print(Invitation__1)
print(Invitation__2)
print(Invitation__3)
print(Invitation__4)
print(Invitation__5)

print(Invitation_ + " but i'm sorry turns out the dinner table won't arrive in time. So, i can invite only 2 people")
print(Invitation__1 + " but i'm sorry turns out the dinner table won't arrive in time. So, i can invite only 2 people")
print(Invitation__2 + " but i'm sorry turns out the dinner table won't arrive in time. So, i can invite only 2 people")
print(Invitation__3 + " but i'm sorry turns out the dinner table won't arrive in time. So, i can invite only 2 people")
print(Invitation__4 + " but i'm sorry turns out the dinner table won't arrive in time. So, i can invite only 2 people")
print(Invitation__5 + " but i'm sorry turns out the dinner table won't arrive in time. So, i can invite only 2 people")

sorry = ", sorry i can't invite you to dinner because of this matter"
poped_guest1 = guest.pop(0)
print(poped_guest1 + sorry)
poped_guest2 = guest.pop(1)
print(poped_guest2 + sorry)
poped_guest3 = guest.pop(2)
print(poped_guest3 + sorry)
poped_guest4 = guest.pop(2)
print(poped_guest4 + sorry)
print(guest)

still_invited = " you're still invited friend!"
print(guest[0] + still_invited)
print(guest[1] + still_invited)
del guest [0:2]
print(guest)


places = ["maldives", "labuan bajo", "sumba", "raja ampat", "fuji"]
print(places)
places.sort()
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()
print(places)





