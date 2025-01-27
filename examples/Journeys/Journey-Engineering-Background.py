# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.9.16
#   latex_envs:
#     LaTeX_envs_menu_present: true
#     autoclose: false
#     autocomplete: true
#     bibliofile: biblio.bib
#     cite_by: apalike
#     current_citInitial: 1
#     eqLabelWithNumbers: true
#     eqNumInitial: 1
#     hotkeys:
#       equation: Ctrl-E
#       itemize: Ctrl-I
#     labels_anchors: false
#     latex_user_defs: false
#     report_style_numbering: false
#     user_envs_cfg: false
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: false
#   widgets:
#     application/vnd.jupyter.widget-state+json:
#       state: {}
#       version_major: 2
#       version_minor: 0
# ---

# %% [markdown]
# # Journey: Engineering background
#
# This is a second of the possible journeys into HARK - the Python package designed to solve economic models with the heterogeneous agents. As it is a "journey", it is not a one big tutorial, but a set of the links to the notebooks/other resources which will help you understand the different HARK objects and functionalities.
#
# This notebook was designed for users with some skill in programming. It does not require any knowledge of the economic theory - we are going to give you a very basic examples (which cannot substitute the macroeconomic textbooks if you want to learn theory more systematically, here we give you same examples: )
#

# %% [markdown]
# ## Microeconomic agent-type problems
#
# In the economic analysis, one of the most used problems are "consumers problems" which are designed to model the consumer choices. In this class of problems consumers need to find the optimal set of goods given her resources. In the basic formulation of the problem there is only one good but can be consumed in different time periods (let us denote it by $C_t$, where $0\leq t\leq T\leq \infty$ denotes periods). Consumer receives some resources $w_t$ (think wages), which she can invest with interest rate $R$ (denote the investments by $A_t$) or consume. The utility of the consumption in the period $t=0$ is given by function $U()$, for the next periods it is given by the function $\beta^t U ()$ as consumer prefer consumption now then in the future, $\beta<1$. The consumption problem can be then formalize by the maximization problem:
#
# \begin{eqnarray*}
#  \max_{C_t}&  \sum_{t=0}^T \beta^t U(C_t)
# \end{eqnarray*}
#
# With the condition in each t:
# \begin{eqnarray*}
# C_t + A_{t+1} = w_t+RA_t
# \end{eqnarray*}
#
# U is typically assumed to be a constant risk aversion function:
# $$
# U(C)=\frac{C^{1-\rho}}{1-\rho}
# $$
#
# As you see, the following problem enables to analyze the consumer's saving decisions. Obviously, the complexity of the problem depends on the $w_t$, if it is deterministic it is much easier to track down than in case if $w_t$ is given by a stochastic process.
#
# |Number | Tutorial | Description|
# | :---- |  :---- |  :---- |
# |1 |[Gentle_intro_I](https://github.com/econ-ark/DemARK/blob/master/notebooks/Gentle-Intro-To-HARK-PerfForesightCRRA.ipynb) |Here is your first tutorial in HARK, to solve the case when $w_t$ is deterministic|
# |2 |[Gentle_intro_II](https://github.com/econ-ark/DemARK/blob/master/notebooks/Gentle-Intro-To-HARK-Buffer-Stock-Model.ipynb) |The notebook concerning the case when $w_t$ follows the idiosyncratic AR process|
# |3|[Chinese-Growth](https://github.com/econ-ark/DemARK/blob/master/notebooks/Chinese-Growth.ipynb)|The third notebook concern the case when $w_t$|
