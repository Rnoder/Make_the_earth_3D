import os
os.chdir(rf'C:\Users\endeavor1\Desktop\earth\30m')

in_file_name = "30m.txt"
out_file_name_template = "splitted_%d.txt"

max_lines = 11664000

split_index = 1
line_index = 1
out_file = open(out_file_name_template % (split_index,), "w")
in_file = open(in_file_name)
line = in_file.readline()
while line:
    if line_index > max_lines:
        print("Starting file: %d" % split_index)
        out_file.close()
        split_index = split_index + 1
        line_index = 1
        out_file = open(out_file_name_template % (split_index,), "w")
    out_file.write(line)
    line_index = line_index + 1
    line = in_file.readline()

out_file.close()
in_file.close()



####
