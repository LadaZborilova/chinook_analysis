import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = psycopg2.connect(
    host="localhost",
    dbname="chinook",
    user="postgres",
    password="Polokolo"
)


query = """
    SELECT artist_id, COUNT(*) AS album_count
    FROM album
    GROUP BY artist_id
    ORDER BY album_count DESC
    LIMIT 10;
"""



import matplotlib.pyplot as plt
import pandas as pd


data = {
    'kategorie': ['A', 'B', 'C', 'D', 'E'],
    'hodnota': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)


fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# První graf
axes[0, 0].bar(df['kategorie'], df['hodnota'], color='skyblue')
axes[0, 0].set_title('Graf 1')
axes[0, 0].set_xlabel('Kategorie')
axes[0, 0].set_ylabel('Hodnota')

# Druhý graf
axes[0, 1].plot(df['kategorie'], df['hodnota'], color='orange')
axes[0, 1].set_title('Graf 2')
axes[0, 1].set_xlabel('Kategorie')
axes[0, 1].set_ylabel('Hodnota')

# Třetí graf
axes[1, 0].pie(df['hodnota'], labels=df['kategorie'], autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow', 'purple'])
axes[1, 0].set_title('Graf 3')

# Čtvrtý graf
axes[1, 1].hist(df['hodnota'], bins=5, color='purple')
axes[1, 1].set_title('Graf 4')
axes[1, 1].set_xlabel('Hodnoty')
axes[1, 1].set_ylabel('Frekvence')

# všechny grafy
plt.tight_layout() 
plt.show()