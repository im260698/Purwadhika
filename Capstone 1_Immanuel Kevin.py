# List Member Powerlifting Gym (Source Data)
list_member_powerlifting_gym = [
['1','Kevin',25,'Male','183 cm','90 kg','180 kg','120 kg','200 kg'],
['2','Andre',29,'Male','175 cm','65 kg','110 kg','80 kg','140 kg'],
['3','Siska',22,'Female','162 cm','55 kg','90 kg','50 kg','100 kg'],
['4','Nadhif',21,'Male','180 cm','70 kg','150 kg','100 kg','180 kg'],
['5','Tasya',18,'Female','155 cm','52 kg','80 kg','40 kg','85 kg'],
['6','Joshua',31,'Male','178 cm','83 kg','130 kg','100 kg','200 kg'],
['7','Alvin',27,'Male','171 cm','70 kg','120 kg','90 kg','190 kg'],
['8','Kelvin',24,'Male','187 cm','95 kg','210 kg','140 kg','250 kg'],
['9','Silvia',21,'Female','165 cm','54 kg','80 kg','50 kg','100 kg'],
['10','Lavin',19,'Male','165 cm','48 kg','70 kg','50 kg','80 kg'],
['11','Jeslyn',30,'Female','171 cm','59 kg','130 kg','90 kg','160 kg'],
['12','Samuel',23,'Male','175 cm','62 kg','120 kg','100 kg','150 kg'],
['13','Farrel',20,'Male','170 cm','57 kg','100 kg','65 kg','120 kg'],
['14','Rachel',35,'Female','159 cm','54 kg','70 kg','50 kg','80 kg'],
['15','Johny',38,'Male','185 cm','95 kg','230 kg','140 kg','280 kg']
]

# Function Inquiry Member Data
def inquiry_member_data(): 
    inquiry=input('''
    Menu Inquiry Member Data
    1. Inquiry All Member Data
    2. Search Member Data by ID
    Input Inquiry Menu : ''')
    if inquiry == '1' :             
      print('Data Member Powerlifting Gym\n')      
      print ('ID\t|Name\t|Age|Gender\t|Height\t|Weight\t|Squat\t|Bench\t|Deadlift')
      for i in range(len(list_member_powerlifting_gym)):
       print(f'{list_member_powerlifting_gym[i][0]}\t|{list_member_powerlifting_gym[i][1]}\t|{list_member_powerlifting_gym[i][2]}\t|{list_member_powerlifting_gym[i][3]}\t|{list_member_powerlifting_gym[i][4]}\t|{list_member_powerlifting_gym[i][5]}\t|{list_member_powerlifting_gym[i][6]}\t|{list_member_powerlifting_gym[i][7]}\t|{list_member_powerlifting_gym[i][8]}')
    elif inquiry == '2' :
      search_by_id=input(
      'Input ID Member : ')
      print(f'{list_member_powerlifting_gym[int(search_by_id)-1][0]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][1]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][2]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][3]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][4]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][5]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][6]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][7]}\t|{list_member_powerlifting_gym[int(search_by_id)-1][8]}')
      

# Function Add Member Data (Fix)
def add_member_data() :
  add=input('''
  Menu Add Member Data
  1. Add Member Data 
  2. Cancel Add 
  Input Update Menu : ''')
  if add == '1':
    member_id=input('Please Input Member ID to Add : ')
    member_name=input('Please Input Member Name : ')
    member_age=input('Please Input Member Age: ')  
    member_gender=input('Please Input Member Gender : ')
    member_height=input('Please Input Member Height : ')
    member_weight=input('Please Input Member Weight : ')
    member_squat=input('Please Input Member Max Squat : ')
    member_bench=input('Please Input Member Max Bench : ')
    member_deadlift=input('Please Input Member Max Deadlift : ')
    
    # If New Member ID already Exist 
    if member_id in list_member_powerlifting_gym[0]:
      print('Data Already Exists!')
    
    # If New Member ID not Exist
    else :
      member_id not in list_member_powerlifting_gym[0] 
      confirm_save_data = input('Do You Want To Save Data? (Yes/No): ')
      # If Want Save New Member Data
      if confirm_save_data == 'Yes': 
        list_member_powerlifting_gym.append([member_id,member_name,member_age,member_gender,member_height,member_weight,member_squat,member_bench,member_deadlift]),print('Data Successfully Saved!')
      
      # If Don't Want Save New Member Data
      elif confirm_save_data == 'No' :  
        print('Data Not Saved.')
      # If Input Other Than Yes/No 
      else :
        print('Invalid Input!')
    

# Function Update Member Data
def update_member_data ():
  update=input('''
  Menu Update Member Data
  1. Update Member Data by ID
  2. Cancel Update
  Input Update Menu : ''')
  if update == '1': 
    member_id=input('Please Input Member ID to Update : ')
  # If Member ID Exist
    if member_id == list_member_powerlifting_gym[int(member_id)-1][0] :
      print(f'{list_member_powerlifting_gym[int(member_id)-1][0]}\t|{list_member_powerlifting_gym[int(member_id)-1][1]}\t|{list_member_powerlifting_gym[int(member_id)-1][2]}\t|{list_member_powerlifting_gym[int(member_id)-1][3]}\t|{list_member_powerlifting_gym[int(member_id)-1][4]}\t|{list_member_powerlifting_gym[int(member_id)-1][5]}\t|{list_member_powerlifting_gym[int(member_id)-1][6]}\t|{list_member_powerlifting_gym[int(member_id)-1][7]}\t|{list_member_powerlifting_gym[int(member_id)-1][8]}')
    confirm_update=input('Continue Update? (Yes/No): ') 
    if confirm_update=='Yes' : 
      column_update=input('Please insert column index that you want to change : ')
      column_new_value=input('Insert column new value : ')
      save_update=input('Update Data? (Yes/No): ')
      if save_update =='Yes' :
        list_member_powerlifting_gym[int(member_id)-1][int(column_update)] = column_new_value
        print('Data Successfully Updated!')
      elif save_update =='No' : 
        print('Data Not Updated')
      else :
        print('Invalid Input')
    else :
      print('Data does not exist')

      
      


# Function Delete Member Data
def delete_member_data():
  delete=input('''
  Menu Delete Member Data
  1. Delete Member Data by ID
  2. Cancel Delete
  Input Delete Menu : ''')
  if delete == '1': 
    member_id=input('Please Input Member ID to Delete : ')
    if member_id == list_member_powerlifting_gym[int(member_id)-1][0] :
      confirm_delete=input('Do You Want To Delete Data? (Yes/No): ')
      if confirm_delete == 'Yes' : 
        list_member_powerlifting_gym.remove(list_member_powerlifting_gym[int(member_id)-1])
        print('Data Successfully Deleted!')
      elif confirm_delete == 'No' : 
        print('Data Not Deleted')
      else :
        print('Invalid Input')

def doorprize_member():
  import random
  doorprize=input('''
  Welcome to Powerlifting Gym Doorprize Menu
  1. Spin the wheel to pick 1 Year Membership Doorprize Winner
  2. Spin the wheel to pick Whey Protein Doorprize Winner
  3. Spin the wheel to pick Gym Bag Doorprize Winner
  Input Doorprize Menu : ''')
  if doorprize == '1':
    print('Spinning the wheel...')
    winner = random.choice(list_member_powerlifting_gym)
    print(f'{winner[1]} You Got 1 Year Membership Doorprize')
  elif doorprize == '2':
    print('Spinning the wheel...')
    winner = random.choice(list_member_powerlifting_gym)
    print(f'{winner[1]} You Got Whey Protein Doorprize')
  elif doorprize == '3':
    print('Spinning the wheel...')
    winner = random.choice(list_member_powerlifting_gym)
    print(f'{winner[1]} You Got Gym Bag Doorprize')

# Function Input List Menu
while(True):
  list_menu=input('''
    Welcome to Powerlifting Gym! Stay Strong Fellas!

    List Menu For Strong People:
    1. Inquiry Member Data 
    2. Add Member Data
    3. Update Member Data
    4. Delete Member Data
    5. Doorprize For Member
    6. Exit Program Powerlifting Gym
    Hello Strong Man, Please Input Menu Number : ''')
  
  if(list_menu=='1'):
    inquiry_member_data()
  elif(list_menu=='2'):
    add_member_data()
  elif(list_menu=='3'):
    update_member_data()
  elif(list_menu=='4'):
    delete_member_data()
  elif(list_menu=='5'):
    doorprize_member()
  elif(list_menu=='6'):
    break         
  else :
    print('The option you entered is not valid')
    break
