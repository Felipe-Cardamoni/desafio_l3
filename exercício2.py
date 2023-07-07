from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, expr

# Cria uma sessão Spark
spark = SparkSession.builder.getOrCreate()

# Define a lista de transações
transacoes = [
    {'transacao_id': 1, 'total_bruto': 3000, 'desconto_percentual': 6.99},
    {'transacao_id': 2, 'total_bruto': 57989, 'desconto_percentual': 1.45},
    {'transacao_id': 4, 'total_bruto': 1, 'desconto_percentual': None},
    {'transacao_id': 5, 'total_bruto': 34, 'desconto_percentual': 0.0}
]

# Cria um dataframe do Spark a partir da lista de transações
df = spark.createDataFrame(transacoes)

# Calcula o total líquido da empresa
total_liquido = df.select(
    round((col('total_bruto') - expr('IFNULL(desconto_percentual, 0) * total_bruto / 100')), 2).alias('total_liquido')
).agg({'total_liquido': 'sum'}).collect()[0][0]

# Formata o total líquido com duas casas decimais
total_liquido_formatado = '{:.2f}'.format(total_liquido)

# Exibe o total líquido da empresa
print("Total líquido da empresa:", total_liquido_formatado)
