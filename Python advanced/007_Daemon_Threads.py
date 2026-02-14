# ========== DAEMON THREAD ==========

# running in the background and the script terminates even,
# they're still running. not vital to the program
# use it for constantly reading in information from a file
# then terminate the script and also terminate a daemon

# Main Thread ends = Daemon Thread die

# imagine you are playing a video game
# Main Story/Game + Environment/Music

import threading
import time

event = threading.Event()  # switch on-off for soundtrack


def background_music():
    while True:
        event.wait()  # not playing until fight the boss
        print("[music] BOSS THEME STARTING....")
        time.sleep(1)


t_music = threading.Thread(target=background_music, daemon=True)
t_music.start()

while True:
    x = input("\nReady to fight the Boss? (y/n): ").lower()

    if x == "y":
        event.set()  # meet boss = music: on

        print("\n--- ENTERING BOSS ROOM ---")
        for i in range(5):
            print(f" Fighting Boss {i + 1}...")
            time.sleep(1)
        print("You are dead!")

        event.clear()  # 2. victory/defeated music: off back to menu
        time.sleep(1)
        print("[ Back to the menu. ]")
        break

    elif x == "n":
        print("Saved and Exit")
        break