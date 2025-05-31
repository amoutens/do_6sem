import matplotlib.pyplot as plt
def stats_graph_output(data1, data2):

    plt.figure(figsize=(10, 6))
    plt.plot(data1, label='Greedy')
    plt.plot(data2, label='Gale-Shapley', color='orange')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Data 1 and Data 2')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    pass