#!/usr/bin/env python3
import inspect, pathlib, sys, random
def replicator2():
    """ replicator """  # son of mine
    indent_len = lambda line: len(line) - len(line.lstrip(" "))
    # find the block of the function definition and its call
    lines = pathlib.Path(__file__).read_text().splitlines()
    this_frame = inspect.currentframe()
    if this_frame is None: print("Unable to read the current frame", file=sys.stderr); return
    this_line_idx: int = this_frame.f_lineno - 1
    this_line_indent: int = indent_len(lines[this_line_idx])
    # ugly iterators as we don't want to pase the function in a loop as the file would grow even faster
    beg_idx = next(i for i in range(this_line_idx - 1, 0, -1) if lines[i] == " " * (this_line_indent - 4) + "def replicator2():")
    end_idx = next(i for i in range(this_line_idx + 1, len(lines)) if lines[i] == " " * (this_line_indent - 4) + "replicator2()")
    block = lines[beg_idx:end_idx+1]
    block = [line[this_line_indent-4:] for line in block]
    consonants, vowels = "rtpsdfghklzcvbnmjwy", "ieaou"
    syllable = lambda: random.choice(list(consonants) + [""]) + random.choice(vowels) + random.choice(["", random.choice(consonants)])
    child_name = "".join(syllable() for _ in range(4))
    my_name_line_idx = next(i for i in range(beg_idx, this_line_idx) if lines[i][this_line_indent:this_line_indent+3] == '"""')
    my_name = lines[my_name_line_idx].split(' """ ')[1]
    parent_name =lines[my_name_line_idx].split(' """  # son of ')[1]
    childs_docstr = f'    """ {child_name} """  # son of {my_name}'
    block[1] = childs_docstr
    print(f"running {my_name} son of {parent_name}")
    # read the source again because it might have been already overwritten by injected replicators
    lines = pathlib.Path(__file__).read_text().splitlines()
    insert_idx = random.randint(2, len(lines) - 1)
    new_indent = indent_len(lines[insert_idx])
    block = [(" " * new_indent) + line for line in block]
    lines = lines[:insert_idx] + block + lines[insert_idx:]
    pathlib.Path(__file__).write_text("\n".join(lines))
    print(f"injected {child_name} son of {my_name}")
replicator2()
