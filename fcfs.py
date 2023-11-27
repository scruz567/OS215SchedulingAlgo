def fcfs_scheduler(tasks):
    # Sort the tasks by their arrival time
    sorted_tasks = sorted(tasks, key=lambda x: x[0])
    
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    completion_times = []

    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    
    for task in sorted_tasks:
        arrival_time, burst_time = task
        if arrival_time > current_time:
            current_time = arrival_time
        else:
            waiting_time = current_time - arrival_time
            total_waiting_time+=waiting_time
        turnaround_time = waiting_time + burst_time
        total_turnaround_time+=turnaround_time
        
        completion_time = current_time + burst_time
        completion_times.append(completion_time)

        print(f"P{sorted_tasks.index(task) + 1}\t{arrival_time}\t\t{burst_time}\t\t{completion_time}\t\t{waiting_time}\t\t{turnaround_time}")
        current_time += burst_time
    
    schedule_length = max(completion_times) - min([task[0] for task in sorted_tasks])
    throughput = len(tasks) / schedule_length
    
    average_waiting_time = total_waiting_time / len(sorted_tasks)
    average_turnaround_time = total_turnaround_time / len(sorted_tasks)
    
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)
    print("Schedule Length:", schedule_length)
    print("Throughput:", throughput)
    
def main():
    n = int(input("Enter the number of processes: "))
    tasks = []

    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process P{i + 1}: "))
        burst_time = int(input(f"Enter burst time for process P{i + 1}: "))
        tasks.append((arrival_time, burst_time))

    fcfs_scheduler(tasks)

if __name__ == "__main__":
    main()
