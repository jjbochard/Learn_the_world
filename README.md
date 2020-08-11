# Learn_the_world

I always want to learn country and their capitals. So I use my skills in python to code this quick application. It was mainly inspire from the course "Démarrez votre projet avec Python" from Openclassrooms (link : https://openclassrooms.com/fr/courses/4262331-demarrez-votre-projet-avec-python/4264121-bonus-collectez-des-citations-automatiquement-avec-scrapy)

## How to use

Launch the scraper :
- Start to delete the old files :
    rm -rf country.json
- Then launch the scraper :
    scrapy runspider country_scraper.py -o country.json
- Do the last step for capital.json, currency.json and language.json
- Then launch the python files : 
python3 learn_the_world.py
