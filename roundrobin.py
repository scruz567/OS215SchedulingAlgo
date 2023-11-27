from collections import deque

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def preemptive_round_robin(processes, time_quantum):
    time = 0
    completed_processes = []
    waiting_time = [0] * len(processes)
    ready_queue = deque()
    current_process = None
    completion_times = [0] * len(processes)

    while len(completed_processes) < len(processes):
        # Check for new arrivals
        for process in processes:
            if process.arrival_time <= time and process not in completed_processes and process not in ready_queue:
                if process != current_process:
                    ready_queue.append(process)
        
        if current_process:    
            ready_queue.append(current_process)


        if ready_queue:
            current_process = ready_queue.popleft()

        if current_process:
            if current_process.remaining_time <= time_quantum and current_process.remaining_time > 0:
                time += current_process.remaining_time
                completion_times[processes.index(current_process)] = time
                waiting_time[processes.index(current_process)] += time - current_process.arrival_time - current_process.burst_time
                current_process.remaining_time = 0
                completed_processes.append(current_process)
                current_process = None
                
            else:
                time += time_quantum
                current_process.remaining_time -= time_quantum
        else:
            time += 1


    turnaround_time = [burst_time + wait_time for burst_time, wait_time in zip([p.burst_time for p in processes], waiting_time)]
    avg_turnaround_time = sum(turnaround_time) / len(processes)
    avg_waiting_time = sum(waiting_time) / len(processes)
    schedule_length = time
    throughput = len(processes) / schedule_length

    return completion_times, turnaround_time, avg_turnaround_time, waiting_time, avg_waiting_time, schedule_length, throughput

def main():
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        name = input(f"Enter the name of process {i + 1}: ")
        arrival_time = int(input(f"Enter the arrival time for {name} (ms): "))
        burst_time = int(input(f"Enter the burst time for {name} (ms): "))
        processes.append(Process(name, arrival_time, burst_time))

    time_quantum = int(input("Enter the time quantum (ms): "))

    completion_time, turnaround_time, avg_turnaround_time, waiting_time, avg_waiting_time, schedule_length, throughput = preemptive_round_robin(processes, time_quantum)

    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i, process in enumerate(processes):
        print(f"{process.name}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Schedule Length: {schedule_length}")
    print(f"Throughput: {throughput:.2f} processes/ms")

if __name__ == "__main__":
    main()
