class Monkey:
    def __init__(self):
        self.has_banana=False
        self.position="floor"
    def monkey_on_floor(self):
        print("monkey on the floor")
    def climbs_box(self):
        if self.position=='floor':
            self.position="box"
            print("Monkey climbs the box")
    def grabs_banana(self):
        if self.position=='box' and not self.has_banana:
            self.has_banana=True
            print("monkey grabs the banana!")
    def solve_problem():
        monkey=Monkey()
        monkey.monkey_on_floor()
        monkey.climbs_box()
        monkey.grabs_banana()
Monkey.solve_problem()        