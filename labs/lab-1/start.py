from pathlib import Path

LAB_ROOT    = Path("/tmp/linux-lab")

if not LAB_ROOT.exists():
    LAB_ROOT.mkdir()

print("Lab 1 is ready.")
print()
print("Task:")
print("Create the following:")
print("  /tmp/linux-lab/project/")
print("  /tmp/linux-lab/project/hello.txt")


