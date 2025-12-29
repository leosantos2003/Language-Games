import numpy as np
import random

class QLearningAgent:
    def __init__(self, name, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.name = name
        self.actions = actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        
        self.q_table = {}

    def get_q_value(self, state, action_index):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return self.q_table[state][action_index]

    def choose_action(self, state, mode='train'):
        """
        'train' -> exploration
        'test' -> exploitation
        """
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))

        if mode == 'train' and random.uniform(0, 1) < self.epsilon:
            return random.choice(range(len(self.actions)))
        else:
            return np.argmax(self.q_table[state])

    def learn(self, state, action_index, reward, next_state):
        old_value = self.get_q_value(state, action_index)
        
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(len(self.actions))
        next_max = np.max(self.q_table[next_state])
        
        new_value = old_value + self.lr * (reward + self.gamma * next_max - old_value)
        self.q_table[state][action_index] = new_value