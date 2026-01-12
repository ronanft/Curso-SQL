import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    store = mo.sql(
        f"""
        INSTALL spatial; -- extensão que inclui suporte a Excel
        LOAD spatial;

        CREATE TABLE superstore AS
        SELECT * 
        FROM read_excel('https://github.com/ronanft/Curso-SQL/raw/main/Sample%20-%20Superstore.xls');
        """
    )
    return


if __name__ == "__main__":
    app.run()
