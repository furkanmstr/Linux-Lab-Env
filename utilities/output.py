import os
import typer
import shutil


passed = 0
failed = 0

def print_header(lab_name):
    print()
    print("=" * 50)
    if lab_name:
        print(f"  {lab_name}")
    print("=" * 50)
    print()

def check_result(description: str, result: bool):
    global passed, failed

    if result:
        icon    = "+"
        label   = "PASS"
        passed += 1
        color   = typer.colors.GREEN
    else:
        icon    = "x"
        label   = "FAIL"
        failed += 1
        color   = typer.colors.RED

    terminal_width = shutil.get_terminal_size().columns
    prefix = f"  [{icon}]  "
    description_width = 2

    formatted_description = f"{description:<{description_width}}"

    typer.echo(
        f"{prefix}{formatted_description}",
        nl=False
    )

    spaces = terminal_width - len(prefix) - len(formatted_description) - len(label) 

    typer.echo(
        " " * max(spaces, 1),
        nl=False
    )

    typer.secho(label, fg=color, bold=True)

    return result

def finish() -> bool:
    total = passed + failed
    score_pct = int((passed / total) * 100) if total > 0 else 0

    print()
    print("-" * 50)
    print("  Result")
    print("-" * 50)
    print(f"  Passed  :  {passed}")
    print(f"  Failed  :  {failed}")
    print(f"  Score   :  {passed}/{total}  ({score_pct}%)")
    print("-" * 50)
    print()

    return failed == 0

