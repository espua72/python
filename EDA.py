def fxMissingValues(df, color=['black', 'white']):
    # find quantity & % of missing values and plot it the heatmap
    import seaborn as sns
    import pandas as pd
    
    #color=['darkblue', 'red'] 
    cols = df.columns
    sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(color))
    
    ma_num = []
    ma_pc =[]
    lendf = df.shape[0]
    
    for col in cols:
        manum = df[col].isna().sum()
        ma_num.append(manum)
        ma_pc.append(round(100*manum/lendf, 2))
    
    df_ma = pd.DataFrame(zip(cols, ma_num, ma_pc), columns=['Columns', 'Missing', '%'])
    return df_ma

    