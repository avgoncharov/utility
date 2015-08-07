# Input file consist of lines. Each line consist of id and some value, which are separated by tab (\t).
with open('input.txt') as in_f:
    lines = in_f.readlines()

# Input file convert to sql-script. Every line of the input file is converted to insert command of output script.
with open('output.sql','w') as out_f:
    for itr in lines:
        i = itr.index('\t')
        b1 = itr[:i]
        b2 = itr[i+1:len(itr) - 1]
        out_f.write("INSERT INTO TableName (ClmnA, ClmnB) VALUES ('{0}', '{1}');\n".format(b1, b2))
