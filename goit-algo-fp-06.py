
def greed_algo(items, budget):
    # сортуємо словник за найбільшим відношенням калорій до вартості
    items_sorted = sorted(
        items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)

    total_calories = 0
    lim_budget = budget
    chosen_items = []

    for item, detail in items_sorted:
        if detail['cost'] <= lim_budget:
            total_calories += detail['calories']
            chosen_items.append(item)
            lim_budget -= detail['cost']

    return total_calories, budget-lim_budget, chosen_items


def dynamic_algo(items, budget):

    # Формуємо перелік продуктів
    item_names = list(items.keys())

    # Формуємотаблицю, де строки - порядковий номер за бюджетом +1, с стовбці - кількість страв +1
    # Таблиця має нульові значення
    db_table = [[0 for x in range(budget+1)] for y in range(len(items)+1)]

    # починаємо заповнювати таблицю
    for i in range(1, len(items)+1):
        # для кожного продукту i
        # формуємо функції, що повертають вартість та калорії кожної побранної страви
    
        item_name = item_names[i-1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']

        # формуємо таблицю з вартістю
        for w in range(1, budget+1):
            print(w)
            # для кожного порядкогового номеру строки за бюджетом
            # якщо вартість продукту <= п/н за бюджетом
            if item_cost <= w:
                # заповнюємо таблицю за продуктом (і) та бюджетом (w) обираючі максимальне значення між
                # db_table[i-1][w-item_cost] - максимальна вартість продуктів, які можна придбати на бюджет з урахуванням всіх продуктів до i
                db_table[i][w] = max(item_calories + db_table[i-1][w-item_cost], db_table[i-1][w])  # тут дійсно не зрозуміло чому ми кілокалорії додаємо до різниці бюджету та вартості продуктів
                print(db_table[i-1][w-item_cost])
            else:  
                # заповнюємо занчення таблиці значенням всіх продуктів до i
                db_table[i][w] = db_table[i-1][w]
    
    # вибираємо дані з таблиці:
    chosen_items = []
    w = budget
    total_calories = db_table[len(items)][budget] 
    total_costs = 0
    for i in range(len(items),0,-1):
        item_name = item_names[i-1]
        item_cost = items[item_name]['cost']

        if db_table[i][w] != db_table[i-1][w]:
            chosen_items.append(item_name)
            total_costs += item_cost
            w-=item_cost
    return total_calories, total_costs, chosen_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


budget = 105
print(greed_algo(items, budget))
print(dynamic_algo(items, budget))
