# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from Pet import Pet

# 🐾 Create a pet instance
my_pet = Pet("Buddy")

# 🛠️ Test the methods
my_pet.get_status()  # 📋 Display initial status
my_pet.eat()         # 🍖 Feed the pet
my_pet.play()        # 🎾 Play with the pet
my_pet.sleep()       # 💤 Let the pet sleep
my_pet.train("roll over")  # 🐕‍🦺 Teach a new trick
my_pet.train("play dead")  # 🐕‍🦺 Teach another trick
my_pet.show_tricks()       # 🧠 Show learned tricks
my_pet.get_status()        # 📋 Display final status