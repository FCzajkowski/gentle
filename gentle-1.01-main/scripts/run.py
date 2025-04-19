import basic
import platform
import datetime as dt
import os
import typer

# ANSI escape codes for blue bold text and green bold text
BLUE_BOLD = '\033[1;34m'
GREEN_BOLD = '\033[1;32m'
RESET = '\033[0m'

app = typer.Typer()

@app.command()
def main():
    date_and_hour = dt.datetime.now()
    version_of_platform = platform.system()

    typer.echo(f"{BLUE_BOLD}gentle 0.1 (dev ver){RESET} | {date_and_hour.strftime('%H:%M:%S')} | {version_of_platform}")

    while True:
        text = input(f'{GREEN_BOLD}$ {RESET}')  # Change the prompt to green bold
        result, error = basic.run('<stdin>', text)
        if text == "":
            pass
        else:
            clr_det = text[0:3]
            if clr_det.lower() == "clr":
                os.system("cls")
            elif text.lower() == "exit":
                raise typer.Exit()
            else:
                if error:
                    print(error.as_string())
                else:
                    print(f"{GREEN_BOLD} {result} {RESET}")

app()
