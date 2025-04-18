# -*- coding: utf-8 -*-
class Pet:
    # 🐾 Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name  # 🏷️ Name of the pet
        self.hunger = 5  # 🍖 Initial hunger level (0 = full, 10 = very hungry)
        self.energy = 5  # ⚡ Initial energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # 😊 Initial happiness level (0–10)
        self.tricks = []  # 🧠 List to store tricks the pet has learned

    # 🍽️ Method to feed the pet
    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3, but not below 0
            self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1
            print(f"{self.name} is eating. 🍖 Hunger level: {self.hunger}, 😊 Happiness level: {self.happiness}")
        else:
            print(f"{self.name} is already full.")  # If hunger is already 0

    # 💤 Method to let the pet sleep
    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)  # Increase energy by 5, but not above 10
            print(f"{self.name} is sleeping. 💤 Energy level: {self.energy}")
        else:
            print(f"{self.name} is already fully rested.")  # If energy is already 10

    # 🎾 Method to play with the pet
    def play(self):
        if self.energy > 1 and self.happiness < 10:
            self.energy = max(0, self.energy - 2)  # Decrease energy by 2
            self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2
            self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1
            print(f"{self.name} is playing. 😊 Happiness level: {self.happiness}, ⚡ Energy level: {self.energy}, 🍖 Hunger level: {self.hunger}")
        else:
            print(f"{self.name} is too tired or too happy to play.")  # If energy is too low or happiness is maxed out

    # 🐕‍🦺 Method to teach the pet a new trick
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)  # Add the trick to the list if not already learned
            print(f"{self.name} learned a new trick: 🐾 {trick}.")
        else:
            print(f"{self.name} already knows the trick: 🐾 {trick}.")  # If the trick is already known

    # 🧠 Method to display all tricks the pet has learned
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} can do the following tricks: 🐾 {', '.join(self.tricks)}")  # List all tricks
        else:
            print(f"{self.name} doesn't know any tricks yet.")  # If no tricks are learned

    # 📋 Method to display the current status of the pet
    def get_status(self):
        print(f"📋 Name: {self.name}")  # Display the pet's name
        print(f"🍖 Hunger: {self.hunger}")  # Display the pet's hunger level
        print(f"⚡ Energy: {self.energy}")  # Display the pet's energy level
        print(f"😊 Happiness: {self.happiness}")  # Display the pet's happiness level
        print(f"🧠 Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")  # Display the tricks or 'None' if no tricks

