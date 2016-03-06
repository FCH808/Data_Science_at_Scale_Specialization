import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:
    # value:
    key = record[0]
    value = record[1]

    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key:
    # value:

    for value in set(list_of_values):
        if list_of_values.count(value) == 1:
            mr.emit((key, value ))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
