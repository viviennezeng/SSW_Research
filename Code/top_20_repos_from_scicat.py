import pandas as pd

# Load dataset
df = pd.read_pickle('SciCatDatasetV1.pkl')

# Filter for scientific application software
df_filtered = df[
    df['isScientificAppSoftware'].str.strip().str.lower() == 'yes'
]
# Drop rows with missing values in key columns
df_filtered = df_filtered.dropna(subset=['NumCommits', 'NumAuthors', 'NumActiveMon'])

# Convert numeric columns just in case they're stored as strings
df_filtered['NumCommits'] = df_filtered['NumCommits'].astype(int)
df_filtered['NumAuthors'] = df_filtered['NumAuthors'].astype(int)
df_filtered['NumActiveMon'] = df_filtered['NumActiveMon'].astype(int)

# Sort by scientific activity
df_top = df_filtered.sort_values(
    by=['NumCommits', 'NumAuthors', 'NumActiveMon'],
    ascending=False
)

# Select top 20 repos
df_top_20 = df_top.head(20)
