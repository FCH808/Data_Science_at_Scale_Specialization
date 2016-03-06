import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:
    # value:
    key='1'
    value = record[1][:-10]

    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key:
    # value:

    for value in set(list_of_values):
        mr.emit((value))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
