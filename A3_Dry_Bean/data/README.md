# Task A3 Dataset: Dry Bean Dataset

- **Source:** UCI Machine Learning Repository (ID 602)
- **Samples:** 13,611 grains across 7 registered varieties
- **Target:** 7 classes (Barbunya, Bombay, Cali, Dermason, Horoz, Seker, Sira)
- **Access in Python:**
```python
from ucimlrepo import fetch_ucirepo
beans = fetch_ucirepo(id=602)
X, y = beans.data.features, beans.data.targets
```
