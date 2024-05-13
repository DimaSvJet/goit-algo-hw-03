import numpy as np
import pandas as pd

num_throws = 100000
dice_1 = []
dice_2 = []

for _ in range(num_throws):
    # 2 - 12
    dice_1.append(np.random.randint(low=1, high=7))
    dice_2.append(np.random.randint(low=1, high=7))

points_table = pd.DataFrame(
    {'Dice 1': dice_1, 'Dice 2': dice_2}, index=range(1, num_throws+1))

points_table['Sum of dice'] = 0


def sum_of_dice(row):
    row['Sum of dice'] = row['Dice 1'] + row['Dice 2']
    return row


points_table = points_table.apply(sum_of_dice, axis='columns')

grouped_table = points_table.groupby(['Sum of dice'])[
    'Sum of dice'].agg(['count'])


def probability(row):
    row['predict'] = row['count'] * 100 / num_throws
    return row


probability_table = grouped_table.apply(probability, axis='columns')

probability_table['dictionary'] = [
    2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]


print(probability_table)
