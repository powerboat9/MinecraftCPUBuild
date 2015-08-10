#$_Input-1$>and($_Input-2$)>not>$fun$>$__Output-1$

def condence(text):
    text.replace("not>not>", "")

def compileToBasic(text):
    text.replace("increment", "add(#1#)")
    text.replace("decrement", "sub(#1#)")
    text.replace("sub(", "add(-")
    
    text.replace("delay(#", "setdelay(#")
    text.replace("tick(#1#)>tick(#1#)", "tick(#2#)")
