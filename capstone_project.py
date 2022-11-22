ListEmployeeData = [
    {
    'NIK'       : '0122001',
    'Name'      : 'Juha Bach Ywach',
    'Age'       : '50',
    'Gender'    : 'Male',
    'Position'  : 'Head of Data',
    'Address'   : 'Jl Pancoran I No 01'
    },
    {
    'NIK'       : '0222002',
    'Name'      : 'Jugram Haschwalt',
    'Age'       : '30',
    'Gender'    : 'Male',
    'Position'  : 'Busdev Manager',
    'Address'   : 'Jl Kebon Kacang 2 No 12'
    },
    {
    'NIK'       : '0222003',
    'Name'      : 'Gerard Valkyrie',
    'Age'       : '35',
    'Gender'    : 'Male',
    'Position'  : 'Marketing Manager',
    'Address'   : 'Jl Pasir Jati III'
    },
    {
    'NIK'       : '0222004',
    'Name'      : 'Bambieta Basterbine',
    'Age'       : '27',
    'Gender'    : 'Female',
    'Position'  : 'Data Architec',
    'Address'   : 'Jl Andir II No 11'
    },
    {
    'NIK'       : '0122005',
    'Name'      : 'Candice Catnip',
    'Age'       : '26',
    'Gender'    : 'Female',
    'Position'  : 'Data Science',
    'Address'   : 'Jl Kejora No 7'
    }
]

# From Main Menu, option no 1 show employee data => (if input number 1 from Main_menu)
def ShowData():
    InputShowData = (int(input('''
        Employee Data Menu :
        1. Show Employee Database
        2. Find Employee Data
        3. Back To Main Menu
        
        Input :''')))
    if InputShowData == 1:
        EmployeeData()
        InputTesting = input('''
        Continue ? (Yes/No)
        Input Here : ''')
        if (InputTesting == 'no' or InputTesting == 'No'):
            Main_menu()
        else:
            ShowData()       
    elif InputShowData == 2:
        FindEmployee()
    elif InputShowData == 3:
        Main_menu()
    else:
        print()
        print(''' \tYou Input the Wrong Option\n
        Choose one from the list ''')
        ShowData()

# Part of show data, option no 1 show employee database
def EmployeeData ():
    print(' ======================= Employee Database ======================= \n')
    for idx, i in enumerate(ListEmployeeData):
        print(f"{i['NIK']} | {i['Name']} \t| {i['Age']} | {i['Gender']} \t| {i['Position']}\t| {i['Address']}")

# Part of show data, option no 2 find employee data
def FindEmployee():
    EmployeeData()
    InputNIK = input('\n\nInput Employee NIK: ')
    for i in range (len(ListEmployeeData)):
        if InputNIK == ListEmployeeData[i]['NIK']:
            print(f'''\n{ListEmployeeData[i]['NIK']} | {ListEmployeeData[i]['Name']} | {ListEmployeeData[i]['Age']} | {ListEmployeeData[i]['Gender']} | {ListEmployeeData[i]['Position']} \t\t| {ListEmployeeData[i]['Address']}
            ''')
            InputNIK = input('''
            Continue ? (Yes/No)
            Input Here : ''')
            if (InputNIK == 'no' or InputNIK == 'No'):
                ShowData()
            else:
                FindEmployee()
    print('''\nThe employee data you are looking for not be found \n
Please input correct NIK
            ''')
    FindEmployee()

# From Main Menu, option no 2 add employee data => (if input number 2 from Main_menu)
def AddData():
    InputAddData = (int(input('''
    Add Employee Data Menu :
        1. Add New Data
        2. Back to Main Menu
    Choose one of the option : ''')))
    if  InputAddData == 1:
        EmployeeNIK = input('Input NIK Employee that you want to add :')
        for i in ListEmployeeData:
            if EmployeeNIK == i['NIK']:
                print('''
This NIK already registered\n
Please input new NIK''')
                AddData()

        EmployeeName = input('Input new employee name that you want to add :')
        EmployeeAge = input('Input new employee age that you want to add :')
        EmployeeGender = input('Input new employee gender that you want to add :')
        EmployeePoisition = input('Input new employee position that you want to add :')
        EmployeeAddress = input('Input new employee address that you want to add :')

        Confirmation = input('''
Are you sure want to add new employee data ? (Yes/No)
    ''')
        if Confirmation == 'Yes' or Confirmation == 'yes':
                ListEmployeeData.append({
                    'NIK'       : EmployeeNIK,
                    'Name'      : EmployeeName,
                    'Age'       : EmployeeAge,
                    'Gender'    : EmployeeGender,
                    'Position'  : EmployeePoisition,
                    'Address'   : EmployeeAddress
                })
                print('New employee data has been added')
                Confirmation = input('''
Continue ? (Yes/No)
Input Here :  ''')
                if (Confirmation == 'no' or Confirmation == 'No'):
                    Main_menu()
                else:
                    AddData()
        else:
                print('New employee data has not been added')
                AddData()
    elif InputAddData == 2:
        Main_menu()
    else:
        print('''
        You input the wrong choice
        Please input 1 or 2 from list
        ''')
        AddData()

# From Main Menu, option no 3 update employee data => (if input number 3 from Main_menu)
def UpdateData():
        UpdateDataEmployee = (input('''
        Update Employee Menu :
        1. Update Employee Menu
        2. Back to Main Menu
        Choose one of the option : '''))

        if UpdateDataEmployee == '1':
            EmployeeData()
            NIKEmployee = (input('Input NIK Employee: '))
            for i in ListEmployeeData:
                if NIKEmployee == i['NIK']:
                    print(' Employee Data Found ')
                    ConfirmUpdate = input('''
                    Do you want to update the data ? (Yes/No)
                    Input you choice : ''')
                    if ConfirmUpdate == 'Yes' or ConfirmUpdate == 'yes':
                        UpdateList = input('''
                        Select one of the following list you want to update
                        1. NIK
                        2. Name
                        3. Age
                        4. Gender
                        5. Position
                        6. Address

                        which one you want to update : ''')

                        if UpdateList == '1':
                            NIKNewUpdate = input('Input new NIK')
                            ConfirmationUpdate = input('Are you sure want to update data (Yes/No) ?')
                            if ConfirmationUpdate == 'Yes' or ConfirmationUpdate == 'yes':
                                i['NIK'] = NIKNewUpdate
                                print('Data has been updated')
                                EmployeeData()
                                UpdateData()
                            else:
                                print('Data has not updated')
                                UpdateData()
                        elif UpdateList == '2':
                            NameNewUpdate = input('Input new Name')
                            ConfirmationUpdate = input('Are you sure want to update data (Yes/No) ?')
                            if ConfirmationUpdate == 'Yes' or ConfirmationUpdate == 'yes':
                                i['Name'] = NameNewUpdate
                                print('Data has been updated')
                                EmployeeData()
                                UpdateData()
                            else:
                                print('Data has not updated')
                                UpdateData()
                        elif UpdateList == '3':
                            AgeNewUpdate = input('Input new Age')
                            ConfirmationUpdate = input('Are you sure want to update data (Yes/No) ?')
                            if ConfirmationUpdate == 'Yes' or ConfirmationUpdate == 'yes':
                                i['Name'] = AgeNewUpdate
                                print('Data has been updated')
                                EmployeeData()
                                UpdateData()
                            else:
                                print('Data has not updated')
                                UpdateData()
                        elif UpdateList == '4':
                            GenderNewUpdate = input('Input new Gender')
                            ConfirmationUpdate = input('Are you sure want to update data (Yes/No) ?')
                            if ConfirmationUpdate == 'Yes' or ConfirmationUpdate == 'yes':
                                i['Name'] = GenderNewUpdate
                                print('Data has been updated')
                                EmployeeData()
                                UpdateData()
                            else:
                                print('Data has not updated')
                                UpdateData()
                        elif UpdateList == '5':
                            PositionNewUpdate = input('Input new Position')
                            ConfirmationUpdate = input('Are you sure want to update data (Yes/No) ?')
                            if ConfirmationUpdate == 'Yes' or ConfirmationUpdate == 'yes':
                                i['Name'] = PositionNewUpdate
                                print('Data has been updated')
                                EmployeeData()
                                UpdateData()
                            else:
                                print('Data has not updated')
                                UpdateData()
                        elif UpdateList == '6':
                            AddressNewUpdate = input('Input new Address')
                            ConfirmationUpdate = input('Are you sure want to update data (Yes/No) ?')
                            if ConfirmationUpdate == 'Yes' or ConfirmationUpdate == 'yes':
                                i['Name'] = AddressNewUpdate
                                print('Data has been updated')
                                EmployeeData()
                                UpdateData()
                            else:
                                print('Data has not updated')
                                UpdateData()
                        else:
                            print('Pilihan tidak tersedia')
                            UpdateData()
                    else:
                        print('Update data cancle')
                        UpdateData()
            print('Employee Data Not Found')
            UpdateData()
        elif UpdateDataEmployee == '2':
            Main_menu()
        else:
            print('Input between 1 or 2 from list')
            UpdateData()

# From Main Menu, option no 4 show employee data => (if input number 4 from Main_menu)
def DeleteData():
    EmployeeData()
    DeleteDataEmployee = input('''
    Delete Data Employee Menu :
        1. Delete Employee Data
        2. Back to Main Menu
        Choose one of the option : ''')
    if DeleteDataEmployee == '1':
        NIKEmployee = input('Input NIK Employee that you want to delete: ')
        for i in ListEmployeeData:
                if NIKEmployee == i['NIK']:
                    print('Employee Data Found ')
                    ConfirmDelete = input('''
    Do you want to delete the data ? (Yes/No)
    Input you choice : ''')
                    if ConfirmDelete == 'Yes' or ConfirmDelete == 'yes':
                        ListEmployeeData.remove (i)
                        print(f'Employee Data with NIK {NIKEmployee} HAS BEEN DELETED')
                        EmployeeData()
                        Continue = input('''
                        Continue ? (Yes/No)
                        Input Here : ''')
                        if (Continue == 'no' or Continue == 'No'):
                            Main_menu()
                        else:
                            DeleteData()
                    else:
                        print('Delet data cancel')
                        DeleteData()
        print('Employee Data Not Found')
        DeleteData()
    elif DeleteDataEmployee == '2':
            Main_menu()
    else:
            print('Input between 1 or 2 from list')
            DeleteData()
                
#Function main menu 
def Main_menu():
        Database_menu = (str(input
        ('''
        ======================= Employee Data Base PT Busur Abadi =======================
        
        Main Menu :
            1. Employee Database
            2. Add Employee Data
            3. Update Employee Data
            4. Delete Employee Data
            5. Exit Program

        Choose one from the list :  ''')))

        if(Database_menu == '1'):
            ShowData()
        elif(Database_menu == '2'):
            AddData()
        elif(Database_menu == '3'):
            UpdateData()
        elif(Database_menu == '4'):
            DeleteData()
        elif(Database_menu == '5'):
            print('''
            ============= Thank you for access employee data base PT Busur Abadi =============
            ''')
            exit()
        else:
            print()
            print(''' ========= You input the wrong option ========= \n Choose one from the list : ''')
            Main_menu()

print(Main_menu())
