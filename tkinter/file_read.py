def read_file():
    d = {}
    with open('acc.txt', 'r', encoding='utf-8') as file:
        for line in file:
            model_string, box = line.strip().split(':')
            box = box.strip()
            for model in model_string.strip().split(','):
                model = model.strip()
                if model not in d:
                    d[model] = []
                d[model].append(box)
    return d
