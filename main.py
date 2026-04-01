import os
import time
from datetime import datetime
from typing import TypedDict


class Task(TypedDict):
    time: str
    action: str
    args: str
    done: bool


def create_file(filename: str) -> None:
    """Create an empty file with the given filename."""
    with open(filename, "w"):
        pass


def list_files(directory: str) -> None:
    """List files in the given directory."""
    files = os.listdir(directory)
    print(f"Files in '{directory}': {', '.join(files)}")


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
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(" ")
                time = parts[0]
                action = parts[1]
                args = " ".join(parts[2:])
                tasks.append(
                    {"time": time, "action": action, "args": args, "done": False}
                )
    except FileNotFoundError:
        print(f"Schedule file '{filename}' not found.")

    return tasks


def execute_action(action: str, args: str) -> None:
    """Execute a single action.
    Supported commands: print, list_files, create_file
    """
    # TODO: handle each command using action and args
    eval(f"{action}('{args}')")
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
            for task in tasks:
                # if task["time"] == now and not task["done"]:
                if not task["done"]:
                    execute_action(task["action"], task["args"])
                    task["done"] = True
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


run_scheduler()
