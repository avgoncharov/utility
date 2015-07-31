# Input file consist of lines. Values in every line are separated by whitespace.
# Input file convert to sql-script. Every line of the input file is converted to insert command of output script.
with open('input.txt') as in_f:
    lines = in_f.readlines()

with open('output.sql','w') as out_f:
    for itr in lines:
        buf = itr.split()
        out_f.write("INSERT INTO TableName (ClmnA, ClmnB) VALUES ('{0}', '{1}');\n".format(buf[0], buf[1]))
