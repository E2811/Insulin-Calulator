from sql_queries import getDataUser
def insulin_calculator(carbohydrates,  user_id, weight_type ='kg'):
    ''' Caluclate insulin relation to carbohydrates '''
    weight = getDataUser(user_id)['weight']
    if weight_type == 'kg':
        total_dose = 0.55*weight
    elif weight_type == 'lbs':
        total_dose = weight/4
    
    relation = 1 / int(500 % total_dose)

    dose = int(carbohydrates*relation) + 1

    return dose 