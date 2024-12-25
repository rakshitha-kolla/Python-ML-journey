def gen_parenthesis(n,open,close,s,ans):
    if open==n and close==n:
        ans.append(s)
        return
    if open<n:
        gen_parenthesis(n,open+1,close,s+"{",ans)
    if close<open:
        gen_parenthesis(n,open,close+1,s+"}",ans)
def allParenthesis(n):
    ans=[]
    if n>0:
        gen_parenthesis(n,0,0,"",ans)
    return ans
n=int(input("Enter n: "))
par=allParenthesis(n)
for s in par:
    print(s)