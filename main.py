import os
import time
from datetime import datetime
from datetime import time as dt_time
from typing import Literal, TypedDict, cast

Action = Literal["print", "list_files", "create_file"]


class Task(TypedDict):
    time: dt_time
    action: Action
    args: str
    done: bool


def parse_action(value: str) -> Action | None:
    if value in {"print", "list_files", "create_file"}:
        return cast(Action, value)
    return None


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
                parts = line.split(maxsplit=2)

                time = datetime.strptime(parts[0], "%H:%M:%S").time()
                action = parse_action(parts[1])
                if action is None:
                    print(f"Skipping invalid action: {parts[1]}")
                    continue
                args = parts[2]

                tasks.append(
                    {
                        "time": time,
                        "action": action,
                        "args": args,
                        "done": False,
                    }
                )
    except FileNotFoundError:
        print(f"Schedule file '{filename}' not found.")

    return tasks


def create_file(filename: str) -> None:
    """Create an empty file with the given filename."""
    with open(filename, "w"):
        pass


def list_files(directory: str) -> None:
    """List files in the given directory."""
    files = os.listdir(directory)
    print({", ".join(files)})


def execute_action(action: Action, args: str) -> None:
    """Execute a single action.
    Supported commands: print, list_files, create_file
    """
    # TODO: handle each command using action and args
    match action:
        case "print":
            print(args)
        case "list_files":
            list_files(args)
        case "create_file":
            create_file(args)
        case _:
            print(f"Unknown action: {action}")

    with open("log.txt", "a") as f:
        now = datetime.now().strftime("%H:%M:%S")
        f.write(f"{now} {action} {args}\n")


def run_scheduler() -> None:
    tasks = load_schedule("schedule.txt")
    if not tasks:
        print("No tasks loaded. Exiting.")
        return

    print("Scheduler running... (Ctrl+C to stop)")
    try:
        while True:
            now = datetime.now().time().replace(microsecond=0)
            # TODO: loop through tasks, execute if time matches and not done
            for task in tasks:
                if task["time"] <= now and not task["done"]:
                    # if not task["done"]:
                    print(f"Executing task: {task['action']} {task['args']}")
                    execute_action(task["action"], task["args"])
                    task["done"] = True
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


run_scheduler()
