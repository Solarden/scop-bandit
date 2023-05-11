import subprocess  # nosec


def run_command(command):
    subprocess.call(command, shell=False)  # nosec


if __name__ == "__main__":
    user_input = input("Enter your name: ")
    command = ["echo", f"Hello, {user_input}!"]
    run_command(command)
