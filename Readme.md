# Chronic Kidney Disease Detection
 -  *Using flask and basic machine learning concepts I have built a small backend in flask to reuse the model*
 -  [API REFERENCE](/POST.md)

## Steps for running project
 ###  *`Step-1`*
 - #### Clone the repository
  ```
  git clone https://github.com/Hemant-Stellar/Chronic_kidney_disease_detection.git
  cd Chronic_kidney_disease_detection
  ```
### *`Step-2`*
- #### Create Virtual Environment
  ```
  python -m venv .venv
  ```
### *`Step-3`*
- #### activate Virtual Environment
- ##### for windows
  ```
  .venv\Scripts\activate
  ```
- ##### for mac
   ```
    . .venv/bin/activate
   ```
 ### *`Step-4`*
 - #### install dependencies
   ```
   pip install -r requirements.txt
   ```
### *`Step-5`*
- #### train model and save
  ```
  python saved_model.py
  ```
### *`Step-6`*
- #### run server
  ```
  flask run
  ```
  

