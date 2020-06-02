"""
The :mod:`rl_agents.agents.policies` submodule includes:

* Epsilon Greedy
* Softmax (a.k.a Boltzman Policy)
"""
from rl_agents.agents.policies.tabular_policies import (
    BoltzmanPolicy,
    EDecreasePolicy,
    EGreedyPolicy,
)
