#!/usr/bin/env python3
import inspect, pathlib, sys, random
def replicator2():
    def indent_len(line: str) -> int:
        return len(line) - len(line.lstrip(" "))
    # find the block of the function definition and its call
    lines = pathlib.Path(__file__).read_text().splitlines()
    this_frame = inspect.currentframe()
    if this_frame is None:
        print("Unable to read the current frame", file=sys.stderr)
        return
    this_line_idx: int = this_frame.f_lineno - 1
    this_line_indent: int = indent_len(lines[this_line_idx])
    # ugly iterators as we don't want to pase the function in a loop as the file would grow even faster
    beg_idx = next(i for i in range(this_line_idx - 1, 0, -1) if lines[i] == " " * (this_line_indent - 4) + "def replicator2():")
    end_idx = next(i for i in range(this_line_idx + 1, len(lines)) if lines[i] == " " * (this_line_indent - 4) + "replicator2()")
    block = lines[beg_idx:end_idx+1]
    lines = pathlib.Path(__file__).read_text().splitlines()
    insert_idx = random.randint(1, len(lines) - 1)
    insert_line = lines[insert_idx]
    indent_diff = indent_len(lines[insert_idx]) - this_line_indent - 4
    if indent_diff < 0:
        block = [" " * (-indent_diff) + row for row in block]
    elif indent_diff > 0:
        block = [row.lstrip(" " * indent_diff) for row in block]
    lines = lines[:insert_idx + 1] + block + lines[insert_idx + 1:]
    print("\n".join(lines))
    print(indent_diff, insert_idx)
    print(insert_line)
replicator2()
