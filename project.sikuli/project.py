import webbrowser
modes = ("Add subscription", "Download renderer", "Leave mesage")
webbrowser.open("http://www.google.com")
#of course, I can go directly to corona, I like to click few more times in google
wait ("1603554227762.png")
click (Pattern("1603554227762.png").targetOffset(-59,18))
type("corona renderer"+Key.ENTER)
wait(Pattern("1603555309693.png").targetOffset(-304,-271))
click(Pattern("1603555309693.png").targetOffset(-262,-227))
wait(Pattern("1603555492991.png").targetOffset(512,0))
options = select("Choose one of actions", options = modes)
if options == modes[0]:
    email = input("Type your e-mail please")
    type(Key.PAGE_DOWN)
    click(Pattern("1603651128477.png").targetOffset(-32,37))
    type(email)
    click(Pattern("1603651128477.png").targetOffset(186,27))
    if exists("1603651690362.png",10): 
        popup("Your e-mail was succesfully subscribed, please check your inbox")
    else:
        popup("Something is wrong and your e-mail was not subscribed")
elif options == modes[1]:
    click(Pattern("1603555492991.png").targetOffset(250,1))
    type(Key.PAGE_DOWN)
    wait("1603650786641.png")
    click(Pattern("1603650786641.png").targetOffset(-30,67))
    popup("Check if corona is in your downloads.")
elif options == modes[2]:
    name = input("What is your name?")
    email = input("What is your email?")
    message = input("Type your message for Corona team, please.")
    click(Pattern("1603651342167.png").targetOffset(41,441))
    wait("1603561648412.png")
    click(Pattern("1603561648412.png").targetOffset(-20,-115))
    type(name)
    click(Pattern("1603561648412.png").targetOffset(-38,-54))
    type(email)
    click(Pattern("1603561648412.png").targetOffset(-29,29))
    type(message)
    click(Pattern("1603561648412.png").targetOffset(-125,148))
    wait("1603561782759.png")
    click(Pattern("1603561648412.png").targetOffset(16,218))
    if exists("1603652234447.png",10):
        popup("Your message was succesfuly send")
    else:
        popup("Something is wrong and your message was not send")

     