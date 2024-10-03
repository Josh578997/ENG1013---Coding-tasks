import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('ai_presentation/data.csv')

# Extract the 'No. of Students' column
student_counts = df['No. of Students']

# Create the bell curve
plt.figure(figsize=(10, 6))
sns.histplot(student_counts, bins=10, kde=True, stat='density', color='skyblue')

# Add labels and title
plt.title('Bell Curve of Number of Students')
plt.xlabel('Number of Students')
plt.ylabel('Density')
plt.grid(True)

# Show the plot
plt.show()