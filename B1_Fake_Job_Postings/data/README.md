# Task B1 Dataset: Real or Fake Job Postings (EMSCAD)

- **Source:** Kaggle (shivamb/real-or-fake-fake-jobposting-prediction) & HuggingFace (victor/real-or-fake-fake-jobposting-prediction)
- **Samples:** 17,880 postings (866 fraudulent)
- **Modalities:** Free text (title, profile, description, requirements) + Tabular metadata
- **Access in Python:**
```python
from datasets import load_dataset
ds = load_dataset('victor/real-or-fake-fake-jobposting-prediction', split='train')
```
