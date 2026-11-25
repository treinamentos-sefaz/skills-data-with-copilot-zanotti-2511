"""Módulo 2 — Manipulação de DataFrames com pandas.

Complete cada função com o apoio do GitHub Copilot. Prefira operações
vetorizadas e evite alterar o DataFrame original (use ``.copy()``).

Valide com:  ``python lab/check.py --module pandas``
"""
from __future__ import annotations

import pandas as pd


def load_wines(path: str) -> pd.DataFrame:
    """Leia o CSV em ``path`` e retorne um DataFrame do pandas."""
    # Prompt sugerido: "Leia o arquivo CSV em path com pandas e retorne o DataFrame."
    return pd.read_csv(path)


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Converta a coluna ``rating`` para numérico e remova as linhas cujo
    ``rating`` seja nulo. Retorne o DataFrame limpo."""
    result = df.copy()
    result["rating"] = pd.to_numeric(result["rating"], errors="coerce")
    return result.dropna(subset=["rating"])


def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Retorne as ``n`` variedades com maior média de ``rating`` (colunas:
    variety, avg_rating), ordenadas da maior para a menor."""
    return (
        df.groupby("variety", as_index=False)["rating"]
        .mean()
        .rename(columns={"rating": "avg_rating"})
        .sort_values("avg_rating", ascending=False)
        .head(n)
    )


def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``rating_category`` com as faixas: "Baixa" (< 85),
    "Média" (85 a 90) e "Alta" (> 90). Dica: use ``pd.cut``."""
    result = df.copy()
    ratings = pd.to_numeric(result["rating"], errors="coerce")
    result["rating_category"] = pd.cut(
        ratings,
        bins=[float("-inf"), 85, 90, float("inf")],
        labels=["Baixa", "Média", "Alta"],
    )
    result.loc[ratings == 85, "rating_category"] = "Média"
    return result


def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``country`` extraindo o último trecho após a vírgula de
    ``region`` (ex.: "Mendocino, California" -> "California")."""
    result = df.copy()
    result["country"] = result["region"].str.split(",").str[-1].str.strip()
    return result
