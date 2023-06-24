from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
data=[("aaa",23),("bbb",34)]
schema=StructType([StructField("name",StringType(),True),
                   StructField("age",IntegerType(),True)])
df=spark.createDataFrame(data=data,schema=schema)
df.show()
def sum(a,b):
    return a+b
n1,n2=map(int(),input().split())
result=sum(n1,n2)
print(result)
