import matplotlib.pyplot as plt
import numpy as np
import random

agents = []

INITIAL_M = 1000
NUMBER_OF_AGENTS = 100
ITER = int(10E6)
# EM 1.0 temos a mesma situação da função a_exchange_agents
LAMBDA = float(0.25)


def popular_agents():
    global agents
    agents = [float(INITIAL_M) for i in range(NUMBER_OF_AGENTS)]


def rand_agents():
    i = random.randint(0, NUMBER_OF_AGENTS - 1)
    j = random.randint(0, NUMBER_OF_AGENTS - 1)
    return i, j


# swap de valor apenas
def a_exchange_agents():
    e = random.random()
    i, j = rand_agents()

    if i == j:
        return False

    t_sum = agents[i] + agents[j]

    a = (1.0 - e) * t_sum

    # garante que a transação será sempre positiva
    if a >= 0.0:
        b = e * t_sum

        agents[i] = b
        agents[j] = a

        return True

    return False


# swap de valor com um save money
def b_exchange_agents():
    e = random.random()
    i, j = rand_agents()

    if i == j:
        return False

    t_sum = agents[i] + agents[j]

    a = (1.0 - e) * t_sum

    # garante que a transação será sempre positiva
    if a >= 0.0:
        b = e * t_sum

        sig = (1.0 - LAMBDA) * (e * agents[j] - (1 - e) * agents[i])

        if (b - sig) >= 0.0 and (a + sig) >= 0.0:
            agents[i] = a + sig
            agents[j] = b - sig

        return True

    return False


def plot_agents(sorted_agents: [float]):
    fig, ax = plt.subplots()

    ax.bar(range(0, NUMBER_OF_AGENTS), sorted_agents, width=1, edgecolor="white", linewidth=0.5)

    ax.set(xlim=(0, NUMBER_OF_AGENTS * 1.2), xticks = np.arange(0, NUMBER_OF_AGENTS * 1.2, step=NUMBER_OF_AGENTS * 0.1),
           ylim=(0, sorted_agents[0] * 1.2), yticks = np.arange(0, sorted_agents[0] * 1.2, step = sorted_agents[0] * 0.2))

    plt.show()


def twenty_percent_value(sorted_agents: [float]):
    sum_money_agents = sum(sorted_agents)
    iter_sum = 0
    count_agents = 0
    for agent in sorted_agents:
        count_agents += 1
        iter_sum += agent
        if (iter_sum / sum_money_agents) >= 0.80:
            break

    print(f'number of agents {NUMBER_OF_AGENTS}')
    print(f'number of agents that corresponds to 80.0% of the wealth {count_agents}')
    print(f"percentage that corresponds to 80.0% of the wealth {round((count_agents / NUMBER_OF_AGENTS) * 100, 2)}%")


def __main__():
    popular_agents()

    print(f"ITERACTION: {ITER}")

    PERC_ITER = (ITER * 0.01)

    for i in range(ITER):
        b_exchange_agents()

        if(i % PERC_ITER) == 0:
            print(f"{round((i / ITER) * 100)} %")

    print(f"ALL INITIAL MONEY: {INITIAL_M * NUMBER_OF_AGENTS} - SUM ALL MONEY: {round(sum(agents), 2)}")

    sorted_agents = sorted(agents, key=lambda k: float(k), reverse=True)

    twenty_percent_value(sorted_agents)
    plot_agents(sorted_agents)


__main__()
