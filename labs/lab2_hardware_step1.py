from sense_hat import SenseHat

sense = SenseHat()

sense.show_letter("B")

index = 1



####
# Main game loop
####

while True:
  selection = False
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":
        index+=1
        if index %2 == 0:
            sense.show_letter("B")
        else:
            sense.show_letter("L")
