import sys
import os

dlg_file = (sys.argv[1])


with open(dlg_file, 'r') as f:
  lines = f.readlines()

for line in lines:
  line_str = line.strip()

  if line_str[0:5] == 'MODEL':
    n_run = int(str.split(line_str,' ')[1])
    outfile = "pose_" + str (n_run) + ".pdb"
    file = open(outfile, 'w')

  if ((line_str[0:6] == "HETATM" or line_str[0:4] == "ATOM") and (line_str[17:20] == "INH") or (line_str[17:20] == "UNL") or ((line_str[31:34] == "  0"))):
    if (line_str[21:22] == "d"):
      if (line_str[13:14] == "l" or line_str[13:14] == "L") :
        file.write(line_str[0:12] + "Cl" + line_str[14:21] + "    1" + line_str[26:55] + "\n")
      elif (line_str[13:14] == "r" or line_str[13:14] == "R"):
        file.write(line_str[0:12] + "Br" + line_str[14:21] + "    1" + line_str[26:55] + "\n")
      else:
        file.write(line_str[0:21] + "    1" + line_str[26:55] + "\n")
    else:
      if (line_str[13:14] == "l" or line_str[13:14] == "L") :
        file.write(line_str[0:12] + "Cl" +  line_str[14:55] + "\n")
      elif (line_str[13:14] == "r" or line_str[13:14] == "R"):
        file.write(line_str[0:12] + "Br" + line_str[14:21] + "    1" + line_str[26:55] + "\n")
      else:
        file.write(line_str[0:21] + "    1" + line_str[26:55] + "\n")
  if (line_str[0:7] == "TORSDOF"):
    file.write("END")
