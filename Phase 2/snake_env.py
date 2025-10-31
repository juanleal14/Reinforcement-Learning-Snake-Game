"""
Snake Eater Environment
Made with PyGame
Last modification in April 2024 by José Luis Perán
Machine Learning Classes - University Carlos III of Madrid
"""
import numpy as np
import random
from collections import deque
class SnakeGameEnv:
    def __init__(self, frame_size_x=150, frame_size_y=150, growing_body=True):
        # Initializes the environment with default values
        self.frame_size_x = frame_size_x
        self.frame_size_y = frame_size_y
        self.growing_body = growing_body
        self.reset()

    def reset(self):
        # Resets the environment with default values
        self.snake_pos = [50, 50]
        self.snake_body = [[50, 50], [60, 50], [70, 50]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10, random.randrange(1, (self.frame_size_y // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        self.steps_since_last_food = 0  # NEW LINE
        return self.get_state()

    def step(self, action):
        # Implements the logic to change the snake's direction based on action
        # Update the snake's head position based on the direction
        # Check for collision with food, walls, or self
        # Update the score and reset food as necessary
        # Determine if the game is over
        self.update_snake_position(action)
        reward = self.calculate_reward()
        self.update_food_position()
        state = self.get_state()
        self.game_over = self.check_game_over()
        return state, reward, self.game_over


    def get_state(self):
        from collections import deque

        hx, hy = self.snake_pos
        fx, fy = self.food_pos
        segments = self.snake_body

        # Relative food position
        to_left  = int(fx < hx)
        to_right = int(fx > hx)
        to_up    = int(fy < hy)
        to_down  = int(fy > hy)

        # Basic collision detection
        def hits_obstacle(cell):
            x, y = cell
            return (
                x < 0 or x >= self.frame_size_x or
                y < 0 or y >= self.frame_size_y or
                cell in segments[1:]
            )

        # Flood-fill to check if a cell leads to the tail
        def reachable_from(start):
            visited = set()
            pending = deque([tuple(start)])
            tail = tuple(segments[-1])
            body_excl_tail = set(tuple(b) for b in segments[:-1])

            while pending:
                node = pending.popleft()
                if node == tail:
                    return True

                for dx, dy in [(10, 0), (-10, 0), (0, 10), (0, -10)]:
                    neighbor = (node[0] + dx, node[1] + dy)
                    if neighbor not in visited and neighbor not in body_excl_tail:
                        x, y = neighbor
                        if 0 <= x < self.frame_size_x and 0 <= y < self.frame_size_y:
                            visited.add(neighbor)
                            pending.append(neighbor)
            return False

        # Next potential moves
        north = [hx, hy - 10]
        south = [hx, hy + 10]
        west  = [hx - 10, hy]
        east  = [hx + 10, hy]

        # Check safe movement directions
        safe_north = int(not hits_obstacle(north) and reachable_from(north))
        safe_south = int(not hits_obstacle(south) and reachable_from(south))
        safe_west  = int(not hits_obstacle(west)  and reachable_from(west))
        safe_east  = int(not hits_obstacle(east)  and reachable_from(east))

        state = [
            to_up,
            to_down,
            to_left,
            to_right,
            safe_north,
            safe_south,
            safe_west,
            safe_east
        ]

        return state






        
    def get_body(self):
        return self.snake_body
 
    def get_food(self):
        return self.food_pos

    def calculate_reward(self):
        if self.check_game_over():
            return -25  # Strong negative reward on death

        # Distance before move
        prev_head = self.snake_body[1]  # second block is where head came from
        prev_distance = abs(self.food_pos[0] - prev_head[0]) + abs(self.food_pos[1] - prev_head[1])
        curr_distance = abs(self.food_pos[0] - self.snake_pos[0]) + abs(self.food_pos[1] - self.snake_pos[1])

        if self.snake_pos == self.food_pos:
            self.steps_since_last_food = 0
            return +10  # Reward for eating
        
        #if self.steps_since_last_food > 1500:  # You can tweak this threshold
        #    return -10  # Penalty for stalling too long
        if curr_distance < prev_distance:
            return +0.9  # Reward for moving closer
        elif curr_distance > prev_distance:
            return -1.1
        else:
            return -0.3  # Small penalty for moving away or same distance



        
    def check_game_over(self):
        # Return True if the game is over, else False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x-10:
            return True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y-10:
            return True
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                return True
                
        return False

    def update_snake_position(self, action):
        # Updates the snake's position based on the action
        # Map action to direction
        change_to = ''
        direction = self.direction
        if action == 0:
            change_to = 'UP'
        elif action == 1:
            change_to = 'DOWN'
        elif action == 2:
            change_to = 'LEFT'
        elif action == 3:
            change_to = 'RIGHT'
    
        # Move the snake
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
    
        if direction == 'UP':
            self.snake_pos[1] -= 10
        elif direction == 'DOWN':
            self.snake_pos[1] += 10
        elif direction == 'LEFT':
            self.snake_pos[0] -= 10
        elif direction == 'RIGHT':
            self.snake_pos[0] += 10
            
        self.direction = direction
        
        
        self.snake_body.insert(0, list(self.snake_pos))
        
        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            self.score += 10
            self.steps_since_last_food = 0  # reset step counter on eating
            self.food_spawn = False
            # If the snake is not growing
            if not self.growing_body:
                self.snake_body.pop()
        else:
            self.snake_body.pop()
            self.steps_since_last_food += 1  # increment when not eating
    
    def update_food_position(self):
        if not self.food_spawn:
            while True:
                new_food_pos = [
                    random.randrange(1, (self.frame_size_x // 10)) * 10,
                    random.randrange(1, (self.frame_size_y // 10)) * 10
                ]
                if new_food_pos not in self.snake_body:
                    self.food_pos = new_food_pos
                    break
        self.food_spawn = True
        
        

