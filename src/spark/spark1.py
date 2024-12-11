import pyspark
from pyspark import SparkContext
sc = SparkContext()
n = sc.parallelize([4,10,9,7])
n.take(3)
