# The script of the game goes in this file.
__author__="Nathan D'Agostino"
# Creator: Nathan D'Agostino
# This program is a game in a similar format to Oregon Trail, where you have to manage a certain about of money while trying
# to keep your mentality in check and make it through the 20 day trip.
# Citation: Most of the code was written in Renpy, rather than Pycharm or Visual Studio, this was reccommended by Prof. Vanselow.

define e = Character("???")
define y = Character("[z]")
define ke = Character("Mom")
define dad = Character("Dad")
define money = 1000
define sanity = 100
define guilt = 0
default Phone = True
def time_skip(elapse):
    """Fuction works as a time lapse whenever the user choses an option for how much time they wish to wait."""
    print(elapse + " Hours have passed.")
#This is placed in to be used for time skips and showing how much time as passed.

# The game starts here.
label start:
    "Welcome! To Sprint into the Beyond! This game is essentially Oregon Trail really watered down, there are a few mechanics that are still to be added, but will be later on! Enjoy!"
#For Renpy, this is how a print statement is utilized, so instead of print() it is just either the
#defined character followed by their choice of speech or just using "" to make a generic print statement.
    $ z = renpy.input("What is your name?")
#This is how input is used, instead of the standard input() command.
    $ z = z.strip()
    #This is to ensure no extra spaces and such in the character name!

    e "Hey! I know you can hear me! Well.... Listen, your family isn't in a great spot right now and whatever you have saved up is all you've got for the 20 day trip."

    y "Huh? What? I don't understand! Who are you? How do you know me?"
    #This is the main style of dialouge and whenever possible there will be player input options.

    e "You will understand later I promise!"

    "Later that night."

    y "Who the heck was that? Whatever, just in case lets see what we have."

    "Balance: [money] dollars"

    y "Wow....  I thought I saved more... Oh well, nothing I can do about it now."

    "You ponder for a bit and hear your phone vibrate with a notification."
    define notif = "Beep " * 3

    "[notif] WARNING: Payment due for: Netlfix Verizon Wireless."

    y "Shoot! I forgot to pay for my phone bill and my netflix subscription, if I don't do it I won't have anything to do in the car, but if I do, then I will be in even more trouble if that wierd voice is right."

    menu:
        #This is the menu styling, this is how the game can register player choices then choose the outcomes.
        "Pay for the phone bill and Netflix subscription":
            jump paid

        "Ignore the payment and lose the Phone and Netflix subscription":
            jump unpaid

    label paid:
        $ money = 1000
        $ money -= 35
#This is how the addition and subtraction is used instead of standard + and -.
        "Remaining: %(money)d"
        y "Damn that kinda hurts."
        jump damn
    label unpaid:
        $ sanity = 100
        $ sanity -= 5
#Using subtraction to remove variables
        "Sanity left: %(sanity)d"
        y "Well, there is no point to carrying this around."
        $ Phone = False
        "You lost Item: Phone"
        jump yikes
    label damn:
        y "Well no point worrying over it, atleast I can call, text, and watch videos so I don't lose my mind."
    label yikes:
        y "Well no point worrying over it, hopefully this won't come back to bite me."

    y "Alright let's get to bed"

    "Next day....."

    "[notif]"

    "You look at your calendar on the wall"
    define days_rem = 20
    "Days remaining of trip: [days_rem]."
    y "Damn, was my decision worth it?"
    #These lines are mainly apparent to show how much time the player has to survive.
    menu:
        "Sit and ponder about it":
            jump sad

        "Move onwards":
            jump ignore
        "Scrounge around room" if sanity == 100:
            jump scavenge

    label sad:
        $ sanity -= 10
        "Sanity left: %(sanity)d"
        y "Damn I just feel sad now."
        jump leavin_time
    label ignore:
        $ sanity += 5
        "Sanity left: %(sanity)d"
        y "Meh, I wonder how the trip will go."
        jump leavin_time
    label scavenge:
        "Found: Nothing"
        y "Wow, nothing useful...."
        jump leavin_time
    label leavin_time:
        ke "[y]!!!! TIME TO GO!"
    y "Dang, this is gonna either be real fun or real boring."

    "Some time passes"

    dad "Alright kiddo, we are making a stop. Want to grab anything?"

    menu:
        "Go inside":
            y "Yeah, I'll go take a look."
            jump enter

        "Refuse":
            y "Nah."
            jump stay

    label enter:
        "You enter the store."
        "[notif]"
        "You see that it is a normal Gas Station store."
        y "Well, I got some time, lets look around!"
define count = 10
while count >= 1:
# This is a loop example for when the player is within a store or interacting with others.
    menu:
        "Look at drinks":
            "You see many drinks."
            $ count -= 2
#This is to edit the loop to know when to close the loop.
            "Time left: %(count)d"
            jump drink_opt
        "Leave.":
            "You leave"
            $ count -= 10
            jump stay
    label drink_opt:
        "There lotsa drinks."
        y "I don't think I need to buy anything."
        $ count -= 8
        "Time left: %(count)d"
        jump stay

    label stay:
        "Time passes and your Dad is ready to go again!"
        $ count -= 10
    dad "ALRIGHT! Let's continue onwards!"
    "Your dad starts to drive again."

    "Time passes and you see nothing but trees and empty land."

    "More time passes"

    y "God I am really fugkin bored."

    dad "[y]!! Language"

    y "Yeah yeah, sorry."

    menu:
        "Check phone" if Phone == True:
            "You look at your phone"
            jump not_bored
        "Look out window":
            "You look out the window"
            jump not_too_bored
        "Be bored":
            "You feel dead inside"
            jump bored_af
    label not_bored:
        $ sanity += 10
        "Sanity left: %(sanity)d"
        jump onwards
    label not_too_bored:
        "Sanity left: %(sanity)d"
        jump onwards
    label bored_af:
        $ sanity -= 25
        "Sanity left: %(sanity)d"
        jump onwards
    label onwards:
        "Well, onwards I guess."
    if sanity != 100:
        ke "You look half-alive."
    y "Thanks mom."
    $ sanity -= 5
    "Sanity left: %(sanity)d"
    if money >= 900 or sanity >= 90:
        "You are somehow ok, in a way...."
        e "Hey! Heads up, you might want to let your family know that something is about to happen."
        y "???"
    #This menu choice list is a lot longer as the story is getting more dependent on previous user choices.
    #This can lead into different paths and such, but mainly is meant to lead into different menu choices.
    menu:
        "Warn your parents that something bad is about to happen.":
            y "Hey Dad, Mom?"
            ke "Yes?"
            dad "What's up champ?"
            y "Now I might sound crazy, but you might want to keep an eye out."
            ke and dad "What? Uhhhh alright...."
            "You feel slightly off, as if your mental capabilities are leaving you."
            $ sanity -= 10
            jump told_family
        "Stay quiet":
            "You feel this guilt growing on you."
            $ guilt += 10
            "Guilt: %(guilt)d"
            jump told_family
    label told_family:
        "As time went on, you just say trees and the road, with the occasional passing car."
        time_skip("4")


    #The menu is a perameter passing allowing the user to pick and choose their fate.
    "This is all for now, as the maker of the game, I would like to actually make a story of this and have some real visuals, until next time!"

    #Currently in notes as the Defined Function is not needed yet, but will be implemented later on.
    # This is a start to a define function to use for transitions.
    # This ends the game.

    return
