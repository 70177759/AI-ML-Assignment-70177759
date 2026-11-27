# Task B3 Dataset: Women's E-Commerce Clothing Reviews

- **Source:** Kaggle (nicapotato/womens-ecommerce-clothing-reviews) & HuggingFace (saattrupdan/womens-clothing-ecommerce-reviews)
- **Samples:** 23,486 consumer reviews
- **Target:** Star rating (1 - 5)
- **Leakage Prevention:** `recommended_ind` is strictly omitted from features.
- **Access in Python:**
```python
from datasets import load_dataset
ds = load_dataset('saattrupdan/womens-clothing-ecommerce-reviews', split='train')
```
