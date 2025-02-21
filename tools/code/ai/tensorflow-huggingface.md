# Fine-Tuning Pipeline for Diagnosing Foot Injury using TensorFlow
## Model Overview

In this pipeline, we will use the Hugging Face model `microsoft/mri-autoencoder-v0.1` for diagnosing injuries from X-rays and MRIs. This model is a pre-trained autoencoder specifically designed for MRI images.

## Step 1: Install Hugging Face Transformers

Before proceeding, ensure you have the Hugging Face Transformers library installed:

```bash
pip install transformers
```

## Step 2: Import Libraries

```python
import tensorflow as tf
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## Step 3: Load Pre-trained Model and Fine-Tune

```python
# Load the Hugging Face model and feature extractor
model_name = "microsoft/mri-autoencoder-v0.1"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Freeze the base model
for layer in model.base_model.layers:
    layer.trainable = False

# Add custom layers on top of the base model
x = model.base_model.output
x = Flatten()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(1, activation='sigmoid')(x)

# Create the final model
model = Model(inputs=model.base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```



