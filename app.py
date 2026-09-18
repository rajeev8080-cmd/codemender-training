import subprocess

def run_user_cmd(user_input):
    # Example command execution
    subprocess.run(["echo", str(user_input)])

if __name__ == "__main__":
    print("CodeMender Test Application")
