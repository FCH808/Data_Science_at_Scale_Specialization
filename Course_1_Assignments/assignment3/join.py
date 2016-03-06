import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record

    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key:
    # value:
    first_order_id =  list_of_values.pop(0)

    for v in list_of_values:
        mr.emit(first_order_id + v)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
