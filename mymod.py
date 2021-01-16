# PART B-- THE MODULE

# Function a

def table_print(user_list, header, width = 10):
    output = "{:<{}} {:<{}}" 
    print(output.format(header[0],width,header[1],width), end = '')
    print('\n' + "-" * (width*2))
    for data, data1 in user_list:
        print(output.format(data, width, data1, width))
    print()
    

# Function b
def insertion_sort(values, pos):
    for i in range(1, len(values)):
        j = i
        while j > 0 and values[i][pos] < values[j-1][pos]:
            j -= 1
        values.insert(j,values.pop(i))
    return values 


##def selection_sort(values, pos):
##    for i in range(len(values)-1):
##        maxval = i
##        for j in range(i+1, len(values)):
##            if values[maxval][pos] > values[j][pos]:
##                maxval = j
##    temp = values[i]
##    values[i] = values[maxval]
##    values[maxval] = temp
##
##    temp1 = values[maxval]
##    values[maxval] = values[i]
##    values[i] = temp1
##
##    return values

# Function c
def tallied_data(user_list, col_query, col_tally):    
    summary = {}
    for values in user_list:
        
        if values[col_query] not in summary:
            summary[values[col_query]] = int(values[col_tally])
        else:
            summary[values[col_query]] += int(values[col_tally])

    sum_sorted = list(summary.items())
    insertion_sort(sum_sorted, 1)
    sum_sorted.reverse()
    return sum_sorted


##for row in user_list:
##        if (col_query, col_tally) in data:
##            data[col_query] += row[col_tally]
##        else:
##            data[col_query] = row[col_tally]

#return summary.items()

##new_data = [(user_list[item],item) for item in user_list if item in user_list]
##    return new_data

