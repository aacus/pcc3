def describe_city(city_name, country_name='Guatemala'):
    sentence = f'{city_name.title()} is in {country_name.title}.'
    print(sentence)

describe_city('Villa Nueva')
describe_city('Mixco')
describe_city('Reykjavik', 'Iceland')
