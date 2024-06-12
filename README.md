# NSFW Classifier

[NSFW Classifier Streamlit App](https://nsfw-classifier.streamlit.app/)

This repository contains a NSFW (Not Safe For Work) image classifier which categorizes images into three classes: `Violent`, `Adult`,`and `Safe`. The classifier is built using a ResNet50 model with transfer learning and additional layers for enhanced performance. The model achieves an accuracy of around 91% on a test set of 1400 images.

## Table of Contents
- [Project Overview](#project-overview)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Streamlit Application](#streamlit-application)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The NSFW Classifier is designed to automatically detect and categorize images as Violent, Adult, or Safe. This tool can be used to filter out inappropriate content in various applications.

## Model Architecture

The model is built using the ResNet50 architecture with transfer learning. Additional layers have been added to fine-tune the model for the specific task of NSFW classification. 

- **Base Model:** ResNet50
- **Additional Layers:** Fully Connected Layers,Sigmoid for classification

## Dataset

- **Total Images:** 7000
  - **Training Set:** 4200 images
  - **Validation Set:** 1400 images
  - **Test Set:** 1400 images
- **Classes:**
  - Violent
  - Adult
  - Safe

## Installation

To run the project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Adiiii02/NSFW-Classifier.git
    cd main.py
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To classify images using the NSFW Classifier, you can run the provided script:

```sh
python classify.py --image_path path_to_your_image.jpg
```

This will output the classification result for the provided image.

## Streamlit Application

A Streamlit application is provided for easy interaction with the classifier. To run the Streamlit app, use the following command:

```sh
streamlit run main.py
```

This will launch a local web server where you can upload images and get classification results in real-time.

You can also access the deployed Streamlit application here: [NSFW Classifier Streamlit App](https://nsfw-classifier.streamlit.app/)

## Results

The model achieves an accuracy of around 91% on the test set of 1400 images. Detailed performance metrics and visualizations can be found.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
