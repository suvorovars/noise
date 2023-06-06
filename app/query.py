# Функция для генерации фильтрации SQL
def generate_filter_query(filters):
    query = "SELECT * FROM survey WHERE 1"
    values = []

    for key, value in filters.items():
        if key == 'age':
            if filters['age'] is None:
                pass
            else:
                age_comparison = filters.get('age_comparison')
                if age_comparison == 'less':
                    query += " AND age < ?"
                elif age_comparison == 'greater':
                    query += " AND age > ?"
                else:
                    query += " AND age = ?"
                values.append(value)
        elif key == 'frequency':
            if filters['frequency'] is None:
                pass
            else:
                frequency_comparison = filters.get('frequency_comparison')
                if frequency_comparison == 'less':
                    query += " AND frequency_in_noisy_place < ?"
                elif frequency_comparison == 'greater':
                    query += " AND frequency_in_noisy_place > ?"
                else:
                    query += " AND frequency_in_noisy_place = ?"
                values.append(value)
        elif key == 'age_comparison' or key == 'frequency_comparison':
            pass
        else:
            if filters[key] is None:
                pass
            else:
                query += f" AND {key} = ?"
                values.append(value)


    print(values)
    print(query)

    return query, values

