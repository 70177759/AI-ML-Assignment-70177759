# Task A1 Dataset: Breast Cancer Wisconsin (Diagnostic)

- **Source:** UCI Machine Learning Repository (ID 17) & `sklearn.datasets.load_breast_cancer`
- **Samples:** 569 instances (357 benign, 212 malignant)
- **Features:** 30 continuous real-valued features computed from fine needle aspirate (FNA) cell nuclei images.
- **Acquisition in Python:**
```python
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X, y = data.data, data.target
```
