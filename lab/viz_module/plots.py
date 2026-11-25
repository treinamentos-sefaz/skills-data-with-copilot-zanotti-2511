"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    # Prompt sugerido: "Crie um histograma da coluna rating com 20 bins, título e
    #  labels em português, e salve a figura em out_path."
    fig, ax = plt.subplots(figsize=(8, 5))
    try:
        ax.hist(df["rating"].dropna(), bins=20, color="steelblue", edgecolor="white")
        ax.set(title="Distribuição das avaliações", xlabel="Avaliação", ylabel="Quantidade de vinhos")
        fig.tight_layout()
        fig.savefig(out_path, format="png", dpi=150)
    finally:
        plt.close(fig)
    return fig


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    counts = df["variety"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(9, 6))
    try:
        ax.barh(counts.index, counts.values, color="steelblue")
        ax.invert_yaxis()
        ax.set(title="Variedades mais frequentes", xlabel="Quantidade de vinhos", ylabel="Variedade")
        fig.tight_layout()
        fig.savefig(out_path, format="png", dpi=150)
    finally:
        plt.close(fig)
    return fig


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top_varieties = df["variety"].value_counts().head(5).index
    filtered = df.loc[df["variety"].isin(top_varieties)].copy()
    fig, ax = plt.subplots(figsize=(10, 6))
    try:
        sns.boxplot(data=filtered, x="variety", y="rating", order=top_varieties, color="steelblue", ax=ax)
        ax.set(title="Avaliações por variedade", xlabel="Variedade", ylabel="Avaliação")
        ax.tick_params(axis="x", labelrotation=20)
        fig.tight_layout()
        fig.savefig(out_path, format="png", dpi=150)
    finally:
        plt.close(fig)
    return fig
