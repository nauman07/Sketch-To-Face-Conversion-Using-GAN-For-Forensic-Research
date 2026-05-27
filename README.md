# 🎨 Sketch-to-Face Conversion Using GAN for Forensic Research

A **Generative Adversarial Network (GAN)** based system that converts forensic facial sketches into realistic face images, designed to assist law enforcement and forensic investigations.

---

## 📖 About

In forensic investigations, eyewitness sketches are a common tool for identifying suspects. However, interpreting hand-drawn sketches can be challenging. This project uses a GAN to synthesize photorealistic face images from forensic sketches, bridging the gap between sketch-based identification and facial recognition systems.

This work has been published — please cite the paper if you use this code.

---

## 📂 Repository Structure

```
Sketch-To-Face-Conversion-Using-GAN-For-Forensic-Research/
├── GAN.py                  # GAN model (Generator + Discriminator)
├── DatasetCreator.py       # Script to prepare sketch-face paired dataset
├── predictor.py            # Run inference on new sketches
├── model.png               # GAN architecture diagram
├── Figure_1.png ...        # Sample outputs
└── README.md
```

---

## ✨ Features

- End-to-end sketch-to-face image synthesis using GAN
- Custom dataset creation pipeline
- Inference script for generating face images from new sketches
- 16 sample output figures included in the repository

---

## 🔬 Architecture

The model uses a **conditional GAN (cGAN)** architecture:
- **Generator** — Takes a sketch as input and generates a realistic face
- **Discriminator** — Distinguishes between real and generated face images
- Both networks are trained adversarially to improve output quality

---

## 📦 Dataset

Contact the author for dataset access: **nabjad258@gmail.com**

Common publicly available alternatives include the CUHK Face Sketch Database (CUFS).

---

## 🛠️ Tech Stack

| Library | Purpose |
|--------|---------|
| `TensorFlow` / `Keras` | GAN model building and training |
| `OpenCV` | Image loading and preprocessing |
| `NumPy` | Array operations |
| `Matplotlib` | Visualization of outputs |

---

## 🚀 Getting Started

### Install Dependencies

```bash
pip install tensorflow opencv-python numpy matplotlib
```

### Prepare Dataset

```bash
python DatasetCreator.py
```

### Train the GAN

```bash
python GAN.py
```

### Run Inference

```bash
python predictor.py --input your_sketch.jpg
```

---

## 📄 Publication

If you use this code, please cite our paper:

> **Sketch to Face Conversion Using GAN for Forensic Research**  
> Published in IJIRSET, February 2021  
> 🔗 [Read the Paper](http://ijirset.com/upload/2021/february/69_Sketch_NC.pdf)

---

## 📬 Contact

For queries or dataset requests: **nabjad258@gmail.com**

---

## ⚠️ Ethical Note

This tool is designed for **forensic and law enforcement research purposes only**. Misuse for generating deceptive imagery is strongly discouraged.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
