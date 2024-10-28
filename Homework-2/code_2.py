import random

# Function to generate random weights for edges
def generate_weights(num_nodes):
    weights = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10) 
            weights.append((i, j, weight))
    return weights

# Function to write edges with random weights to a text file
def write_weights_to_file(weights, filename):
    with open(filename, "w") as file:
        for edge in weights:
            file.write("{}, {}, {}\n".format(edge[0], edge[1], edge[2]))
    print(f"Random weights saved to {filename}")

# Main function
def main():
    num_nodes = 100
    weights1 = generate_weights(num_nodes)
    weights2 = generate_weights(num_nodes)

    write_weights_to_file(weights1, "question2_1.txt")
    write_weights_to_file(weights2, "question2_2.txt")

if __name__ == "__main__":
    main()
