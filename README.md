# 10fastfingers-bot

### REQUIREMENTS :

1. Chrome version 88.0.4324.150 or any other version with the corresponding [chromedriver.exe](https://chromedriver.chromium.org/)

2. [Python 3+](https://www.python.org/) with [selenium](https://pypi.org/project/selenium/) & [pytesseract](https://pypi.org/project/pytesseract/)

3. [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/) 5.0.0+

### HOW TO USE :

This bot is customizable, you can change the following variables in main.py :
- type_url : you can change the language
- mail : change this variable to your 10fastfingers account email
- password : change this variable to your 10fastfingers account password
- wait_duration : the lower this value is, the faster the bot will be
- wrong_word_probability : the lower this value is, the less likely the bot will type a wrong word
- word_correction_probability : the lower this value is, the less likely the bot will type a wrong letter and correct it

### HOW TO PASS THE ANTICHEAT TEST :

(The wait_duration variable in anticheat_test.py should be lesser than the one in main.py)

If you get a higher score than 120 WPM, you'll need to pass their anticheat test, to do that you'll need to do the following steps :

1. Get onto the anticheat test page (you should receive a notification)

2. Click on start

3. Take a screenshot of all the words you need to type

4. Save the screenshot as Capture.PNG in the folder where anticheat_test.py is

5. Execute anticheat_test.py

6. Get back to the anticheat test page and click on the input box in less than 2 seconds

7. When you see that the last word has been typed click on Sumbit

8. If it failed to unlock redo everything from step 1 (you can try to lower wait_duration variable too)
