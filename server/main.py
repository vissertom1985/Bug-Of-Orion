import time
import sys
from game_controller import GameController

def main():
    print("=================================================")
    print("   Starting BugFX Authoritative Server (Python)  ")
    print("=================================================")

    try:
        # 1. Initialize the Master Controller
        # This automatically creates the SQLite DB, spins up the CommandService,
        # starts the NetworkController, and launches the ConsoleListener.
        control = GameController()

        # 2. Ignite the Core Game Loop
        print("[System] Igniting core game loop...")
        control.run_game()

        print("[System] BugFX Server is online and listening for connections.")
        print("[System] Type 'exit' in the console at any time to safely shut down.")
        print("=================================================")

        # 3. Keep the Main Thread Alive
        # Since the game loop, console listener, and network listener are all 
        # running as background daemon threads, we need to keep this primary 
        # thread awake so the server doesn't instantly close.
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        # Handles the user pressing Ctrl+C in the terminal
        print("\n[System] Caught KeyboardInterrupt. Shutting down gracefully...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[Fatal Error] Server crashed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()