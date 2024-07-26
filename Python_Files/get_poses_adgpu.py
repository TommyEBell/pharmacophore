import sys
import os

dlg_file = (sys.argv[1])


with open(dlg_file, 'r') as f:
  lines = f.readlines()

count = 1
outfile = "pose_" + str (count) + ".pdb"

file = open(outfile, 'w')
for line in lines:
  line_str = line.strip()

  if line_str[0:14] == 'Number of runs':
    n_runs = int(str.split(line_str,':')[1])

  if ((line_str[0:14] == "DOCKED: HETATM" or line_str[0:12] == "DOCKED: ATOM") and (line_str[25:28] == "INH") or (line_str[25:28] == "UNL") or ((line_str[31:34] == "  0"))):
    if (line_str[29:30] == "d"):
      if (line_str[21:22] == "l" or line_str[21:22] == "L") :
        file.write(line_str[8:20] + "Cl" + line_str[22:29] + "    1" + line_str[34:63] + "\n")
      elif (line_str[21:22] == "r" or line_str[21:22] == "R"):
        file.write(line_str[8:20] + "Br" + line_str[22:29] + "    1" + line_str[34:63] + "\n")
      else:
        file.write(line_str[8:29] + "    1" + line_str[34:63] + "\n")
    else:
      if (line_str[21:22] == "l" or line_str[21:22] == "L") :
        file.write(line_str[8:20] + "Cl" +  line_str[22:63] + "\n")
      elif (line_str[21:22] == "r" or line_str[21:22] == "R"):
        file.write(line_str[8:20] + "Br" + line_str[22:29] + "    1" + line_str[34:63] + "\n")
      else:
        file.write(line_str[8:29] + "    1" + line_str[34:63] + "\n")
  if (line_str[0:15] == "DOCKED: TORSDOF"):
    count = count + 1
    file.write("END\n")
    outfile = "pose_" + str (count) + ".pdb"
    file = open(outfile, 'w')
    if count > n_runs:
      os.remove(outfile)
