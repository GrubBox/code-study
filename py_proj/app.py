
import matplotlib.pyplot as plt

# Data for the plot
rounds = ['Seed', 'Series A', 'Series B', 'Series C', 'Series D', 'Series E']
valuations = [4000000, 162980000, 208260000, 1000000000, 3500000000, 7000000000]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(rounds, valuations, marker='o')

# Set logarithmic scale for y-axis
plt.yscale('log')

# Add grid lines
plt.grid(True, which="both", ls="--")

# Add labels and title
plt.xlabel('Funding Round')
plt.ylabel('Valuation ($)')
plt.title('Scale AI Funding Rounds and Valuations')

# Display the plot
plt.show()
