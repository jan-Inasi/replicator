#!/usr/bin/env lua
SELF_PATH = debug.getinfo(1, "S").source:sub(2)
local f = assert(io.open(SELF_PATH, "r")) SRC = f:read("a"); f:close()
SRC_LINES = {} for line in string.gmatch(SRC, "[^\n]*") do SRC_LINES[#SRC_LINES+1] = line end
local function replicator(end_line) local beg_line = debug.getinfo(1, "l").currentline
    print("replicator run")
    f = assert(io.open(SELF_PATH, "r")) local self_text = f:read("a") f:close()
    local self_lines = {} for line in string.gmatch(self_text, "[^\n]*") do self_lines[#self_lines+1] = line end
    local injection_idx = math.random(5, #self_lines - 1)

    local src_block = table.move(SRC_LINES, beg_line, end_line, 1, {})
    table.move(self_lines, injection_idx, #self_lines, injection_idx + #src_block)
    table.move(src_block, 1, #src_block, injection_idx, self_lines)

    f = assert(io.open(SELF_PATH, "w")) f:write(table.concat(self_lines, "\n")) f:close()
    print("replicator write")
end; replicator(debug.getinfo(1, "l").currentline)
