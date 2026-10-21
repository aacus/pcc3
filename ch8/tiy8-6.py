def city_country(city_name, country_name):
    """Return a string like 'Santiago, Chile' """
    return f'{city_name.title()}, {country_name.title()}'

city = city_country('Guatemala City', 'Guatemala')
print(city)

city = city_country('México DF', 'México')
print(city)

city = city_country('Santiago', 'Chile')
print(city)