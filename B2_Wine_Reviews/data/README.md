# Task B2 Dataset: Wine Reviews (WineEnthusiast)

- **Source:** Kaggle (zynicide/wine-reviews) & HuggingFace (james-burton/wine_reviews)
- **Samples:** ~130k professional wine ratings and descriptions
- **Target:** Points awarded by critic (80 - 100)
- **Access in Python:**
```python
from datasets import load_dataset
ds = load_dataset('james-burton/wine_reviews', split='train')
```
