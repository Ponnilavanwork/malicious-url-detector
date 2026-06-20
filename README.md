# Malicious URL Detection using Machine Learning

## Overview

This project detects whether a URL is safe or malicious using Machine Learning.

## Features

- URL length analysis
- Dot count analysis
- Hyphen count analysis
- Digit count analysis
- HTTPS detection
- Random Forest Classifier

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- Machine Learning

## Project Structure

```text
malicious-url-detector/
│
├── data/
│   └── urls.csv
│
├── feature_extractor.py
├── train_model.py
├── predict.py
├── model.pkl
```

## Installation

```bash
pip install -r requirements.txt
```

## Training

```bash
python train_model.py
```

## Prediction

```bash
python predict.py
```

## Sample Output

```text
Enter URL:
https://google.com

Safe URL
```