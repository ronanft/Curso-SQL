import marimo

__generated_with = "0.19.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # SQL do Zero ao Avançado com DuckDB

    Nesta aula vamos aprender SQL **do zero**, usando um dataset realista (Superstore),
    e evoluir passo a passo até consultas avançadas usadas no mercado.

    O objetivo não é decorar comandos, mas **aprender a pensar em SQL**:
    - como explorar dados
    - como resumir informações
    - como trabalhar com datas
    - como lidar com dados faltantes
    - como construir consultas legíveis e escaláveis

    Vamos usar o DuckDB porque ele roda localmente, é rápido e tem uma sintaxe moderna,
    muito próxima de bancos usados em produção.
    """)
    return


@app.cell
def _(mo):
    store = mo.sql(
        f"""
        CREATE TABLE superstore AS
        SELECT * 
        FROM READ_CSV_AUTO('https://github.com/ronanft/Curso-SQL/raw/main/superstore.csv');
        """
    )
    return


@app.cell
def _(mo, superstore):
    _df = mo.sql(
        f"""
        FROM superstore LIMIT 10;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 0 — Conhecendo os dados

    Antes de escrever qualquer consulta, precisamos entender:
    - quais colunas existem
    - quais tipos de dados temos
    - o que cada coluna representa

    Esse é um passo crítico em qualquer projeto real de dados. Usaremos DESCRIBE

    ---

    Em seguida vamos (SELECT/LIMIT):
    - visualizar algumas linhas da tabela
    - identificar colunas categóricas, numéricas e temporais
    - entender quais colunas fazem sentido para análise

    Perguntas importantes:
    - Qual coluna representa o tempo?
    - Qual coluna representa valor monetário?
    - Existem identificadores únicos?
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 1 — Selecionando dados

    Nesta etapa, vamos aprender a **filtrar linhas**.

    Filtrar é uma das operações mais importantes em SQL.
    Aqui vamos ver:
    - filtros simples
    - filtros com múltiplas condições
    - operadores lógicos

    Vamos responder perguntas como:
    - pedidos com vendas acima de um valor
    - pedidos lucrativos
    - pedidos de uma categoria específica

    Comandos que usaremos:
    WHERE, operadores: =, >, <, operadores lógicos: AND, OR
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Agora vamos aprender a **ordenar os resultados**.

    Ordenar não muda os dados,
    mas muda como nós **interpretamos** a informação.

    Vamos:
    - ordenar por vendas
    - ordenar por data
    - encontrar os maiores e menores valores

    Comandos que usaremos:
    ORDER BY, ASC, DESC, LIMIT
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 2 — Resumindo dados com agregações

    Em dados reais, raramente analisamos linha por linha.
    Normalmente queremos **resumos**.

    Aqui vamos aprender a:
    - contar registros
    - somar valores
    - calcular médias
    - identificar máximos e mínimos

    Comandos que usaremos:
    COUNT, SUM, AVG, MIN, MAX
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Agora vamos aprender a **agrupar dados**.

    Agrupar significa responder perguntas do tipo:
    - vendas por categoria
    - lucro por região
    - pedidos por segmento

    Toda vez que usamos funções agregadas com colunas categóricas,
    precisamos usar agrupamento.

    Comandos que usaremos:
    GROUP BY, funções agregadas (SUM, AVG, COUNT)
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aqui vamos aprender a **combinar agrupamento com filtros**.

    Importante:
    - `WHERE` filtra linhas ANTES do agrupamento
    - `GROUP BY` cria os grupos
    - funções agregadas resumem os grupos

    Vamos aplicar filtros cumulativos e entender essa ordem de execução.

    Comandos que usaremos:
    WHERE, GROUP BY,  ORDER BY
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 4 — Escrevendo dados no banco (CRUD)

    Até agora só lemos dados.
    Agora vamos aprender a **modificar** o banco.

    Essas operações existem em sistemas reais
    e precisam ser usadas com muito cuidado.

    Comandos que usaremos:
    INSERT INTO, VALUES
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aqui vamos aprender a **atualizar registros**.

    Atenção total ao uso do WHERE.
    Um UPDATE sem filtro pode alterar a tabela inteira.

    Comandos que usaremos:
    UPDATE, SET, WHERE
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Agora vamos aprender a **remover dados**.

    Assim como o UPDATE, DELETE é perigoso
    e sempre deve ser usado com filtros bem definidos.

    Comandos que usaremos:
    DELETE, WHERE
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 5 — Queries dentro de queries

    À medida que os problemas ficam mais complexos,
    uma única query não é suficiente.

    Aqui vamos aprender a usar:
    - subqueries
    - CTEs (Common Table Expressions)

    Isso melhora a legibilidade e organização do código.

    Comandos que usaremos:
    subquery com SELECT,
    WITH ... AS
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vamos usar CTEs para:
    - dividir um problema grande em partes menores
    - reutilizar resultados intermediários
    - deixar o SQL mais próximo de um código legível

    Comandos que usaremos:
    WITH,
    múltiplas CTEs encadeadas
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 6 — Combinando dados

    JOINs permitem combinar informações de fontes diferentes.

    Aqui vamos aprender:
    - por que JOINs existem
    - diferença entre LEFT JOIN e INNER JOIN
    - o impacto de cada tipo no resultado

    Comandos que usaremos:
    LEFT JOIN,
    INNER JOIN,
    ON
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vamos criar uma **tabela calendário** para resolver
    um problema clássico de dados temporais:
    dias sem registro.

    Isso vai nos permitir:
    - identificar datas faltantes
    - manter séries temporais contínuas

    Comandos que usaremos:
    WITH RECURSIVE,
    UNION ALL,
    INTERVAL
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 7 — Lidando com dados ausentes

    Valores nulos são extremamente comuns em dados reais.

    Aqui vamos aprender:
    - o que significa NULL
    - por que NULL não é zero
    - como substituir valores ausentes

    Comandos que usaremos:
    COALESCE
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 8 — Funções de janela (WINDOW FUNCTION)

    Funções de janela permitem cálculos
    que não colapsam linhas como o GROUP BY.

    Elas são fundamentais para:
    - rankings
    - comparações linha a linha
    - análises temporais avançadas

    Comandos que usaremos:
    OVER(),
    ROW_NUMBER,
    RANK
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Agora vamos trabalhar com deslocamento temporal.

    Queremos acessar:
    - o valor anterior
    - o valor seguinte

    Isso nos permite comparar períodos consecutivos (muito usado com preços de ações em bolsa).

    Comandos que usaremos:
    LAG,
    LEAD,
    ORDER BY dentro do OVER()
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nível 9 — Imputação de dados no SQL

    Vamos resolver um problema real:
    dias sem vendas registradas.

    A estratégia será:
    - identificar valores ausentes
    - usar informações dos dias vizinhos
    - preencher os dados de forma inteligente

    Comandos que usaremos:
    LAG,
    LEAD,
    COALESCE,
    ROUND
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aqui vamos juntar tudo que aprendemos:
    - CTEs
    - JOINs
    - funções de janela
    - tratamento de NULLs

    Essa é uma query que você poderia usar
    em um cenário real de analytics.

    Comandos que usaremos:
    múltiplas CTEs,
    LEFT JOIN,
    funções de janela,
    funções numéricas
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusão

    Neste curso percorremos o caminho completo do SQL:
    - leitura de dados
    - filtragem
    - agregação
    - análise temporal
    - escrita no banco
    - SQL analítico avançado

    Se você domina esse fluxo,
    você está pronto para trabalhar com dados no mundo real.
    """)
    return


if __name__ == "__main__":
    app.run()
