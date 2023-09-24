from Lab03 import Stack, StackApp

def useStackApp():
    sa=StackApp()
    expr='dsdk1(jkdfk{pp[ sd]fsd)sddfd'
    expr1='2+(4+3*2+1)/3'
    print("Postfix Expression = ", sa.infix2Postfix(expr1))

    expr2="2432*+1+3/+"
    print("Postfix Evaluation = {:.2f}",format(sa.evalPostfix(expr2)))