import mysql.connector as db
con=db.connect(host="localhost",user="root",password="srishti2603",database="bank")

if con.is_connected():
    print("connected")

cursor=con.cursor()

#         #CREATING DATABASE BANK   
# cursor.execute("create database bank")
# con.commit()

#        # BRANCH TABLE
# cursor.execute('''create table branches(branch_id int primary key auto_increment,
#     branch_name varchar(70) not null,
#     branch_code varchar(20) unique not null,
#     phone varchar(15),
#     address varchar(100),
#     status varchar(20) default 'active')''')
# con.commit()

#        # STAFF TABLE
# cursor.execute('''create table staff(staff_id int primary key auto_increment,
#             branch_id int not null,
#             name varchar(50) not null,
#             role varchar(30) not null,
#             username varchar(50) unique not null,
#             password varchar(25) not null,
#             status varchar(20) default'active',
#             foreign key (branch_id) references branches(branch_id))''')
# con.commit()     

#             # CUSTOMERS TABLE
# cursor.execute('''create table customers( customer_id int primary key auto_increment,
#             name varchar(70) not null,
#             dob date not null,
#             phone varchar(15) unique not null,
#             email varchar(50),
#             address varchar(100),
#             kyc_status varchar(20),
#             status varchar(20) default'active')''')   
# con.commit() 

#              # ACCOUNT TABLE
# cursor.execute('''create table accounts( account_id int primary key auto_increment,
#             customer_id int not null,
#             branch_id int not null,
#             account_no varchar(30) unique not null,
#             account_type varchar(30) not null,
#             balance decimal(15,2) default 0.00,
#             status varchar(20) default 'active',
#             opened_on date not null,
#             foreign key (customer_id) references customers(customer_id),
#             foreign key (branch_id) references branches(branch_id))''')   
# con.commit()                               

#                    # TRANSACTION TABLE
# cursor.execute('''create table transaction(transaction_id int primary key auto_increment,
#             account_id int not null,
#             staff_id int,
#             transaction_type varchar(30) not null,
#             amount decimal(15,2) not null,
#             reference_no varchar(50) unique not null,
#             transaction_time datetime,
#             foreign key (account_id) references accounts(account_id),
#             foreign key (staff_id) references staff(staff_id))''')
# con.commit()    
                            
#                   #  CASHIER SESSIONS
# cursor.execute('''create table cashier(session_id int primary key auto_increment,
#             staff_id int not null,
#             opening_cash decimal(15,2) not null,
#             total_deposits decimal(15,2) default 0.00,
#             total_withdrawals decimal(15,2) default 0.00,
#             closing_cash decimal(15,2),
#             opened_at datetime,
#             closed_at datetime,
#             status varchar(20) default'open',
#             foreign key (staff_id) references staff(staff_id))''')   
# con.commit() 
 
#             #    FIXED DEPOSIT
# cursor.execute('''create table fd_records(fd_id int primary key auto_increment,
#             customer_id int not null,
#             account_id int not null,
#             fd_type varchar(30) not null,
#             amount decimal(15,2) not null,
#             interest_rate decimal(5,2) not null,
#             start_date date not null,
#             maturity_date date not null,
#             status varchar(20) default'active',
#             foreign key (customer_id) references customers(customer_id),
#             foreign key (account_id) references accounts(account_id))''')
# con.commit() 
 
#                # AUDIT LOGS
# cursor.execute('''create table audit_logs(log_id int primary key auto_increment,
#             staff_id int,
#             customer_id int,
#             action varchar(100) not null,
#             details varchar(255),
#             timestamp datetime ,
#             foreign key (staff_id) references staff(staff_id),
#             foreign key (customer_id) references customers(customer_id))''')
# con.commit()                                                                    

#               #  INSERETED INITIAL DATA
# cursor.execute ('''insert into branches(branch_name,branch_code, phone, address) values ("shimla main branch", "SHM001", "9876500001", "mall road, shimla"),
#     ("chandigarh branch", "CHD001", "9876500002", "sector 17, chandigarh"),
#     ("delhi branch", "DEL001", "9876500003", "connaught place, delhi"),
#     ("mumbai branch", "MUM001", "9876500004", "andheri, mumbai"),
#     ("bangalore branch", "BLR001", "9876500005", "mg road, bangalore"),
#     ("kolkata branch", "KOL001", "9876500006", "salt lake, kolkata"),
#     ("pune branch", "PUN001", "9876500007", "shivaji nagar, pune"),
#     ("jaipur branch", "JPR001", "9876500008", "tonk road, jaipur"),
#     ("lucknow branch", "LKO001", "9876500009", "hazratganj, lucknow"),
#     ("dehradun branch", "DDN001", "9876500010", "rajpur road, dehradun"),
#     ("amritsar branch", "ASR001", "9876500011", "mall road, amritsar"),
#     ("manali branch", "MNL001", "9876500012", "mall road, manali"),
#     ("gurgaon branch", "GGN001", "9876500013", "mg road, gurgaon"),
#     ("noida branch", "NOI001", "9876500014", "sector 18, noida"),
#     ("hyderabad branch", "HYD001", "9876500015", "banjara hills, hyderabad");''')      
# con.commit() 

#                     #FOR STAFF
# cursor.execute('''insert into staff( branch_id, name, role, username, password) values(1,"rahul sharma", "branch_manager",
#          "manager01", "manager123"),

#         (2, "neha thakur", "branch_manager",
#          "manager02", "manager456"),

#         (11, "aman verma", "branch_manager",
#          "manager03", "manager789"),

#         (4, "rohit kumar", "branch_manager",
#          "manager04", "manager321"),

#         (1, "pooja sharma", "cashier",
#          "cashier01", "cashier123"),

#         (9, "karan singh", "cashier",
#          "cashier02", "cashier456"),

#         (3, "simran kaur", "cashier",
#          "cashier03", "cashier789"),

#         (4, "vikas mehta", "cashier",
#          "cashier04", "cashier321"),

#         (15, "ravi kumar", "fd_manager",
#          "fdmanager01", "fd123"),

#         (6, "neha verma", "fd_manager",
#          "fdmanager02", "fd456"),

#         (7, "arjun kapoor", "fd_manager",
#          "fdmanager03", "fd789"),

#         (12, "megha sharma", "fd_manager",
#          "fdmanager04", "fd321");''') 
# con.commit()                        

#            #   FOR CUSTOMERS
# cursor.execute('''insert into customers(name, dob, phone, email, address, kyc_status ) values  ("srishti thakur", "2006-03-26", "9000000001",
#          "srishti@gmail.com", "shimla", "verified"),

#         ("priya sharma", "2002-08-20", "9000000002",
#          "priya@gmail.com", "chandigarh", "verified"),

#         ("ankit verma", "2001-11-10", "9000000003",
#          "ankit@gmail.com", "delhi",null),

#         ("rohan singh", "2000-04-12", "9000000004",
#          "rohan@gmail.com", "mumbai", "verified"),

#         ("neha kapoor", "2003-09-25", "9000000005",
#          "neha@gmail.com", "bangalore", "verified"),

#         ("aditya sharma", "1999-06-18", "9000000006",
#          "aditya@gmail.com", "kolkata", "verified"),

#         ("simran kaur", "2002-01-30", "9000000007",
#          "simran@gmail.com", "pune", "verified"),

#         ("rahul mehta", "2001-07-14", "9000000008",
#          "rahul@gmail.com", "jaipur", "not verified"),

#         ("pooja verma", "2003-03-22", "9000000009",
#          "pooja@gmail.com", "lucknow", "verified"),

#         ("karan singh", "1998-12-05", "9000000010",
#          "karan@gmail.com", "dehradun", "verified"),

#         ("megha thakur", "2002-10-17", "9000000011",
#          "megha@gmail.com", "shimla",null),

#         ("vikas kumar", "2000-02-11", "9000000012",
#          "vikas@gmail.com", "amritsar", "verified"),

#         ("ravi sharma", "1999-05-09", "9000000013",
#          "ravi@gmail.com", "manali", "verified"),

#         ("aarti singh", "2003-11-21", "9000000014",
#          "aarti@gmail.com", "gurgaon", "verified"),

#         ("manish verma", "1997-08-16", "9000000015",
#          "manish@gmail.com", "noida", "not verified"),

#         ("kavita sharma", "2001-03-19", "9000000016",
#          "kavita@gmail.com", "hyderabad", "verified"),

#         ("rohit thakur", "1998-09-27", "9000000017",
#          "rohit@gmail.com", "shimla", "verified"),

#         ("divya kapoor", "2002-06-13", "9000000018",
#          "divya@gmail.com", "chandigarh", "verified"),

#         ("mohit sharma", "2000-10-08", "9000000019",
#          "mohit@gmail.com", "delhi", "verified"),

#         ("isha verma", "2003-12-01", "9000000020",
#          "isha@gmail.com", "mumbai", "verified"),

#         ("sahil kumar", "1999-04-26", "9000000021",
#          "sahil@gmail.com", "bangalore", "verified"),

#         ("tanvi sharma", "2002-07-05", "9000000022",
#          "tanvi@gmail.com", "kolkata", "verified"),

#         ("nikhil singh", "1998-11-18", "9000000023",
#          "nikhil@gmail.com", "pune", "verified"),

#         ("riya thakur", "2001-01-23", "9000000024",
#          "riya@gmail.com", "jaipur", "verified"),

#         ("deepak verma", "1997-05-15", "9000000025",
#          "deepak@gmail.com", "lucknow", "verified"),

#         ("sonam sharma", "2000-09-11", "9000000026",
#          "sonam@gmail.com", "dehradun", "verified"),

#         ("abhishek singh", "1999-02-28", "9000000027",
#          "abhishek@gmail.com", "amritsar", "verified"),

#         ("preeti kumar", "2002-04-07", "9000000028",
#          "preeti@gmail.com", "manali", "verified"),

#         ("yash kapoor", "2001-08-30", "9000000029",
#          "yash@gmail.com", "gurgaon", "verified"),

#         ("nisha verma", "2003-10-12", "9000000030",
#          "nisha@gmail.com", "noida", "verified"),

#         ("varun sharma", "1998-06-24", "9000000031",
#          "varun@gmail.com", "hyderabad", "not verified"),

#         ("muskan thakur", "2002-02-14", "9000000032",
#          "muskan@gmail.com", "shimla", "verified"),

#         ("akash kumar", "2000-07-29", "9000000033",
#          "akash@gmail.com", "chandigarh", "verified"),

#         ("shreya singh", "2001-11-03", "9000000034",
#          "shreya@gmail.com", "delhi", "verified"),

#         ("vivek verma", "1997-12-19", "9000000035",
#          "vivek@gmail.com", "mumbai", "verified"),

#         ("ananya sharma", "2003-05-28", "9000000036",
#          "ananya@gmail.com", "bangalore", "not verified"),

#         ("tarun kapoor", "1999-09-06", "9000000037",
#          "tarun@gmail.com", "kolkata", "verified"),

#         ("komal sharma", "2002-03-16", "9000000038",
#          "komal@gmail.com", "pune", "verified"),

#         ("varsha singh", "2000-08-22", "9000000039",
#          "varsha@gmail.com", "jaipur", "verified"),

#         ("sumit kumar", "1998-01-10", "9000000040",
#          "sumit@gmail.com", "lucknow", "verified"),

#         ("payal verma", "2001-06-05", "9000000041",
#          "payal@gmail.com", "dehradun", "verified"),

#         ("aman sharma", "1999-10-20", "9000000042",
#          "aman@gmail.com", "amritsar", "verified"),

#         ("rakesh singh", "1997-04-15", "9000000043",
#          "rakesh@gmail.com", "manali", "verified"),

#         ("sakshi thakur", "2003-07-18", "9000000044",
#          "sakshi@gmail.com", "gurgaon",null),

#         ("harsh verma", "2000-12-09", "9000000045",
#          "harsh@gmail.com", "noida", "verified"),

#         ("monika sharma", "2002-05-31", "9000000046",
#          "monika@gmail.com", "hyderabad", "verified"),

#         ("gaurav kumar", "1998-08-12", "9000000047",
#          "gaurav@gmail.com", "shimla", "verified"),

#         ("nikita singh", "2001-02-25", "9000000048",
#          "nikita@gmail.com", "chandigarh", "verified"),

#         ("sachin verma", "1999-11-17", "9000000049",
#          "sachin@gmail.com", "delhi", "verified"),

#         ("meena sharma", "2003-09-03", "9000000050",
#          "meena@gmail.com", "mumbai", "verified"); ''')      
# con.commit()   
 
#                      # FOR ACCOUNTS
# cursor.execute('''insert into accounts (customer_id, branch_id, account_no, account_type, balance, opened_on) values
# (1, 8, 'ACC1001', 'Savings', 25000.00, '2020-01-01'),
# (2, 1, 'ACC1002', 'Savings', 18000.00, '2020-02-01'),
# (3, 1, 'ACC1003', 'Current', 32000.00, '2020-03-01'),
# (4, 1, 'ACC1004', 'Savings', 15000.00, '2020-04-01'),
# (5, 1, 'ACC1005', 'Savings', 28000.00, '2020-05-01'),
# (6, 11, 'ACC1006', 'Current', 22000.00, '2020-06-01'),
# (7, 11, 'ACC1007', 'Savings', 19500.00, '2020-07-01'),
# (8, 1, 'ACC1008', 'Savings', 30500.00, '2020-08-01'),
# (9, 1, 'ACC1009', 'Current', 27000.00, '2020-09-01'),
# (10, 1, 'ACC1010', 'Savings', 21000.00, '2020-10-01'),
# (11, 2, 'ACC1011', 'Savings', 26000.00, '2020-11-01'),
# (12, 2, 'ACC1012', 'Current', 18000.00, '2020-12-01'),
# (13, 10, 'ACC1013', 'Savings', 34000.00, '2021-01-01'),
# (14, 10, 'ACC1014', 'Savings', 15500.00, '2021-02-01'),
# (15, 2, 'ACC1015', 'Current', 29000.00, '2021-03-01'),
# (16, 2, 'ACC1016', 'Savings', 31000.00, '2021-04-01'),
# (17, 3, 'ACC1017', 'Savings', 20000.00, '2021-05-01'),
# (18, 3, 'ACC1018', 'Current', 27500.00, '2021-06-01'),
# (19, 3, 'ACC1019', 'Savings', 15000.00, '2021-07-01'),
# (20, 3, 'ACC1020', 'Savings', 33000.00, '2021-08-01'),
# (21, 3, 'ACC1021', 'Savings', 24000.00, '2021-09-01'),
# (22, 3, 'ACC1022', 'Current', 18500.00, '2021-10-01'),
# (23, 3, 'ACC1023', 'Savings', 29500.00, '2021-11-01'),
# (24, 3, 'ACC1024', 'Savings', 21000.00, '2021-12-01'),
# (25, 4, 'ACC1025', 'Current', 25000.00, '2022-01-01'),
# (26, 4, 'ACC1026', 'Savings', 27000.00, '2022-02-01'),
# (27, 4, 'ACC1027', 'Savings', 19000.00, '2022-03-01'),
# (28, 4, 'ACC1028', 'Current', 31000.00, '2022-04-01'),
# (29, 4, 'ACC1029', 'Savings', 22000.00, '2022-05-01'),
# (30, 4, 'ACC1030', 'Savings', 28000.00, '2022-06-01'),
# (31, 4, 'ACC1031', 'Current', 26000.00, '2022-07-01'),
# (32, 4, 'ACC1032', 'Savings', 30000.00, '2022-08-01'),
# (33, 4, 'ACC1033', 'Savings', 21000.00, '2022-09-01'),
# (34, 4, 'ACC1034', 'Current', 27000.00, '2022-10-01'),
# (35, 5, 'ACC1035', 'Savings', 25000.00, '2022-11-01'),
# (36, 5, 'ACC1036', 'Savings', 32000.00, '2022-12-01'),
# (37, 5, 'ACC1037', 'Current', 20000.00, '2023-01-01'),
# (38, 5, 'ACC1038', 'Savings', 28000.00, '2023-02-01'),
# (39, 5, 'ACC1039', 'Savings', 31000.00, '2023-03-01'),
# (40, 5, 'ACC1040', 'Current', 23000.00, '2023-04-01'),
# (41, 5, 'ACC1041', 'Savings', 26000.00, '2023-05-01'),
# (42, 5, 'ACC1042', 'Savings', 29000.00, '2023-06-01'),
# (43, 6, 'ACC1043', 'Current', 21000.00, '2023-07-01'),
# (44, 6, 'ACC1044', 'Savings', 27000.00, '2023-08-01'),
# (45, 6, 'ACC1045', 'Savings', 30000.00, '2023-09-01'),
# (46, 12, 'ACC1046', 'Current', 22000.00, '2023-10-01'),
# (47, 12, 'ACC1047', 'Savings', 25000.00, '2023-11-01'),
# (48, 15, 'ACC1048', 'Savings', 28000.00, '2023-12-01'),
# (49, 15, 'ACC1049', 'Current', 24000.00, '2024-01-01'),
# (50, 15, 'ACC1050','Savings', 30000.00, '2024-02-01');''')
# con.commit()

#                         # FOR TRANSACTION 
# cursor.execute('''insert into transaction(account_id, staff_id, transaction_type, amount, transaction_time, reference_no) values
# ( 1, 2, 'Deposit', 5000.00, '2021-01-10 10:30:00', 'TXN001'),
# ( 2, 3, 'Withdrawal', 2000.00, '2021-01-12 14:20:00', 'TXN002'),
# (3, 4, 'Deposit', 7000.00, '2021-01-15 11:00:00', 'TXN003'),
# (4, 5, 'Withdrawal', 1500.00, '2021-01-18 16:45:00', 'TXN004'),
# (5, 6, 'Deposit', 10000.00, '2021-01-20 09:15:00', 'TXN005'),
# (6, 7, 'Withdrawal', 2500.00, '2021-01-22 13:30:00', 'TXN006'),
# (7, 8, 'Deposit', 8000.00, '2021-01-25 10:00:00', 'TXN007'),
# (8, 9, 'Withdrawal', 3000.00, '2021-01-27 15:45:00', 'TXN008'),
# (9, 10, 'Deposit', 6000.00, '2021-02-01 09:20:00', 'TXN009'),
# (10, 1, 'Withdrawal', 2000.00, '2021-02-03 14:10:00', 'TXN010'),
# (11, 2, 'Deposit', 7500.00, '2021-02-05 11:00:00', 'TXN011'),
# (12, 3, 'Withdrawal', 1800.00, '2021-02-07 16:00:00', 'TXN012'),
# (13, 4, 'Deposit', 9000.00, '2021-02-10 09:30:00', 'TXN013'),
# (14, 5, 'Withdrawal', 2200.00, '2021-02-12 13:40:00', 'TXN014'),
# (15, 6, 'Deposit', 5000.00, '2021-02-15 10:15:00', 'TXN015'),
# (16, 7, 'Withdrawal', 2500.00, '2021-02-17 15:25:00', 'TXN016'),
# (17, 8, 'Deposit', 7000.00, '2021-02-20 09:45:00', 'TXN017'),
# (18, 9, 'Withdrawal', 3000.00, '2021-02-22 14:55:00', 'TXN018'),
# (19, 10, 'Deposit', 6500.00, '2021-02-25 10:05:00', 'TXN019'),
# (20, 1, 'Withdrawal', 2000.00, '2021-02-27 16:15:00', 'TXN020'),
# (21, 2, 'Deposit', 7200.00, '2021-03-02 09:40:00', 'TXN021'),
# (22, 3, 'Withdrawal', 1800.00, '2021-03-04 14:30:00', 'TXN022'),
# (23, 4, 'Deposit', 9500.00, '2021-03-07 10:20:00', 'TXN023'),
# (24, 5, 'Withdrawal', 2500.00, '2021-03-09 15:10:00', 'TXN024'),
# (25, 6, 'Deposit', 11000.00, '2021-03-12 09:50:00', 'TXN025'),
# (26, 7, 'Withdrawal', 3000.00, '2021-03-14 16:00:00', 'TXN026'),
# (27, 8, 'Deposit', 8000.00, '2021-03-17 10:30:00', 'TXN027'),
# (28, 9, 'Withdrawal', 2000.00, '2021-03-19 14:45:00', 'TXN028'),
# (29, 10, 'Deposit', 9500.00, '2021-03-22 09:15:00', 'TXN029'),
# (30, 1, 'Withdrawal', 2500.00, '2021-03-24 15:25:00', 'TXN030'),
# (31, 2, 'Deposit', 6000.00, '2021-03-27 10:10:00', 'TXN031'),
# (32, 3, 'Withdrawal', 2000.00, '2021-03-29 14:40:00', 'TXN032'),
# (33, 4, 'Deposit', 7000.00, '2021-04-01 09:30:00', 'TXN033'),
# (34, 5, 'Withdrawal', 2500.00, '2021-04-03 15:00:00', 'TXN034'),
# (35, 6, 'Deposit', 8500.00, '2021-04-06 10:20:00', 'TXN035'),
# (36, 7, 'Withdrawal', 3000.00, '2021-04-08 16:10:00', 'TXN036'),
# (37, 8, 'Deposit', 9500.00, '2021-04-11 09:45:00', 'TXN037'),
# (38, 9, 'Withdrawal', 2000.00, '2021-04-13 14:50:00', 'TXN038'),
# (39, 10, 'Deposit', 10000.00, '2021-04-16 10:00:00', 'TXN039'),
# (40, 1, 'Withdrawal', 2500.00, '2021-04-18 15:30:00', 'TXN040'),
# (41, 2, 'Deposit', 7200.00, '2021-04-21 09:20:00', 'TXN041'),
# (42, 3, 'Withdrawal', 1800.00, '2021-04-23 14:15:00', 'TXN042'),
# (43, 4, 'Deposit', 9500.00, '2021-04-26 10:10:00', 'TXN043'),
# (44, 5, 'Withdrawal', 2500.00, '2021-04-28 15:05:00', 'TXN044'),
# (45, 6, 'Deposit', 11000.00, '2021-05-01 09:50:00', 'TXN045'),
# (46, 7, 'Withdrawal', 3000.00, '2021-05-03 16:00:00', 'TXN046'),
# (47, 8, 'Deposit', 8000.00, '2021-05-06 10:30:00', 'TXN047'),
# (48, 9, 'Withdrawal', 2000.00, '2021-05-08 14:40:00', 'TXN048'),
# (49, 10, 'Deposit', 9500.00, '2021-05-11 09:15:00', 'TXN049'),
# (50, 1, 'Withdrawal', 4000.00, '2021-05-13 15:20:00', 'TXN050');''')
# con.commit()

#                     # FOR CASHIER
# cursor.execute(''' insert into cashier (staff_id, opening_cash, closing_cash, opened_at, closed_at, status)
# values (1, 5000.00, 7350.50, '2026-09-01 09:00:00', '2026-09-01 18:00:00', 'Closed'),
# (2, 3000.00, 4825.75, '2026-09-01 10:00:00', '2026-09-01 19:00:00', 'Closed'),
# (3, 4500.00, 6200.00, '2026-09-02 09:30:00', '2026-09-02 17:30:00', 'Closed'),
# (1, 6000.00, 8150.25, '2026-09-02 09:00:00', '2026-09-02 18:00:00', 'Closed'),
# (4, 3500.00, 5100.50, '2026-09-03 10:00:00', '2026-09-03 18:30:00', 'Closed'),
# (2, 4000.00, 6750.00, '2026-09-03 09:00:00', '2026-09-03 18:00:00', 'Closed'),
# (3, 5500.00, 7200.75, '2026-09-04 09:30:00', '2026-09-04 17:30:00', 'Closed'),
# (4, 2500.00, 4300.25, '2026-09-04 10:00:00', '2026-09-04 19:00:00', 'Closed'),
# (1, 5000.00, NULL, '2026-09-04 09:00:00', NULL, 'Open'),
# (2, 4500.00, NULL, '2026-09-04 10:00:00', NULL, 'Open');''')

# con.commit()          

#                     # FOR FIXED DEPOSIT
# cursor.execute('''insert into fd_records(customer_id, account_id, fd_type, amount, interest_rate, start_date, maturity_date)
# values(1, 1, 'Cumulative', 85000.00, 6.50, '2026-01-05', '2027-01-05' ),
# (2, 2, 'Non-Cumulative', 120000.00, 6.75, '2026-01-12', '2027-01-12' ),
# (3, 3, 'Cumulative', 95000.00, 7.00, '2026-02-08', '2027-02-08'),
# (4, 4, 'Non-Cumulative', 150000.00, 7.25, '2026-02-20', '2027-02-20'),
# (5, 5, 'Cumulative', 70000.00, 6.25, '2026-03-10', '2027-03-10'),
# (6, 6, 'Non-Cumulative', 110000.00, 6.50, '2026-03-18', '2027-03-18'),
# (7, 7, 'Cumulative', 180000.00, 7.00, '2026-04-02', '2027-04-02'),
# (8, 8, 'Non-Cumulative', 60000.00, 6.75, '2026-04-15', '2027-04-15'),
# (9, 9, 'Cumulative', 135000.00, 7.25, '2026-05-05', '2027-05-05'),
# (10, 10, 'Non-Cumulative', 90000.00, 6.50, '2026-05-22', '2027-05-22');''')
# con.commit()

#                         # FOR AUDIT LOGS
# cursor.execute('''insert into audit_logs(staff_id, customer_id, action, details, timestamp)
# values(1, 1, 'Login', 'Staff logged into the banking system', '2026-09-01 09:05:00'),
# (2, 2, 'Customer Update', 'Updated customer contact information', '2026-09-01 09:20:00'),
# (3, 3, 'Account View', 'Viewed customer account details', '2026-09-01 09:45:00'),
# (4, 4, 'Deposit', 'Cash deposit processed for customer account', '2026-09-01 10:15:00'),
# (1, 5, 'Withdrawal', 'Cash withdrawal processed from customer account', '2026-09-01 10:40:00'),
# (5, 6, 'Account Creation', 'New savings account created', '2026-09-01 11:10:00'),
# (6, 7, 'KYC Verification', 'Customer KYC documents verified', '2026-09-01 11:35:00'),
# (7, 8, 'Password Change', 'Customer password was changed', '2026-09-01 12:05:00'),
# (2, 9, 'Fund Transfer', 'Funds transferred to another account', '2026-09-01 12:30:00'),
# (3, 10, 'FD Creation', 'New fixed deposit created', '2026-09-01 13:00:00'),
# (4, 11, 'FD Update', 'Fixed deposit details updated', '2026-09-01 13:25:00'),
# (1, 12, 'Account Status Change', 'Account status changed to inactive', '2026-09-01 14:00:00'),
# (5, 13, 'Deposit', 'Cheque deposit recorded in customer account', '2026-09-02 09:15:00'),
# (6, 14, 'Customer Update', 'Customer address information updated', '2026-09-02 09:45:00'),
# (7, 15, 'Withdrawal', 'ATM withdrawal transaction verified', '2026-09-02 10:20:00'),
# (8, 16, 'Account View', 'Viewed current account transaction history', '2026-09-02 10:50:00'),
# (9, 17, 'FD Creation', 'New cumulative fixed deposit created', '2026-09-02 11:25:00'),
# (10,18, 'Login', 'Staff logged into the banking system', '2026-09-02 11:50:00'),
# (2, 19, 'KYC Verification', 'Customer KYC status changed to verified', '2026-09-02 12:20:00'),
# (3, 20, 'Account Closure', 'Customer account closure request processed', '2026-09-02 13:10:00');''')                       
# con.commit()