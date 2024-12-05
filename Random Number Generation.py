import matplotlib.pyplot as plt

def mid_square_method(seed, n_digits=4):

    squared = str(seed ** 2).zfill(2 * n_digits)
    mid = len(squared) // 2 # Find the middle 
    return int(squared[mid - n_digits // 2:mid + n_digits // 2])

def lcg(seed, a, c, m, n, range_min, range_max):
    """
        range_min (int): Minimum value in the range.
        range_max (int): Maximum value in the range.
    """
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        scaled_value = range_min + (x / m) * (range_max - range_min)
        numbers.append(scaled_value)
    return numbers

def hybrid_prng():
    """
    Hybrid PRNG combining Mid-Square and LCG.
    Allows user to specify the number of random numbers and the range.
    """
    # Step 1: User inputs
    initial_seed = int(input("Enter an initial seed (integer): "))
    n_numbers = int(input("Enter the number of random numbers to generate: "))
    range_min = float(input("Enter the minimum value of the range: "))
    range_max = float(input("Enter the maximum value of the range: "))

    # Step 2: Generate seed using Mid-Square method
    mid_square_seed = mid_square_method(initial_seed)

    # Step 3: LCG constants
    a = 1103515245  
    c = 12345       
    m = 2**31       

    # Step 4: Generate numbers using LCG
    random_numbers = lcg(mid_square_seed, a, c, m, n_numbers, range_min, range_max)

    # Step 5: Visualization - Uniformity Test
    plt.hist(random_numbers, bins=10, color='blue', alpha=0.7, edgecolor='black')
    plt.title("Hybrid PRNG Output - Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

# Run the hybrid PRNG
hybrid_prng()
