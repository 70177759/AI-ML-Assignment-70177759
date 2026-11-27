# Task C3 Dataset: Flickr8k

- **Source:** Kaggle (adityajn105/flickr8k) & HuggingFace (Naveengo/flickr8k)
- **Samples:** 8,091 images with 5 captions each (40,455 captions)
- **Image Split:** 6,000 train / 1,000 validation / 1,091 test
- **Access in Python:**
```python
from datasets import load_dataset
ds = load_dataset('Naveengo/flickr8k', split='train')
```
