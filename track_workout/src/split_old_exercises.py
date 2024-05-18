import re

def split_ex(name, rep):
    """
    name (str): name of the exercise
    rep (str): number of repetitions
    example input: split_ex(spaudimas, "27.5*3, 30*3, 32.5*1+30*2")
    """
    
    # === split repetitions, separated by comma

rep = "27.5*3, 30*3, 32.5*1+30*2"
rep_empty = rep.replace(" ", "")
p = re.compile('[,]+')

# === split exercise separated by comma
iterator = p.finditer(rep_empty)

for j in iterator:
    string_place = j.start()
    print(string_place)

print(f"string: {rep_empty}")
print(rep_empty[0:6])
print(rep_empty[7:11])
print(rep_empty[12:len(rep_empty)])