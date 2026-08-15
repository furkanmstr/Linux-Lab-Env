from utilities.checks import check_directory, check_file
from utilities.output import print_header, finish


print_header("Lab 1 — Filesystem Basics")

check_directory("/tmp/linux-lab/project")
check_file("/tmp/linux-lab/project/hello.txt")

finish()

