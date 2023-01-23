import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from itertools import count
import matplotlib.dates as mdates

error_codes = {
    'N': 'NO ERROR',
    'C': 'CANCELED BUT NOT FILED',
    'F': 'FILED BUT NOT CANCELED',
    'C_E': 'CANCELED BUT NO REQUEST',
    'R': 'REJECTED',
    'T': 'TRADED',
}

# Read data from CSV files
data1 = pd.read_csv('OA14Y.csv')
data1['time'] = pd.to_datetime(data1['time'], unit='ns', utc=True)
data2 = pd.read_csv('OOOTO.csv')
data2['time'] = pd.to_datetime(data1['time'], unit='ns', utc=True)
data3 = pd.read_csv('OA14Y.csv')
data3['time'] = pd.to_datetime(data1['time'], unit='ns', utc=True)
data4 = pd.read_csv('OOOTO.csv')
data4['time'] = pd.to_datetime(data1['time'], unit='ns', utc=True)

# Create figure and axes
fig = plt.figure(figsize=(50,8))
ax1 = fig.add_subplot(411)  # 4 rows, 1 column, subplot 1
ax3 = fig.add_subplot(412)
ax2 = fig.add_subplot(413)  # 4 rows, 1 column, subplot 3
ax4 = fig.add_subplot(414)  # 4 rows, 1 column, subplot 4

ax1.xaxis_date()
ax2.xaxis_date()
ax3.xaxis_date()
ax4.xaxis_date()

ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
ax3.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
ax4.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))


ax1.set_title("Price Evolution Of OA14Y Over Time")
ax1.set_xlabel("Time (UTC)")
ax1.set_ylabel("Price")

ax2.set_title("Price Evolution Of OOOTO Over Time")
ax2.set_xlabel("Time (UTC)")
ax2.set_ylabel("Price")

ax3.set_title("Error Types For OA14Y")
ax3.set_xlabel("Time (UTC)")
ax3.set_ylabel("Error Code")

ax4.set_title("Error Types For OOOTO")
ax4.set_xlabel("Time (UTC)")
ax4.set_ylabel("Error code")

x_values1 = []
y_values1 = []
x_values2 = []
y_values2 = []
x_values3 = []
y_values3 = []
x_values4 = []
y_values4 = []

def animate(i):
    x = next(index)
    counter = next(index)
    x_values1.append(data1['time'][x])
    y_values1.append(data1['close'][x])
    x_values2.append(data2['time'][x])
    y_values2.append(data2['close'][x])
    x_values3.append(data1['time'][x])
    y_values3.append(data1['error'][x])
    x_values4.append(data2['time'][x])
    y_values4.append(data2['error'][x])

    if counter > 40:
        x_values1.pop(0)
        y_values1.pop(0)
        x_values2.pop(0)
        y_values2.pop(0)
        x_values3.pop(0)
        y_values3.pop(0)
        x_values4.pop(0)
        y_values4.pop(0)
        
    ax1.set_xlim(min(x_values1), max(x_values1))
    ax1.plot(x_values1, y_values1,linestyle='--', c='r')
    ax2.set_xlim(min(x_values2), max(x_values2))
    ax2.plot(x_values2, y_values2,linestyle='--', c='b')
    ax3.plot(x_values4, y_values4,linestyle='--', c='g')
    ax4.plot(x_values4, y_values4,linestyle='--', c='y')

index = count()
fig.subplots_adjust(hspace=0.7)
ani = animation.FuncAnimation(fig, animate, interval=700)
plt.show()
