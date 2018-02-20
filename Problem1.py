from enum import Enum
import numpy as np

class CoinState(Enum):
    """The state if (Tail, Tail, Head) occured"""
    Success = 1
    Failure = 0

class Game():
    def __init__(self,id, success_prob):
        self._id = id
        self._success_prob = success_prob
        self._rnd = np.random
        self._rnd.seed(id)
        self._coinstate = CoinState.Failure
        self._suc_times = 0
        self._reward = 0


    def simulate(self, n_time_steps):
        t = 0 #iteration times
        while t+1 < n_time_steps:
            if self._rnd.sample() < self._success_prob:
               self._coinstate = CoinState.Success
               self._suc_times +=1
               t += 3
            t += 1

    def get_reward(self):
        self._reward = self._suc_times *100 - 250
        return self._reward

class Cohort():
    def __init__(self, id, size, success_prob):
        self._id = id
        self._size = size
        self._success_prob =success_prob
        self._games = []
        self._rewards = []

        for i in range(size):
            game_m = Game(id * size + i, success_prob)
            self._games.append(game_m)

    def simulate(self, n_times_steps):
        for game in self._games:
            game.simulate(n_times_steps)
            value = game.get_reward()
            self._rewards.append(value)

    def get_ave_reward(self):
        return sum(self._rewards)/len(self._rewards)

# simulate a game
Time_Steps = 19
Successrate = 0.125
size = 1000

game1 = Game(id = 1, success_prob=Successrate)
game1.simulate(n_time_steps=Time_Steps)
print(game1.get_reward())

#Simulate a cohort
cohort1 = Cohort(id=0, size = size, success_prob=Successrate)
cohort1.simulate(n_times_steps=Time_Steps)
print(cohort1.get_ave_reward())











