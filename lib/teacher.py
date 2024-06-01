#!/usr/bin/env python

#!/usr/bin/env python3

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History", "Art"]

    def teach(self):
        return random.choice(self.knowledge)
