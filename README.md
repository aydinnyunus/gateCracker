# GateCracker 🤖

Find default passwords on Smart Locks in Turkey

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)

## Prerequisites

Before running gateCracker, you need to set up and run the REST API server:

1. Clone the REST API repository: `git clone https://github.com/aydinnyunus/gateCracker-REST.git`
2. Navigate to the REST API directory: `cd gateCracker-REST`
3. Install dependencies: `go mod tidy`
4. Run the API server: `go run main.go`
5. The API will be available at `http://localhost:8080`

## How to run the project? 🤔

1. Clone github repository in your local system: `git clone https://github.com/aydinnyunus/gateCracker.git`
2. Move in gateCracker repository: `cd gateCracker`
3. Create new virtual python environment: `python3 -m venv venv`
4. Activate virtual python environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install all the libraries mentioned in [requirements.txt](https://github.com/aydinnyunus/gateCracker/blob/master/requirements.txt) using: `pip install -r requirements.txt`
6. Make sure the REST API server is running on `http://localhost:8080` (see Prerequisites above)
7. Run Python file: `python main.py`

## Directory Tree 🌵

```bash
.
├── images
│   ├── website.png
├── README.md
├── requirements.txt
└── main.py
```

## ScreenShot 📸

**1).** This is the Main Page of the website. Select your model on the Select Box Menu.

![github-small](images/website.png)

## Blog Post

[https://sockpuppets.medium.com/bypassing-door-passwords-4004b8d7995](https://sockpuppets.medium.com/bypassing-door-passwords-4004b8d7995)

## Bug / Feature Request 👨‍💻

If you find a bug (the application couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/aydinnyunus/gateCracker/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/aydinnyunus/gateCracker/issues/new). Please include sample queries and their corresponding results.

## Connect with me! 🌐

[<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/linkedin.png" title="LinkedIn">](https://linkedin.com/in/yunus-ayd%C4%B1n-b9b01a18a/) [<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/github.png" title="Github">](https://github.com/aydinnyunus/ai-captcha-bypass) [<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/instagram-new.png" title="Instagram">](https://instagram.com/aydinyunus_/) [<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/twitter-squared.png" title="Twitter">](https://twitter.com/aydinnyunuss)
