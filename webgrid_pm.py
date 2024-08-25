import random
import time
import math

class Task:
def init(self, identifier, priority, difficulty):
self.identifier = identifier
self.priority = priority
self.difficulty = difficulty

class Grid:
def init(self, size):
self.size = size
self.cells = [[None for _ in range(size)] for _ in range(size)]
def allocate_tasks(self, tasks):
    positions = [(i, j) for i in range(self.size) for j in range(self.size)]
    random.shuffle(positions)
    for task, (i, j) in zip(tasks, positions):
        self.cells[i][j] = task

class WebgridProjectManagement:
def init(self, grid_size, duration):
self.grid = Grid(grid_size)
self.duration = duration
self.score = 0
self.tasks_completed = 0
self.start_time = None
self.end_time = None

def create_tasks(self, num_tasks):
    return [Task(f"Task{i}", random.randint(1, 5), random.randint(1, 5)) 
            for i in range(num_tasks)]

def run_simulation(self):
    tasks = self.create_tasks(self.grid.size * self.grid.size // 2)  # Fill half the grid
    self.grid.allocate_tasks(tasks)
    self.start_time = time.time()
    
    while time.time() - self.start_time < self.duration:
        self.display_grid()
        row, col = map(int, input("Enter row and column (e.g., '2 3'): ").split())
        if self.is_valid_selection(row, col):
            task = self.grid.cells[row][col]
            if task:
                self.score += self.calculate_score(task)
                self.tasks_completed += 1
                self.grid.cells[row][col] = None
                print(f"Task completed! Score: {self.score}")
            else:
                self.score -= 1
                print("No task at this location. -1 point.")
        else:
            print("Invalid selection. Try again.")

    self.end_time = time.time()
    self.display_results()

def is_valid_selection(self, row, col):
    return 0 <= row < self.grid.size and 0 <= col < self.grid.size

def calculate_score(self, task):
    return task.priority * task.difficulty

def display_grid(self):
    for row in self.grid.cells:
        print(" ".join("X" if cell else "O" for cell in row))

def calculate_pme(self):
    duration_minutes = (self.end_time - self.start_time) / 60
    ntcpm = self.tasks_completed / duration_minutes
    return (ntcpm / self.grid.size) * 100

def calculate_bps(self, pme):
    total_time_seconds = self.end_time - self.start_time
    return math.log2(pme) / total_time_seconds if pme > 0 else 0

def display_results(self):
    pme = self.calculate_pme()
    bps = self.calculate_bps(pme)
    print(f"\nResults:")
    print(f"Total Score: {self.score}")
    print(f"Tasks Completed: {self.tasks_completed}")
    print(f"Project Management Efficiency (PME): {pme:.2f}")
    print(f"Bits Per Second (BPS): {bps:.2f}")
    self.provide_feedback()

def provide_feedback(self):
    print("\nFeedback:")
    if self.score > 50:
        print("Great job! You demonstrated efficient task management.")
    elif self.score > 25:
        print("Good effort. Try to prioritize high-value tasks for better efficiency.")
    else:
        print("There's room for improvement. Focus on quick decision-making and task prioritization.")

def main():
print("Welcome to the Webgrid Project Management Simulation!")
grid_size = int(input("Enter grid size (4 for small, 8 for medium, 12 for large): "))
duration = float(input("Enter simulation duration in seconds: "))

simulation = WebgridProjectManagement(grid_size, duration)
simulation.run_simulation()

if name == "main":
main()
