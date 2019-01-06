def parse_metrics(value):
    if ' ' in value:
        value = value.split(' ')
        
        return [parse_metrics(v) for v in value]

    if value.endswith('px'):
        return value[:-2]
    
    return value