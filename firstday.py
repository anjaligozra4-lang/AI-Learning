# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# # floor and ceiling operations,math
# import math 
# print(math.floor(16.00))

# import math
# print(math.ceil(16.00))
# # random number generation
# import random
# print(random.randint(1, 100))
# # datatime module
# from datetime import date, datetime, time
# print(datetime.now())

# from datetime import datetime
# print(date.today())

# from datetime import datetime
# print("current date and time:", datetime.now())

# # import os 
# # print(os)
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr.max())

# import numpy as np
# arr = np.array([1, 2, -3, 4, 5])
# print(arr.min())

# import numpy as np
# arr = np.array([1, 2, -3, 4, 5])
# print(arr.mean())

# matrix
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 12,])
# print(arr.reshape(4, 2))
# # element-wise addition of two arrays,multiplication,subtraction
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# print(arr1 + arr2)
# print(arr1 * arr2)
# print(arr1 - arr2)
# print(arr1 / arr2)
# sum of two arrays
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# print (np.sum(arr1))
# print (np.sum(arr2))



# pandas
import pandas as pd
data = {'Name': ['anjali', 'mannat', 'rama', 'asha'],
        'Age': [21, 21, 24, 22]}
df = pd.DataFrame(data)
print(df)

# pandas
import pandas as pd
data = {'Name': ['anjali', 'mannat', 'rama', 'asha'],
        'Age': [21, 21, 24, 22]}
df = pd.DataFrame(data)
print(df['Name'])

# pandas
import pandas as pd
data = {'Name': ['anjali', 'mannat', 'rama', 'asha'],
        'Age': [21, 21, 24, 22]}
df = pd.DataFrame(data)
print(df['Age'])

# pandas filter
import pandas as pd
data = {'Name': ['anjali', 'mannat', 'rama', 'asha'],
        'Age': [21, 21, 24, 22]}
df = pd.DataFrame(data)
print(df[df['Age']>21]) # it will filter the data and return only those rows where the age is greater than 21

# pandas mean age
import pandas as pd
data = {'Name': ['anjali', 'mannat', 'rama', 'asha'],
        'Age': [21, 21, 24, 22]}
df = pd.DataFrame(data)
print(df['Age'].mean())

# pandas maximum age
import pandas as pd
data = {'Name': ['anjali', 'mannat', 'rama', 'asha'],
        'Age': [21, 21, 24, 22]}
df = pd.DataFrame(data)
print(df['Age'].max())


# matplotlib
# line plot
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 200, 300, 400, 500, 600]
plt.plot(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()
# bar chart
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 200, 300, 400, 500, 600]
plt.bar(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()
# pie chart
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 200, 300, 400, 500, 600]
plt.pie(sales, labels=months, autopct='%1.1f%%')
plt.title('Sales Data')
plt.show()
# scatter plot
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 200, 300, 400, 500, 600]
plt.scatter(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()