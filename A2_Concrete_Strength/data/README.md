# Task A2 Dataset: Concrete Compressive Strength

- **Source:** UCI Machine Learning Repository (ID 165)
- **Samples:** 1,030 instances of laboratory concrete mixes
- **Target:** Compressive strength in MPa (2.33 - 82.60)
- **Access in Python:**
```python
from ucimlrepo import fetch_ucirepo
concrete = fetch_ucirepo(id=165)
X, y = concrete.data.features, concrete.data.targets
```
