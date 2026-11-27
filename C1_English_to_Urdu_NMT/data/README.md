# Task C1 Dataset: OPUS-100 English-Urdu

- **Source:** HuggingFace `Helsinki-NLP/opus-100`, config `en-ur`
- **Pairs:** ~750k train, 2,000 validation, 2,000 test
- **Target:** Urdu translation
- **Access in Python:**
```python
from datasets import load_dataset
ds = load_dataset('Helsinki-NLP/opus-100', 'en-ur')
```
