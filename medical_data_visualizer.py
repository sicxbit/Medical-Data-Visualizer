import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("./medical_examination.csv")

# 2
df["overweight"]= (df['weight'] / ((df['height'] / 100) ** 2)) > 25
# Convert overweight boolean to 0 or 1
df['overweight'] = df['overweight'].astype(int)
# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x:0 if x ==1 else 1)
df["gluc"] = df["gluc"].apply(lambda x:0 if x==1 else 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
    df,
    id_vars=["cardio"],
    value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )


    # 6
    plot = sns.catplot(
        x='variable',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='count',
        height=5,
        aspect=1
    )
    
    plot.set_axis_labels('variable', 'total')
    plot.set_titles('Cardio: {col_name}')
    plot.despine(left=True)

    # 7



    # 8
    fig = plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat =  df[
        (df["ap_lo"] <= df['ap_hi']) &
        (df["height"] >= df['height'].quantile(0.025)) &
        (df["height"] <= df['height'].quantile(0.975)) &
        (df["weight"] >= df['weight'].quantile(0.025)) &
        (df["weight"] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt=".1f",  
        square=True, 
        cbar_kws={"shrink": 0.75}, 
        linewidths=0.5,
        ax=ax 
    )


    # 16
    fig.savefig('heatmap.png')
    return fig