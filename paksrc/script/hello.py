# rusted-ruins-script

game.talk("hello-start")
while True:
    response = game.talk("hello-next", ["ans-yes", "ans-no"])
    if response == 1:
        break
