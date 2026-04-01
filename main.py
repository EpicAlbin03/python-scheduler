import time
from datetime import datetime
from typing import TypedDict


class Task(TypedDict):
    time: str
    action: str
    args: str
    done: bool


def load_schedule(filename: str) -> list[Task]:
    """Read schedule.txt and return a list of tasks.
    Each line format: HH:MM:SS command argument
    Returns a list of dicts: {"time": "09:00:05", "action": "print", "args": "Hello!", "done": False}
    """
    tasks: list[Task] = []
    # TODO: open the file, skip blank lines
    # split each line into 3 parts: time, action, args
    # append a dict with "time", "action", "args", "done" to tasks
    # handle missing file gracefully
    try:
        with open(filename) as f:
            for index, line in enumerate(f):
                line = line.strip()
                parts = line.split(" ")
                time = parts[0]
                action = parts[1]
                args = " ".join(parts[2:])
                isLastLine = index == (len(f.readlines()) - 1)
                tasks.append(
                    {"time": time, "action": action, "args": args, "done": isLastLine}
                )
    except FileNotFoundError:
        print(f"Schedule file '{filename}' not found.")

    return tasks


def execute_action(action: str, args: str) -> None:
    """Execute a single action.
    Supported commands: print, list_files, create_file
    """
    # TODO: handle each command using action and args
    pass


def run_scheduler() -> None:
    tasks = load_schedule("schedule.txt")
    if not tasks:
        print("No tasks loaded. Exiting.")
        return

    print("Scheduler running... (Ctrl+C to stop)")
    try:
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            # TODO: loop through tasks, execute if time matches and not done
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


run_scheduler()
