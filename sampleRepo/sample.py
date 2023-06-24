from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

def sum(a,b):
    return a+b
n1,n2=map(int(),input().split())
print(sum(n1,n2))
