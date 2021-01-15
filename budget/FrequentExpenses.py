from . import Expense
#import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_count = collections.Counter(spending_categories)
#print(spending_count)

top5 = spending_count.most_common()
categories, count = zip(*top5)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()