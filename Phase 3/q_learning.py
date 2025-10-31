import numpy as np
import random

class QLearning:
    def __init__(self, n_states, n_actions, alpha=0, gamma=0.7, epsilon=0, epsilon_min=0.008, epsilon_decay=0.99995):
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.state_dict = {}
        self.next_state_index = 0
        self.load_q_table()

    def encode_state(self, state_tuple):
        if state_tuple not in self.state_dict:
            self.state_dict[state_tuple] = self.next_state_index
            self.next_state_index += 1
        return self.state_dict[state_tuple]

    def choose_action(self, state, allowed_actions, training=False):
        if training:
            if np.random.uniform(0, 1) < self.epsilon:
                action = random.choice(allowed_actions)  # Explore
            else:
                action = np.argmax(self.q_table[state])  # Exploit best known
            self.epsilon = max(self.epsilon_min, self.epsilon_decay * self.epsilon)
        else:
            # When not training, always pick the best action
            action = np.argmax(self.q_table[state])
        return action


    def update_q_table(self, state, action, reward, next_state):
        current_q = self.q_table[state][action]
        max_next_q = np.max(self.q_table[next_state])  # Estimate of optimal future value
        updated_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_next_q)
        self.q_table[state][action] = updated_q

    def save_q_table(self, filename="q_table_phase3.txt"):
        np.savetxt(filename, self.q_table)

    def load_q_table(self, filename="q_table_phase3.txt"):
        try:
            self.q_table = np.loadtxt(filename)
        except IOError:
            # If the file doesn't exist, initialize Q-table with zeros as per dimensions
            self.q_table = np.zeros((self.n_states, self.n_actions))
