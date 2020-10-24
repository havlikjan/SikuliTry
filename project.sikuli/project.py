import webbrowser
modes = ("Add subscription", "Download renderer", "Leave mesage")

webbrowser.open("http://www.google.com")


wait ("1603554227762.png")
click (Pattern("1603554227762.png").targetOffset(-59,18))
type("corona renderer"+Key.ENTER)
wait(Pattern("1603555309693.png").targetOffset(-304,-271))
click(Pattern("1603555309693.png").targetOffset(-262,-227))
wait(Pattern("1603555492991.png").targetOffset(512,0))
options = select("Choose one of actions", options = modes)
if options == modes[0]:
    email = input("Type your e-mail please")
    click(Pattern("1603561022182.png").targetOffset(-19,1))
    type(email)
    click(Pattern("1603558647949.png").targetOffset(4,-3))
    wait("1603561249469.png"):
        popup("Your e-mail was succesfully subscribed, please check your inbox")
elif options == modes[1]:
    click(Pattern("1603555492991.png").targetOffset(250,1))
    wait("1603556998267.png")
    click(Pattern("1603556998267.png").targetOffset(-292,15))
    popup("Downloading started succesfully")
elif options == modes[2]:
    name = input("What is your name?")
    email = input("What is your email?")
    message = input("Type your message for Corona team, please.")
    click("1603561627827.png")
    wait("1603561648412.png")
    click(Pattern("1603561648412.png").targetOffset(-20,-115))
    type(name)
    click(Pattern("1603561648412.png").targetOffset(-38,-54))
    type(email)
    click(Pattern("1603561648412.png").targetOffset(-29,29))
    type(message)
    click(Pattern("1603561648412.png").targetOffset(-125,148))
    wait("1603561782759.png")

     