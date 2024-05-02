# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/utils.ipynb.

# %% auto 0
__all__ = []

# %% ../nbs/utils.ipynb 3
def colab_badge(path: str):
    from IPython.display import Markdown

    base_url = "https://colab.research.google.com/github"
    badge_svg = "https://colab.research.google.com/assets/colab-badge.svg"
    nb_url = f"{base_url}/Nixtla/nixtla/blob/main/nbs/{path}.ipynb"
    badge_md = f"""<img src="{badge_svg}" ref="{nb_url}" alt="Open this notebook in Google Colab" style="display:block;float:left">"""
    display(Markdown(badge_md))
