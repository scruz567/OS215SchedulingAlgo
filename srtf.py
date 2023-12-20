from collections import deque

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def srtf_scheduler(processes):
    # Sort the tasks by their arrival time
    completed_processes = []
    time = 0
    waiting_time = [0] * len(processes)
    completion_times = [0] * len(processes)
    ready_queue = deque()
    current_process = None

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
            if current_process.remaining_time == 1: #current process is absolutely the shortest
                time += 1
                completion_times[processes.index(current_process)] = time
                waiting_time[processes.index(current_process)] += time - current_process.arrival_time - current_process.burst_time
                completed_processes.append(current_process)
                current_process = None
            
            elif ready_queue: #there exist other processes
                min_process = min(ready_queue, key=lambda obj: obj.remaining_time)
                
                if min_process.remaining_time == 1: #finish execution of shortest job
                    ready_queue.append(current_process)
                    time += 1
                    completion_times[processes.index(min_process)] = time
                    waiting_time[processes.index(min_process)] += time - min_process.arrival_time - min_process.burst_time
                    completed_processes.append(min_process)
                    ready_queue.remove(min_process)
                    current_process = None
                elif min_process.remaining_time < current_process.remaining_time: #a shorter job will run
                    time += 1
                    min_process.remaining_time -= 1
                else: #current job is the shortest
                    time += 1
                    current_process.remaining_time -= 1
            else: #no ready queue
                time += 1
                current_process.remaining_time -= 1
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

    completion_time, turnaround_time, avg_turnaround_time, waiting_time, avg_waiting_time, schedule_length, throughput = srtf_scheduler(processes)

    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i, process in enumerate(processes):
        print(f"{process.name}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Schedule Length: {schedule_length}")
    print(f"Throughput: {throughput:.2f} processes/ms")

if __name__ == "__main__":
    main()
