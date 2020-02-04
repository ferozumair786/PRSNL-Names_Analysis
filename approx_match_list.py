def approx_match_list(names, decision_boundary = 0.75):
    """
    This function takes in a list of strings or names that are approximate matches
    along with a decision boundary value of what percent of each of the strings 
    should be compared to the list itself. 

    The decision boundary is set to 0.75 or 75% by default.

    The function returns a consolidated list of names or words that should no longer
    have approximate matches
    
    """

    # convert percentage value to decimal
    if decision_boundary > 1:
        decision_boundary = decision_boundary/100

    names_nospecial = [''.join(e for e in string if e.isalnum()) for string in names] 
    
    names_substr = [name[:round(len(name)*decision_boundary)] for name in names_nospecial]

    approx_match_names = []

    approx_match_substr = []

    for name, substr in zip(names, names_substr):

        if substr not in approx_match_names:

            approx_match_names.append(name)
            approx_match_substr.append(substr)

    return approx_match_names






