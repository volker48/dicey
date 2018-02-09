# Diceware
A bare bones web app for generating passwords/passphrases using the EFF word list using 
[Diceware](https://en.wikipedia.org/wiki/Diceware).

### Usage
You'll need python.

1. Install the pip requirements `pip install -r requirements.txt`
2. Run the app `python app.py`.
3. Open [http://localhost:5000/](http://localhost:5000/) to generate 6 words. Append a number `N` like
`http://localhost:5000/10` to generate 10 words. The minimum you can generate for a secure password is 6.
