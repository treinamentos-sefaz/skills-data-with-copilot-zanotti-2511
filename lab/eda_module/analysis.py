"""Módulo 3 — Análise Exploratória de Dados (EDA).

Complete cada função com o apoio do GitHub Copilot. Use ``/explain`` para
entender fórmulas (como o IQR) antes de confiar no código gerado.

Valide com:  ``python lab/check.py --module eda``
"""
from __future__ import annotations

import pandas as pd


def descriptive_stats(df: pd.DataFrame) -> pd.Series:
    """Retorne as estatísticas descritivas da coluna ``rating`` (count, mean,
    std, min, quartis, max). Dica: ``df['rating'].describe()``."""
    return df["rating"].describe()


def detect_outliers_iqr(df: pd.DataFrame, column: str = "rating") -> pd.DataFrame:
    """Retorne as linhas consideradas outliers em ``column`` pelo método IQR
    (valores abaixo de Q1 - 1.5*IQR ou acima de Q3 + 1.5*IQR)."""
    # Prompt sugerido: "Implemente a detecção de outliers da coluna usando IQR (fator 1.5)."
    first_quartile = df[column].quantile(0.25)
    third_quartile = df[column].quantile(0.75)
    iqr = third_quartile - first_quartile
    lower_bound = first_quartile - 1.5 * iqr
    upper_bound = third_quartile + 1.5 * iqr
    return df.loc[(df[column] < lower_bound) | (df[column] > upper_bound)].copy()


def missing_values_report(df: pd.DataFrame) -> pd.Series:
    """Retorne a contagem de valores ausentes por coluna. Dica: ``df.isna().sum()``."""
    return df.isna().sum()


def rating_stats_by_variety(df: pd.DataFrame) -> pd.DataFrame:
    """Agrupe por ``variety`` e retorne count, mean, min e max de ``rating``,
    ordenado pela média decrescente."""
    return (
        df.groupby("variety")["rating"]
        .agg(["count", "mean", "min", "max"])
        .sort_values("mean", ascending=False)
    )
