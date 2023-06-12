# Функция для генерации фильтрации SQL
def generate_filter_query(filters):
    query = "SELECT * FROM survey WHERE 1"
    values = []
    sort_key = ''

    for key, value in filters.items():
        if value is not None and "comparison" not in key:
            if "," in value:
                lst_value = value.split(',')
                query += f" AND {key} BETWEEN ? AND ?"
                values += lst_value
            elif key == "sort_key":
                sort_key = value
            else:
                if filters[key + "_comparison"] is not None:
                    if filters[key + "_comparison"] == 'less':
                        query += f" AND {key} < ?"
                    elif filters[key + "_comparison"] == 'greater':
                        query += f" AND {key} > ?"
                else:
                    query += f" AND {key} = ?"
                values.append(value)
    if sort_key != '':
        query += f" ORDER BY {sort_key}"

    return query, values
