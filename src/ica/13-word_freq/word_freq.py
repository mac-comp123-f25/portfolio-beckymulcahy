def compute_frequencies (file) :
    file = open(file, "r")
    contents = file.read()
    print(contents)

compute_frequencies("../TextFiles/alice.txt")