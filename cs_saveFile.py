import cs_data
#import serial

#ser = serial.Serial('/dev/ttyUSB0', 115200)

def saveData():
    # Data_str = ser.readline().decode("utf-8")
    Data_str = input('Data 입력: ')
    Data_lst = Data_str.split(":")
    print(Data_lst)

    if Data_lst[0] == "E" and Data_lst[2] == "E":
        Data_E = cs_data.saveData('E', Data_lst[1])

        Data_E.save_file()

    if Data_lst[0] == "T" and Data_lst[3] == "T":
        Data_T = cs_data.saveData('T', Data_lst[1])
        Data_H = cs_data.saveData('H', Data_lst[2])

        Data_T.save_file()
        Data_H.save_file()


    if Data_lst[0] == "P" and Data_lst[3] == "P":
        Data_P = cs_data.saveData('P', Data_lst[1])
        Data_D = cs_data.saveData('D', Data_lst[2])

        Data_P.save_file()
        Data_D.save_file()


while True:
    saveData()

