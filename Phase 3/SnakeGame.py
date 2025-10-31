"""
Snake Eater Game
Made with PyGame
Last modification in April 2024 by José Luis Perán
Machine Learning Classes - University Carlos III of Madrid
"""
from snake_env import SnakeGameEnv
from q_learning import QLearning
import pygame
import sys

def main():
    # Window size
    FRAME_SIZE_X = 150
    FRAME_SIZE_Y = 150
    
    # Colors (R, G, B)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)
    
    difficulty = 0  # Adjust as needed
    render_game = True # Show the game or not
    growing_body = True # Makes the body of the snake grow
    training =  False # Defines if it should train or not

    # Initialize the game window, environment and q_learning algorithm
    # Your code here.
    # You must define the number of possible states.
    # number_states = whatever
    

    pygame.init()
    number_states = int(2**9)  # binary features
    def state_to_index(state_list, max_states=number_states):
        binary_string = "".join(str(x) for x in state_list)
        index = int(binary_string, 2)
        return min(index, max_states - 1)  # clamp if needed
    num_episodes = 100
    env = SnakeGameEnv(FRAME_SIZE_X, FRAME_SIZE_Y, growing_body)
    ql = QLearning(n_states=number_states, n_actions=4)  
    # num_episodes = the number of episodes you want for training.


    if render_game:
        game_window = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))
        fps_controller = pygame.time.Clock()
    scores = []
    total_steps_all = 0
    total_fruits_all = 0
    loop_count = 0  # Count the number of loops without eating fruit
    
    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0
        max_reward = 0
        game_over = False

        steps = 0
        fruits_eaten = 0

        while not game_over:
            binary_state = state
            state_index = state_to_index(binary_state)

            allowed_actions = [0, 1, 2, 3]
            action = ql.choose_action(state_index, allowed_actions)
            next_state, reward, game_over = env.step(action)
            next_state_binary = next_state
            next_state_index = state_to_index(next_state_binary)


            if training:
                ql.update_q_table(state_index, action, reward, next_state_index)

            state = next_state
            total_reward += reward
            max_reward = max(max_reward, total_reward)
            steps += 1

            if reward > 9:
                fruits_eaten += 1

            
            # Rendering and quitting logic (no changes)
            if render_game:
                game_window.fill(BLACK)
                snake_body = env.get_body()
                food_pos = env.get_food()
                for pos in snake_body:
                    pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
                pygame.draw.rect(game_window, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print(f"Episode {episode+1}: Steps = {steps}, Fruits eaten = {fruits_eaten}, Total reward = {total_reward}, Max reward = {max_reward}")
                        pygame.quit()
                        sys.exit()

                pygame.display.flip()
                fps_controller.tick(difficulty)

            if env.steps_since_last_food > 5000:
                game_over = True
                #reward = -200  # Strong penalty to learn from it
                loop_count += 1  # Count the loop
                print(f"Episode {episode+1}: Loop count = {loop_count}, Steps = {steps}, Fruits eaten = {fruits_eaten}, Total reward = {total_reward}, Max reward = {max_reward}")
                
            if env.check_game_over():
                break

        ql.save_q_table()

        # Imprimir estadísticas del episodio
        print(f"Episode {episode+1}: Steps = {steps}, Fruits eaten = {fruits_eaten}, Total reward = {total_reward}, Max reward = {max_reward}")
        scores.append(total_reward)

        total_steps_all += steps
        total_fruits_all += fruits_eaten
        

    # Imprimir medias al finalizar todos los episodios
    print("\n=== Training Summary ===")
    print(f"Average steps per episode: {total_steps_all / num_episodes:.2f}")
    print(f"Average fruits eaten per episode: {total_fruits_all / num_episodes:.2f}")
    print(f"Average total reward per episode: {sum(scores) / num_episodes:.2f}")
    print(f"Maximum total reward: {max(scores)}")
    print(f"Loop count: {loop_count}")


if __name__ == "__main__":
    main()
