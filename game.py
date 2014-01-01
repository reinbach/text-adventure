#!/usr/bin/env python
import mapping
import text

from time import sleep

END = BAD_END = False
LOCATION = "front_door"


def echo(text):
    for s in text:
        if (s == "|"):
            sleep(0.5)
        else:
            print(s, sep="", end="", flush=True)
        sleep(0.05)
    print("")


def next_step(intro=True):
    """Provide user with intro and possible actions
    wait for users selection
    """
    display_intro()
    display_possible_actions()
    attempt = input("You... ")
    parse_input(attempt)


def display_intro():
    echo("")
    echo(mapping.LOCATION[LOCATION]['intro'])


def display_possible_actions():
    echo("")
    for i, action in enumerate(mapping.LOCATION[LOCATION]['actions']):
        echo("{0}: {1}".format(i + 1, action[0]))


def display_action_taken(action_int):
    echo("")
    echo(mapping.LOCATION[LOCATION]['actions'][action_int][2])


def parse_input(attempt):
    try:
        action_int = int(attempt) - 1
    except ValueError:
        action_int = -1
    if not get_action(action_int):
        echo(text.UNKNOWN_ACTION)


def get_action(action_int):
    global LOCATION
    try:
        possible_actions = mapping.LOCATION[LOCATION]['actions']
        if action_int in range(0, len(possible_actions)):
            display_action_taken(action_int)
            LOCATION = possible_actions[action_int][1]
            if LOCATION == "end":
                terminate()
            return True
    except KeyError:
        terminate("GA-001")
    return False


def terminate(bad=False):
    """Set game to terminate"""
    global END, BAD_END
    END = True
    BAD_END = bad


def main():
    echo(text.INTRO)
    echo(text.FIRST_NOISE)
    while not END:
        next_step()

    if BAD_END:
        echo(text.GAME_ERROR.format(BAD_END))

    echo("")
    echo("The END")


if __name__ == "__main__":
    main()
