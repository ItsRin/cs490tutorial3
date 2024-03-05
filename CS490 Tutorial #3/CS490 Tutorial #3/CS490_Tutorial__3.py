import matplotlib.pyplot as plt
import numpy as np

dos_data = np.genfromtxt('Denial-of-Service.csv', dtype=None, delimiter=',', names=True, encoding='utf-8')
sdn_data = np.genfromtxt('dataset_sdn.csv', dtype=None, delimiter=',', names=True, encoding='utf-8')

plt.figure(figsize=(10, 6))
plt.plot(dos_data['pktcount'], dos_data['bytecount'], marker='s', linestyle='-', color='red', alpha=0.5, label='Packet vs. Byte Count')
plt.title('Task 1: 2D Scatter Plot')
plt.xlabel('Packet Count (example)')
plt.ylabel('Byte Count (example)')
plt.legend()
plt.grid(True)
plt.show()

# Task 2: Scatter plot with solid linestyle and equation of the line using 'pktperflow' and 'byteperflow'
x = dos_data['pktperflow']
y = dos_data['byteperflow']
slope, intercept = np.polyfit(x, y, 1)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Original data')
plt.plot(x, intercept + slope*x, 'r', label=f'Fitted line: y={intercept:.2f}+{slope:.2f}x')
plt.title('Task 2: Scatter Plot with Line Fit')
plt.xlabel('Packets per Flow (pktperflow)')
plt.ylabel('Bytes per Flow (byteperflow)')
plt.legend()
plt.grid(True)
plt.show()

#Assessment Task II #4
slope, intercept = np.polyfit(dos_data['pktperflow'], dos_data['byteperflow'], 1)
plt.figure(figsize=(10, 6))
plt.plot(dos_data['pktperflow'], dos_data['byteperflow'], 'o', label='Original data')
plt.plot(dos_data['pktperflow'], intercept + slope*dos_data['pktperflow'], '-', label=f'Fitted line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('Packets per Flow')
plt.ylabel('Bytes per Flow')
plt.title('2D Scatter Plot with Fitted Line for Packets per Flow vs Bytes per Flow')
plt.legend()
plt.savefig('packets_per_flow_vs_bytes_per_flow.png')
print(f"Equation of the line: y = {slope}x + {intercept}")
plt.show()