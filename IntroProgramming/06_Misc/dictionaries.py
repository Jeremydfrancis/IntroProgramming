"""
Jeremy Francis
2026_03_23
Dictionaries
"""

human = {}
human["name"] = "Jeremy"
human["job"] = "programming"
human["hobby"] = "gaming"

print(human)


dna = "ATACATGCATACGCGATA"
rna_conv = {"A": "U", "T": "A", "G": "C", "C": "G"}
count_dict = {"A": 0, "G": 0, "C": 0, "T": 0}
rna = ""
for nuc in dna:
    rna += rna_conv[nuc]
    count_dict[nuc] += 1
print(rna)
print(count_dict.get("A"))
