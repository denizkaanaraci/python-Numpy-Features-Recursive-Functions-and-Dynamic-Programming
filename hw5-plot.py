import matplotlib.pyplot as plt

dynamic_time = [0.00100016593933, 0.000999927520752, 0.0019998550415, 0.00200009346008, 0.0019998550415]
recursive_time = [0.128000020981, 0.363999843597, 2.03399991989, 13.3180000782, 66.1940000057]
counts = [15, 16, 18, 20, 22]

fig = plt.figure()
first = fig.add_subplot(211)
first.plot(counts, dynamic_time, 'ro-', lw=1, label='Dynamic Method')
first.set_ylabel("Y axis (Time)")
plt.legend(loc="lower right")

second = fig.add_subplot(212)
second.plot(counts, recursive_time, 'ro-', lw=1, label='Recursive Method')
second.set_xlabel("X axis (M+N)")
second.set_ylabel("Y axis (Time)")
plt.legend(loc="upper left")

plt.show()

exit()
