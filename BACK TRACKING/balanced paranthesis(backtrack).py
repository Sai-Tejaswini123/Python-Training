#balanced parenthesis(backtrack):
def parentheses(n,open_count=0,close_count=0, s=''):
    if len(s)==2*n:
        print(s)
        return
    if open_count<n:
        parentheses(n,open_count + 1,close_count, s + '(')
    if close_count<open_count:
        parentheses(n,open_count,close_count + 1, s + ')')
n = 3
parentheses(n)
