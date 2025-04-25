fitness_data = {"steps": 10000, "calories": 500}

def update_fitness(steps=None, calories=None):
    if steps:
        fitness_data["steps"] += steps
    if calories:
        fitness_data["calories"] += calories
    return f"Updated fitness data: {fitness_data['steps']} steps, {fitness_data['calories']} calories burned."

def fitness_summary():
    spe = f"You have walked {fitness_data['steps']} steps and burned {fitness_data['calories']} calories today."
    v= print(spe)
    return v

update_fitness(steps=20000, calories=6789)
fitness_summary()