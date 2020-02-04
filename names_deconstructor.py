import pandas as pd
import matplotlib as plot

def names_deconstructor(names_df, head = False):
    """
    This function takes in a dataframe with the first column 
    as a list of names or different strings and deconstructs
    them one character at a time. It returns a dataframe and
    a plot of how the deconstruction went.
    
    This should be used to find duplicates or similar words
    
    It will also accept a list, series or dict if passed and 
    turn that into a dataframe.
    
    The head is set to false by default because the analysis 
    begins at the tail end of a word. In order to start at 
    the beginning of a word please set it to true.
    
    This function requires that the user have Pandas and 
    Matplotlib.
    
    """
#     handle other types than dataframe
    if type(names_df) != 'pandas.core.frame.DataFrame':
    
        names_df = pd.DataFrame(names_df)
    
    names_df['NAME'] = names_df.iloc[:,0].copy()
    
#     setup variables and columns for analysis
    names_df['LENGTH'] = names_df['NAME'].apply(lambda x: len(x))
    
    names_df['SUB_LENGTH'] = names_df['NAME'].apply(lambda x: len(x))
    
    names_df['PERCENT_LENGTH'] = names_df['LENGTH'].apply(lambda x: round(100*x/x))
    
    analysis = {'number_names': [len(names_df['NAME'].unique())], 'avg_pct_len': [100]}
    
    avg_pct_min = min(analysis['avg_pct_len'])
    
    substring = 1
    
#     start of analysis of dataframe
    while avg_pct_min >= 50:

#         this is what chops off the words 
        if head == False:
            names_df['NAME'] = names_df['NAME'].apply(lambda x: x[:len(x)-(substring)])
        else:
            names_df['NAME'] = names_df['NAME'].apply(lambda x: x[(substring):])
        
#         this handles the length values
        names_df['SUB_LENGTH'] = names_df['SUB_LENGTH'].apply(lambda x: (x-substring))
        
        names_df['PERCENT_LENGTH'] = 100*(names_df['SUB_LENGTH']/names_df['LENGTH'])
        
#         these two lines capture the values we actually care about
        analysis['number_names'].append(len(names_df['NAME'].unique()))
        
        analysis['avg_pct_len'].append(round(names_df['PERCENT_LENGTH'].mean()))

#         the below line is for debugging
#         print(names_df['COMPANYNAME'].unique())


        # substring += 1
    
#        this determines whether we should keep looping
        avg_pct_min = min(analysis['avg_pct_len'])
    
#     now we are outside the loop
    analysis_df = pd.DataFrame(analysis)
    return analysis_df, analysis_df.plot(x='avg_pct_len', y='number_names')