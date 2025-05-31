from greedy_alg import GreedyAlgorithm
def main():
    m = 3  
    n = 4  
    W = {0: 85, 1: 80, 2: 73, 3: 97}  
    Q = [2, 2, 3]  
    P = {         
        0: [1, 2],
        1: [0, 1],
        2: [0, 2],
        3: [1, 2]
    }

    greedy_alg = GreedyAlgorithm(m, n, W, Q, P)
    greedy_alg.greedy_algorithm()
    greedy_alg.print_matrix()
    S = greedy_alg.calculate_objective_function()
    print(f"Цільова функція S = {S}")

if __name__ == "__main__":
    main()
