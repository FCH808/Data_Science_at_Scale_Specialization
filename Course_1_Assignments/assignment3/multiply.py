import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:
    # value:
    matrix_label = record[0]
    val = record[3]

    A_size = [5, 5]
    B_size = [5, 5]

    if matrix_label == 'a':
        i = record[1]
        j = record[2]
        for k in xrange(B_size[1]):
            mr.emit_intermediate((i, k), {'A{}{}'.format(i,j): val})

    else: # matrix_label == 'b'
        j = record[1]
        k = record[2]
        for i in xrange(A_size[0]):
            mr.emit_intermediate((i, k), {'B{}{}'.format(j, k): val})

def reducer(key, list_of_values):
    # key:
    # value:

    print 'Key: ', key
    print 'Values: ', list_of_values

    A = {}
    B = {}

    for d in list_of_values:

        position_tuple = d.keys()[0]
        value = d.values()[0]

        j_index = ''
        if position_tuple[0] == 'A':
            j_index = position_tuple[2]
            A[j_index] = value
        else: # If == 'B'
            j_index = position_tuple[1]
            B[j_index] = value

        total = 0
        for j in A.keys():
            total += A.get(j, 0) * B.get(j, 0)

    mr.emit( (key[0], key[1], total ) )

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
