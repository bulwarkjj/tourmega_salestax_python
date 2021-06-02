import csv



customer = r'input.csv'
receipt = r'output.csv'


def entries():
    """
    Create input.csv file from user input
    :return:
    """
    outfile = open(customer, 'w', newline='')
    w = csv.writer(outfile)

    while True:
        quantity = input("Enter Quantity: ")
        product = input("Enter Product: ")
        price = input("Enter Price: ")
        print(quantity, product, price)
        w.writerow([quantity, product, price])
        add = input("would you like to add more? y/n")
        if add.lower() == 'n':
            print("receipt finsihed")
            outfile.close()
            break

def apply_taxes():
    """
    read user input from input.csv and apply correct tax base
    to products
    :return:
    """
    total = 0.0
    sales_tax = 0.0
    exempt_list = ["chocolate bar", "book", "packet of headache pills"]
    convert_list =[]


    # turn input.csv into a nest listed to modify
    with open(customer, 'r') as read_obj:
        read = csv.reader(read_obj)
        nest_list = list(read)
        print(nest_list)

    # affect changes to the nest list relating to tax details using a quick sort
    while len(nest_list) > 0:
        if "imported" in nest_list[0][1] and "chocolates" in nest_list[0][1]:
            import_tax = [nest_list[0][0], nest_list[0][1],
                          round(float(nest_list[0][2]) + float(nest_list[0][2]) * 0.05, 2)]

            convert_list.append(import_tax)
            total += float(nest_list[0][2])
            sales_tax += float(nest_list[0][2]) * 0.05
        elif "imported" in nest_list[0][1] and "perfume" in nest_list[0][1]:
            import_tax = [nest_list[0][0], nest_list[0][1],
                          round(float(nest_list[0][2]) + float(nest_list[0][2]) * 0.15, 2)]

            convert_list.append(import_tax)
            total += float(nest_list[0][2])
            sales_tax += float(nest_list[0][2]) * 0.15
        elif nest_list[0][1] in exempt_list:
            import_tax = [nest_list[0][0], nest_list[0][1], nest_list[0][2]]
            convert_list.append(import_tax)
            total += float(nest_list[0][2])
        else:
            import_tax = [nest_list[0][0], nest_list[0][1],
                          round(float(nest_list[0][2]) + float(nest_list[0][2]) * 0.10, 2)]
            convert_list.append(import_tax)
            total += float(nest_list[0][2])
            sales_tax += float(nest_list[0][2]) * 0.10
        del nest_list[0]

    # apply the changes to output.csv
    with open(receipt, 'w') as file:
        write = csv.writer(file)
        write.writerows(convert_list)














