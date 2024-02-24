"""
Author: Parisa Arbab
Date: Jan 22 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link: https://youtu.be/MQrlseB7JR0

Questions:
 What are the important steps in displaying a stem-and leaf plot?
 How will your main function be organized?
 How many levels does your design have? Choose one of the lower level functions to describe in more detail.
"""



def greet_user():
    """Print a welcome message to the user."""
    print("Hello! Welcome to the Stem and Leaf Plot program.")


def get_user_input():
    """
    Prompt the user for a choice between 1, 2, 3, or 'exit'.

    Returns:
        str: The input provided by the user.
    """
    return input("Please input a 1, 2, or 3 to select a datafile, or 'exit' to quit: ")


def read_data(filename):
    """
    Read data from a given filename assuming each line contains an integer.

    Parameters:
        filename (str): The path to the data file.

    Returns:
        list: A list of integers read from the file.
    """
    with open(filename, 'r') as file:
        # Read each line in the file and convert it to an integer, then return as a list
        data = [int(line.strip()) for line in file.readlines()]
    return data

def determine_stem_leaf_digits(data):
    """
    Determine the number of digits for stems and leaves based on the data.

    Parameters:
        data (list): A list of integers from which to determine stem and leaf sizes.

    Returns:
        tuple: A tuple containing the size of stems and the size of leaves.
    """
    max_number = max(data)
    # The number of digits in the largest number minus one will be the stem size
    stem_size = len(str(max_number)) - 1
    # Leaves will always have a single digit
    leaf_size = 1
    return stem_size, leaf_size

def create_stem_and_leaf_plot(data):
    """
    Create a stem-and-leaf plot from a list of integers.

    Parameters:
        data (list): A list of integers to create the plot from.

    Returns:
        dict: A dictionary where each key is a stem and each value is a list of leaves.
    """
    stems = {}
    for number in data:
        stem = number // 10  # Divide by 10 to find the stem.
        leaf = number % 10  # Modulo 10 to find the leaf.
        # Append the leaf to the corresponding stem's list
        stems.setdefault(stem, []).append(leaf)
    return stems


def display_plot(stems):
    """
    Display the stem-and-leaf plot.

    Parameters:
        stems (dict): A dictionary containing stem keys and leaf values.
    """
    print("\nStem and Leaf Plot")
    for stem in sorted(stems):
        # Join all leaves into a string for each stem
        leaves = ' '.join(str(leaf) for leaf in sorted(stems[stem]))
        print(f"{stem} | {leaves}")


def main():
    """
    The main function that runs the stem-and-leaf plot program.

    It greets the user, prompts for input, reads the data file, creates the plot, and displays it.
    The process loops until the user decides to exit.
    """
    greet_user()
    while True:
        choice = get_user_input()
        if choice.lower() == 'exit':
            break
        elif choice in ['1', '2', '3']:
            filepath = f"C:\\Winter 2024\\HCI430-PythonProgramming\\02\\Assignment #2\\StemAndLeaf{choice}.txt"
            data = read_data(filepath)
            stems = create_stem_and_leaf_plot(data)
            display_plot(stems)

        else:
                print(f"Datafile StemAndLeaf{choice}.txt does not exist in the specified directory.")
    else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()