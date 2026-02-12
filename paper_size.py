# --------------------------------------
# Name: Nicole Ormond
# Date: 02/12/2026
# Chapter 2: Exercise 1, Part A
# --------------------------------------

# display dimensions of a letter-size paper in millimeters
# 25.4 mm per inch

# declare constant variable for mm per inch
MM_PER_INCH = float("25.4")

# declare variable for paper width in inches, not constant because paper size can change
paperWidthInInches = float("8.5")

# declare variable for paper length in inches
paperLengthInInches = float("11.0")

# calculate paper size in mm
paperWidthInMM = paperWidthInInches * MM_PER_INCH
paperLengthInMM = paperLengthInInches * MM_PER_INCH

# print result
print("Letter size paper is", paperWidthInMM, "mm by ", paperLengthInMM, "mm")