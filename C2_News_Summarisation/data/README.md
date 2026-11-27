# Task C2 Dataset: BBC Extreme Summarisation (XSum)

- **Source:** HuggingFace `EdinburghNLP/xsum`
- **Samples:** 226,711 BBC news articles with single-sentence summaries
- **Target:** One-sentence abstractive summary
- **Access in Python:**
```python
from datasets import load_dataset
ds = load_dataset('EdinburghNLP/xsum')
```
