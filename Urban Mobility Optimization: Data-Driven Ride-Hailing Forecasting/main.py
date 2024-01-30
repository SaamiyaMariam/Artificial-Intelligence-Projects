
import pandas as pd
import os
import csv
import datetime

if __name__== "__main__" :
    
    print("Reading Datasets...")

    # current working directory
    print(os.getcwd())

    cluster_path = "training_data/cluster_map/cluster_map"#defining path for cluster files
    order_path_base = "training_data/order_data/order_data_2016-01-"#defining path for order files
    poi_path = "training_data/training_data/poi_data/poi_data"#defining path for poi files
    weather_path_base = "training_data/weather_data/weather_data_2016-01-"#defining path for weather files


    # storing file paths of all datasets
    all_paths=[]
    # cluster_map

    all_paths.append(cluster_path)
    # order_data
    order_paths = []
    start = 1
    end = 21
    while start <= end:
        order_path = order_path_base + str(start).zfill(2)  # Converting int to string and padding with leading zeros
        order_paths.append(order_path)
        print("file path: ", order_paths[start-1])
        start += 1
        all_paths.append(order_path)
    # poi_data

    all_paths.append(poi_path)
    # weather_data
    weather_paths=[]
    start=1
    while start <= end:
        weather_path = weather_path_base + str(start).zfill(2)  # Converting int to string and padding with leading zeros
        weather_paths.append(weather_path)
        print("file path: ", weather_paths[start-1])
        start += 1
        all_paths.append(weather_path)

    #storing start_region_hash & time column:
    data = []
    newfile='order_data_new.csv'
    # Read and append the data from input files to the list
    for path in order_paths:
        with open(path, newline='') as input:
            Readers = csv.reader(input, delimiter='\t')
            for row in Readers:
                data.append([row[1], row[2], row[3], row[6]])#appnding all req columns


    data.sort(key=lambda x: x[2])#sorting data acc to start_region_hash

    # Write the sorted data to the output file
    with open(newfile, 'w', newline='') as output:
        writer = csv.writer(output, delimiter='\t')
        writer.writerows(data)


    # sorting our data according to reigion hash ( so we can merge the tables later on)
    data = []
    newfile2='cluster_data_new.csv'
    with open(cluster_path, newline='') as input:
        Readers = csv.reader(input, delimiter='\t')
        for row in Readers:
            data.append([row[0], row[1]])#appnding all req columns


    data.sort(key=lambda x: x[0])#sorting data acc to first col

    # Write the sorted data to the output file
    with open(newfile2, 'w', newline='') as output:
        writer = csv.writer(output, delimiter='\t')
        writer.writerows(data)


    # merging order_data_new and cluster_data_new

    order_path_new = 'order_data_new.csv'#paths for order file new
    cluster_path_new = 'cluster_data_new.csv'#paths for cluster file new

    # Loading our order data
    order_data = []
    with open(order_path_new, 'r', newline='') as order_input:
        order_reader = csv.reader(order_input, delimiter='\t')
        for row in order_reader:
            order_data.append(row)

    # Loading our cluster map data
    cluster_data = {}
    with open(cluster_path_new, 'r', newline='') as cluster_input:
        cluster_reader = csv.reader(cluster_input, delimiter='\t')
        for row in cluster_reader:
            cluster_data[row[0]] = row[1]

    # Updating order data with cluster data
    for row in order_data:
        start_region_hash = row[2]
        if start_region_hash in cluster_data:
            row.append(cluster_data[start_region_hash])
        else:
             row.append('')  # Adding empty val if region hash isnt found

    # # Writing our updated order data to a new file
    merged_file = 'merged_data.csv'
    
    with open('rolling_sum.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([])
    with open(merged_file, 'w', newline='') as merged_output: #opning file
        writer = csv.writer(merged_output, delimiter='\t')
        writer.writerows(order_data)

    newfile3='poi_data_new.csv'
    with open(newfile3, 'w', newline='') as output: #opning file
        writer = csv.writer(output, delimiter='\t')
        with open(poi_path, newline='') as input:
            reader = csv.reader(input, delimiter='\t') #reads file 
            for row in reader:
                writer.writerow([row[0], row[1]])


    poi_path_new = 'poi_data_new.csv'

    # merging merged_data with poi data

    merged_path_new = 'merged_data.csv'
    poi_path_new = 'poi_data_new.csv'

    # Loading our merged data
    merged_data = []
    with open(merged_path_new, 'r', newline='') as merged_input:
        merged_reader = csv.reader(merged_input, delimiter='\t')
        for row in merged_reader:
            merged_data.append(row)

    # Loading our poi data
    poi_data = {}
    with open(poi_path_new, 'r', newline='') as poi_input:
        poi_reader = csv.reader(poi_input, delimiter='\t')
        for row in poi_reader:
            poi_data[row[0]] = row[1]

     # Updating merged data with poi data
    for row in merged_data:
        start_region_hash = row[2]
        if start_region_hash in poi_data:
            row.insert(5, poi_data[start_region_hash])
        else:
            row.insert(5, '') # Adding empty val if region hash isnt found       


    # Writing our updated order data to a new file
    merged_file = 'merged_data.csv'
    with open(merged_file, 'w', newline='') as merged_output:
        writer = csv.writer(merged_output, delimiter='\t')
        writer.writerows(merged_data)

    #merging weather
    sorted_rows=[]
    with open(merged_file,newline='') as input:
        reader=csv.reader(input,delimiter='\t')
        for row in reader:
            sorted_rows.append(row)
    sorted_rows.sort(key=lambda x:x[3])

    with open(merged_file, 'w', newline='') as output:
        writer = csv.writer(output, delimiter='\t')
        writer.writerows(sorted_rows)




    newfile3='weather_data_new.csv'
    sorted_rows2=[]
    for path in weather_paths:
        with open(path, newline='') as input:
                reader = csv.reader(input, delimiter='\t')#reds file
                for row in reader:
                    sorted_rows2.append(row)
    sorted_rows2.sort(key=lambda x:x[0])
    with open(newfile3, 'w', newline='') as output:
        writer = csv.writer(output, delimiter='\t')
        writer.writerows(sorted_rows2)

    merge_data = []
    with open(merged_file, 'r', newline='') as merge_input:
        merge_reader = csv.reader(merge_input, delimiter='\t')
        for row in merge_reader:
            merge_data.append(row)

    weather_data = {}
    with open(newfile3, 'r', newline='') as weather_input:
        weather_reader = csv.reader(weather_input, delimiter='\t')
        for row in weather_reader:
            weather_data[row[0]] = row[2]

    updated_rows = []
    for row in merge_data:
        if row[3] in weather_data:
            row.insert(6, weather_data[row[3]])
        else:
            row.insert(6, '')
        updated_rows.append(row)

    #print(weather_data)
    with open(merged_file, 'w', newline='') as merged_output:
        writer = csv.writer(merged_output, delimiter='\t')
        writer.writerows(updated_rows)


    import datetime
    window_size = 60  # window size = 1 min = 60 seconds
    last_timestamp = datetime.datetime.min
    # Read and append the data from input files to the list
    for path in order_paths:
        with open(path, newline='') as input:
            reader = csv.reader(input, delimiter='\t')#reads input
            sorted_rows = sorted(reader, key=lambda row: datetime.datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S'))
            accepted_orders = []
            window_accepted = 0 
            last_timestamp = None 
            with open(merged_file, 'w', newline='') as output:
                writer = csv.writer(output, delimiter='\t')
                for i, row in enumerate(sorted_rows):#travers rows
                    #dif = (datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S') - last_timestamp).total_seconds()
                    if last_timestamp is not None: # and dif > window_size:#chcks
                        # Reset the accepted orders list for a new window
                        accepted_orders = []
                        window_accepted = 0  # Reset window_accepted to 0 for a new window
                    # creating a new column to store whether or not an order was accepted
                    accepted = row[1] != 'NULL'

                    # Update the accepted orders list
                    accepted_orders.append(accepted)

                    # Calculate the rolling sum for the last 1 hour (3600 seconds)
                    window_accepted = sum(accepted_orders)#rolling sum 
                    last_timestamp=datetime.datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')#lasttimestamp
                    # Write the row to the output file with the rolling sum
                    writer.writerow([row[0], row[1], row[2], row[3],row[4],row[5],accepted, window_accepted])#writing rows

    # MODEL TRAINING
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split


    # Load the data
    data = pd.read_csv('C:/Users/Saamiya M/Desktop/Semester 6/Artificial Intelligence/phase1/rolling_sum.csv')

        
    data['time'] = pd.to_datetime(data['time']).astype('int64') // 10**9

    # Create a new column that represents the count of occurrences of each unique string value
    passenger_id_counts = data['passenger_id'].value_counts()
    data['passenger_id_count'] = data['passenger_id'].apply(lambda x: passenger_id_counts[x])

    # One-hot encode the region hash and poi class columns
    region_id_encodings = pd.get_dummies(data['region_id'], prefix='region')
    poi_class_encodings = pd.get_dummies(data['poi_class'], prefix='poi_class')
    data = pd.concat([data, region_id_encodings, poi_class_encodings], axis=1)

    # Extract features and target variable
    X = data[['passenger_id_count', 'time'] + list(region_id_encodings.columns) + list(poi_class_encodings.columns)]
    y = data['order_count']

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model on the data
    model.fit(X, y)

    # Plot the data and the regression line
    plt.scatter(data['time'], y)
    plt.plot(data['time'], model.predict(X), color='r')
    plt.title('Number of orders accepted vs. No. of Orders Placed')
    plt.xlabel('Time')
    plt.ylabel('Number of orders accepted')
    plt.show()
