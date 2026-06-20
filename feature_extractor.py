from urllib.parse import urlparse
import re

def extract_features(url):
    features = []

    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(sum(c.isdigit() for c in url))
    features.append(1 if url.startswith("https") else 0)

    return features