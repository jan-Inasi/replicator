def replicator():
    """ Adam """ # son of the creator
    import inspect, random, re
    with open(__file__, "r") as file: lines = file.readlines()
    def n_indent(line): return next((n for n, char in enumerate(line) if char != " "), 0)
    middle = inspect.currentframe().f_lineno - 1
    indent = n_indent(lines[middle]) - 4
    def begin_pred(line: str): return indent == n_indent(line) and line.lstrip().rstrip() == "def replicator():"
    def end_pred(line: str): return indent == n_indent(line) and line.lstrip().rstrip() == "replicator()"
    def begend(start):
        begin = next((i for i in range(start, len(lines)) if begin_pred(lines[i])), -1)
        end = next((i for i in range(begin, len(lines)) if end_pred(lines[i])), -1)
        return begin, end
    begin_end = [0, 0]
    def is_inside(begin_end): return begin_end[0] < middle and middle < begin_end[1]
    while not is_inside(begin_end := begend(begin_end[1])):
        if begin_end[0] == -1 or begin_end[1] == -1: return
    begin, end = begin_end
    def non_white(line: str): return len(line.lstrip()) > 0
    def outside(idx: int): return begin < idx and idx > end
    def choice_pred(idx): return non_white(lines[idx]) and outside(idx)
    insert_idx = next((i for i in range(random.randint(0, len(lines)), len(lines)) if choice_pred(i)), len(lines))
    insert_indent = n_indent(lines[insert_idx]) if len(lines) > insert_idx else 0
    diff_indent = insert_indent - indent
    if diff_indent >= 0:
        indentify = lambda line: " " * diff_indent + line if len(line.lstrip()) > 0 else line
    if diff_indent < 0:
        indentify = lambda line: line[-diff_indent:] if len(line.lstrip()) > 0 else line
    lines_to_insert: list[str] = [indentify(line) for line in lines[begin:end+1]]
    idx = next((i for i, line in enumerate(lines_to_insert) if re.match('.*""".*""".*', line)), -1)
    if idx == -1:
        return
    pre, name, _ = lines_to_insert[idx].split('"""')
    child_name = list("ieaounmlpk")
    random.shuffle(child_name)
    child_name = "".join(child_name)
    lines_to_insert[idx] = pre + '""" ' + child_name + ' """' + f" # son of {name[1:-1]}\n"
    new_lines = lines[:insert_idx] + lines_to_insert + lines[insert_idx:]
    print(f"new child of {name[1:-1]} - {child_name}")
    with open(__file__, "w") as file: file.writelines(new_lines)
replicator()
