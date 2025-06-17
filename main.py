from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Mindbox').getOrCreate()

products = spark.read.option('multiLine', True).json('./json/products.json')
categories = spark.read.option('multiLine', True).json('./json/categories.json')

products_categories = (
    spark.read
    .option('multiLine', True)
    .json('./json/products_categories.json')
)

result = (
    products_categories
    .join(products, products_categories.product_id == products.id, 'inner')
    .join(categories, products_categories.category_id == categories.id, 'left')
    .select(
        products.title.alias('product'),
        categories.title.alias('category')
    )
)

result.show()
