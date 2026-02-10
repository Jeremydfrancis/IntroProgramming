"""
Jeremy Francis
2026_02_10_extracredit
Creating Half Pyramid
"""
rows = int(input("\nHow many rows for the triangle? "))
for i in range (1, rows + 1):
      for j in range(1, i + 1):
            print("#", end=" ")
      print()