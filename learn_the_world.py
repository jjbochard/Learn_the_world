import json

def read_values_from_json(path, key):
	values = []
	with open(path) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[key])
		return values


def create_list(path, key, title_list):
	title_list = read_values_from_json(path, key)
	return title_list

	
def learn():
	learn_country = country_list()
	learn_capital = capital_list()
	learn_currency = currency_list()
	learn_language = language_list()
	len_list = len(learn_country)
	i = 0
	while i < len_list:
		first_letter_country = learn_country[i][0]
		print("COUNTRY : " + learn_country[i])
		print("CAPITAL : " + learn_capital[i])
		print("CURRENCY : " + learn_currency[i])
		print("LANGUAGE : " + learn_language[i])
		print("--------------------------------------------------------------------------------")
		i += 1


##########
def country_list():
	return create_list("country.json", "country", "country")

def capital_list():
	return create_list("capital.json", "capital", "capital")

def currency_list():
	return create_list("currency.json", "currency", "currency")

def language_list():
	return create_list("language.json", "language", "language")
##########



learn()


