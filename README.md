<h3 align="center">
    Sobel Filter in Python
</h3>

<p align="center">
  <img width="500" src="https://github.com/user-attachments/assets/e5855178-6c21-465e-a39b-fa496f02eb3b"
</p>

<p align="center">
  <i>
    Simple sobel image processor coded in Python.
  </i>
</p>


## 📖 About
> Refer [here](https://en.wikipedia.org/wiki/Sobel_operator) for a full in-depth explanation of how it works.

A _Sobel filter_, also referred to as the _Sobel operator_ or _Sobel–Feldman operator_ is a process applied to images for edge detection. Put simply, it functions by checking the gradient between pixels to determine if a part of an image is considered to be an edge or outline. 

If there is a large gradient (i.e. great change) between 2 pixel intensities, it is a likely indicator of an edge, and vise versa. By then applying a threshold, a level of control is had over what consititutes as an edge. As such, images such as the one above can be generated with varying degress of success.

For ease of use, the program includes a simple GUI for applying the filter to your own images.

## 🚀 Quickstart 

## 📘 Getting Started 
> This project was built on Python (ver. 3.13) using Pillow (ver. 11.2.1) and Tkinter (ver. 0.1.0), hence these versions are recommended to ensure the program functions as intended.

### Prerequisites
- _Python_ (ver. 3.13 or later) — see [this guide](https://wiki.python.org/moin/BeginnersGuide/Download) for installation help.
- _Pillow_ (ver. 11.2.1 or later)
- _Pillow_ (ver. 0.1.0 or later) 

### Installation
1. Install the latest verion of [_pip_](https://pip.pypa.io/en/stable/) for _Python_.
```bash
python3 -m ensurepip --upgrade
```

2. Install _Pillow_ library using pip
```bash
python3 -m pip install pillow
```

3. Install _Tkinter_ library using pip
```bash
python3 -m pip install tk
```

4. Clone the repo
```bash
git clone https://github.com/e1ijah-c/SobelFilter.git
```

5. Set git remote url to avoid pushes to base project
```bash
git remote set-url origin  https://github.com/e1ijah-c/SobelFilter.git
git remote -v
```

### Usage
1. Download the project. 
2. Navigate to the project directory on your local system.
3. Run the "main.py" file.
4. Select the "Upload Image" button and choose the image you want to apply the Sobel filter.
> ###### Upon completion of step 3: A preview of the image should appear. 
4. Select the "Export" button to save the sobel image.
5. The resulting image can be accesssed in the "output" folder.

## ⛏️ Useful Resources
> Some additional resources I felt helped me conceptually and with the overall project.

- [_Step-by-step Guide_](https://automaticaddison.com/how-the-sobel-operator-works/) on the Sobel Operator functions conceptually and mathematically.
- [_Tutorial on GitHub_](https://cse442-17f.github.io/Sobel-Laplacian-and-Canny-Edge-Detection-Algorithms/) showing how the Sobel filter works in general.

## ☎️ Contact

**Email:** elijahchia255@gmail.com\
**Project Link:** https://github.com/e1ijah-c/Img2ASCII

