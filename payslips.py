import random

genders = ['male', 'female']
workers = []

for i in range(1, 401):
    workers.append({
        'worker_id': i,
        'gender': random.choice(genders),
        'salary': random.randint(6000, 32000)
    })

# go through each worker and generate payslip
for worker in workers:
    try:
        level = "Unassigned"

        if worker['salary'] > 10000 and worker['salary'] < 20000:
            level = "A1"

        if 7500 < worker['salary'] < 30000 and worker['gender'] == 'female':
            level = "A5-F"

        print(f"Payment Slip for worker with ID:  {worker['worker_id']}")
        print(f"Gender: {worker['gender']}")
        print(f"Salary: ${worker['salary']}")
        print(f"Employee Level: {level}")
        print("-" * 100)

    except Exception as e:
        print(
            f"An error occurred while processing worker {worker['worker_id']}: {e}")
