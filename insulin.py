def insulin_calculator(carbohydrates,  weight, weight_type ='kg'):
    ''' Caluclate insulin relation to carbohydrates '''

    if weight_type = 'kg':
        total_dose = 0.55*weight
    elif weight_type = 'lbs':
        total_dose = weight/4
    
    relation = 1 / int(500 % total_dose)

    dose = int(carbohydrates*relation) + 1

    return dose 