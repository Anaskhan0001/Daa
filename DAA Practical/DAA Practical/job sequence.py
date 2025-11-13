# Job class to store details of each job
class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

# Function to schedule jobs to maximize profit
def job_sequencing(jobs):
    # Sort jobs by descending profit (Greedy step)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    slots = [-1] * max_deadline

    total_profit = 0
    job_sequence = []

    for job in jobs:
        # Find a slot from deadline backwards
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[slot] == -1:
                slots[slot] = job.id
                total_profit += job.profit
                job_sequence.append(job.id)
                break

    print("\nScheduled Jobs in Order:", job_sequence)
    print("Total Profit:", total_profit)

# -------------------
# Main Program

jobs_list = []

n = int(input("Enter number of jobs: "))

for i in range(n):
    job_id = input(f"\nEnter Job ID for Job {i+1}: ")
    deadline = int(input(f"Enter Deadline for Job {job_id}: "))
    profit = int(input(f"Enter Profit for Job {job_id}: "))
    jobs_list.append(Job(job_id, deadline, profit))

# Run Job Sequencing
job_sequencing(jobs_list)
