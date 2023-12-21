def first_fit(partitions, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(partitions)):
            if partitions[j] >= processes[i]:
                allocation[i] = j
                partitions[j] -= processes[i]
                break
    if -1 in allocation:
        return (False)
    return (True)


def next_fit(partitions, processes):
    allocation = [-1] * len(processes)
    j = 0

    for i in range(len(processes)):
        while j < len(partitions):
            if partitions[j] >= processes[i]:
                allocation[i] = j
                partitions[j] -= processes[i]
                break
            j = (j + 1) % len(partitions)
    if -1 in allocation:
        return False
    return True


def best_fit(partitions, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_fit_index = -1
        for j in range(len(partitions)):
            if partitions[j] >= processes[i]:
                if best_fit_index == -1 or partitions[j] < partitions[best_fit_index]:
                    best_fit_index = j

        if best_fit_index != -1:
            allocation[i] = best_fit_index
            partitions[best_fit_index] -= processes[i]
    if -1 in allocation:
        return (False)
    return (True)


def worst_fit(partitions, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_fit_index = -1
        for j in range(len(partitions)):
            if partitions[j] >= processes[i]:
                if worst_fit_index == -1 or partitions[j] > partitions[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocation[i] = worst_fit_index
            partitions[worst_fit_index] -= processes[i]
    if -1 in allocation:
        return(False)
    return (True)


def main():
    partitions = [
        {"size": 50},
        {"size": 150},
        {"size": 300},
        {"size": 350},
        {"size": 600}]
    print("The memory is intially partitioned into 50--150--300--350--600")
    for part in partitions:
        fill = input(f"Would you like to fill partition {part}? YES/NO ")
        if fill == "YES":
            part["size"] == 0;               
    
    input_array = input('Enter processes for the array separated by spaces: ex. 300 25 125 50  ')
    processes = input_array.split()
    processes = [int(element) for element in processes]

    # Simulate algorithms
    print("First Fit: " + str(first_fit([partition['size'] for partition in partitions], processes)))
    print("Worst Fit: " + str(worst_fit([partition['size'] for partition in partitions], processes)))
    print("Next Fit: " + str(next_fit([partition['size'] for partition in partitions], processes)))
    print("Best Fit: " + str(best_fit([partition['size'] for partition in partitions], processes)))

if __name__ == "__main__":
    main()