# Analyse various school outcomes in Tennessee using pandas. Suppose you are a
# public school administrator. Some schools in your state of Tennessee are
# performing below average academically. Your superintendent, under pressure
# from frustrated parents and voters, approached you with the task of understanding
# why these schools are under-performing. To improve school performance, you
# need to learn more about these schools and their students, just as a business needs
# to understand its own strengths and weaknesses and its customers. Though you is
# eager to build an impressive explanatory model, you know the importance of
# conducting preliminary research to prevent possible pitfalls or blind spots. Thus,
# you engages in a thorough exploratory analysis, which includes: a lit review, data
# collection, descriptive and inferential statistics, and data visualization.

#import inline
import pandas as pd
#%matplotlib inline
#import matplotlib.pyplot as plt
#import seaborn as sns

sns.set_style('dark_grid')
sns.set(font_scale=1.5)

df = pd.read_csv('middle_tn_schools.csv')

df.describe()

df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe()

# only view these two variables

df[['reduced_lunch', 'school_rating']].corr()

fig, ax = plt.subplots(figsize=(14,8))

ax.set_ylabel('school_rating')

# boxplot with only these two variables
_ = df[['reduced_lunch', 'school_rating']].boxplot(by='school_rating', figsize=(13,8), vert=False, sym='b.', ax=ax)

plt.figure(figsize=(14,8)) # set the size of the graph
_ = sns.regplot(data=df, x='reduced_lunch', y='school_rating')

# create tabular correlation matrix
corr = df.corr()
_, ax = plt.subplots(figsize=(13,10))

# graph correlation matrix
_ = sns.heatmap(corr, ax=ax,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values,
                cmap='cool_warm')
