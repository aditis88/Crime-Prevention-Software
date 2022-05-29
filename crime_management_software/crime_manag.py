# Importing the tkinter module
from tkinter import*
from tkinter import ttk
from turtle import clear
from PIL import Image,ImageTk
import csv 
from face_recognition import*
from tkinter import messagebox as mess

criminal_dict = {}      # --------> This dictionary will store & display the criminal's information

# Creating a class
class Criminal:

    def __init__(self,root) :      # --------> A constructor
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        # variables
        self.var_case_id=StringVar()
        self.var_criminal_name=StringVar()
        self.var_criminal_no=StringVar()
        self.var_criminal_ide=StringVar()
        self.var_crime_date=StringVar()
        self.var_arrest_date=StringVar()
        self.var_criminal_nickname=StringVar()
        self.var_crime_location=StringVar()
        self.var_criminal_address=StringVar()
        self.var_criminal_gen=StringVar()
        self.var_criminal_age=StringVar()
        self.var_crime_type=StringVar()
        
        def prepare_dict():         # --------> A function
            
            with open('data.csv') as file_obj:
      
                # Create reader object by passing the file 
                # object to reader method
                reader_obj = csv.reader(file_obj)
                
                # Iterate over each row in the csv 
                # file using reader object
                for row in reader_obj:
                    
                    update_dict = {
                        row[0] : {'name':(row[1])
                                    ,'criminal_no':(row[2])
                                    ,'criminal_nickname': (row[3])
                                    ,'crime_date':(row[4])
                                    ,'arrest_date':(row[5])
                                    ,'crime_loc':(row[6])
                                    ,'criminal_add':(row[7])
                                    ,'crime_type':(row[8])
                                    ,'criminal_ide':(row[9])
                                    ,'criminal_age':(row[10])
                                    ,'criminal_gen':(row[11])
                                    
                                    }
                    }
                    criminal_dict.update(update_dict)
        
        def write_criminal_record():
            filename = "criminal_records.csv"
    
            # writing to csv file 
            with open(filename, 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the data rows 
                for k, v in criminal_dict.items():
                    # csvwriter.writerow(k)
                    lis = []
                    lis.append(k)
                    for i, l in criminal_dict[k].items():
                        # csvwriter.writerow([i, l])
                        lis.append(l)
                    csvwriter.writerow(lis)
            print(criminal_dict)
            print('\n')
        
        def add_record():      # -------------> A function which will add the criminal's record
            
            if(len(case_entry.get())==0):
                mess._show(title='Error!', message="Please Enter Case Id!!")
                return
            update_dict = {
                case_entry.get() : {'name':(criminal_name_entry.get())
                              ,'criminal_no':(criminal_no_entry.get())
                              ,'criminal_nickname': (criminal_nickname_entry.get())
                              ,'crime_date':(crime_date_entry.get())
                              ,'arrest_date':(arrest_date_entry.get())
                              ,'crime_loc':(crime_loc_entry.get())
                              ,'criminal_add':(criminal_add_entry.get())
                              ,'crime_type':(crime_type_entry.get())
                              ,'criminal_ide':(criminal_ide_entry.get())
                              ,'criminal_age':(criminal_age_entry.get())
                              ,'criminal_gen':(criminal_gen_entry.get())
                              
                              }
            }
            criminal_dict.update(update_dict)
            
            write_criminal_record()
            
            mess._show(title='Status', message="Record Updated/Saved successfully!")
            print(criminal_dict)
            print('\n')
           
            
            
            
        def Clear():    # ----------> A function which will clear the criminal's data written in entry boxes
            case_entry.delete(0,'end')
            criminal_no_entry.delete(0,'end')
            criminal_name_entry.delete(0,'end')
            criminal_nickname_entry.delete(0,'end')
            crime_date_entry.delete(0,'end')
            arrest_date_entry.delete(0,'end')
            crime_loc_entry.delete(0,'end')
            criminal_add_entry.delete(0,'end')
            crime_type_entry.delete(0,'end')
            criminal_ide_entry.delete(0,'end')
            criminal_age_entry.delete(0,'end')
            criminal_gen_entry.delete(0,'end')
            
        
        def delete():    # ----------> A function which will delete the criminal's data
            key= case_entry.get()
            isPresent= criminal_dict.get(key)
            if( isPresent == None):
                mess._show(title='Delete Error!', message="Record Not Found!")
                return
            criminal_dict.pop(key)
            write_criminal_record()
            mess._show(title='Status', message="Record Deleted successfully!")
            
            
        prepare_dict()    # --------> Calling this function to read the criminal's data
        
        # Naming
        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        # ncr logo

        img_logo=Image.open('Images/ncrlogo.png')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)

        # image framing

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        # Image1

        img1=Image.open('Images/police1.png')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        # Image2

        img2=Image.open('Images/police2.png')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        # Image3

        img3=Image.open('Images/police3.png')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1080,y=0,width=540,height=160)

        # Main frame (starts after the image frame)
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=200,width=1500,height=560)

        # # Upper frame (inside the main frame)
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),bg='white',fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels Entry (inside the upper frame)
        #  Case ID
        case_id=Label(upper_frame,text='Case ID',font=('times new roman',11,'bold'),bg='white')
        case_id.grid(row=0,column=0,padx=2,sticky=W)

        case_entry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('times new roman',11,'bold'))
        case_entry.grid(row=0,column=1,padx=2,sticky=W)

        #  Criminal Number 
        criminal_no=Label(upper_frame,text='Criminal No.',font=('times new roman',11,'bold'),bg='white')
        criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        criminal_no_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('times new roman',11,'bold'))
        criminal_no_entry.grid(row=0,column=3,padx=2,pady=7)

        #  Criminal Name
        criminal_name=Label(upper_frame,text='Criminal Name',font=('times new roman',11,'bold'),bg='white')
        criminal_name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        criminal_name_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_name,width=22,font=('times new roman',11,'bold'))
        criminal_name_entry.grid(row=1,column=1,padx=2,sticky=W,pady=7)

        #  Criminal Nickname
        criminal_nickname=Label(upper_frame,text='Criminal Nickname',font=('times new roman',11,'bold'),bg='white')
        criminal_nickname.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        criminal_nickname_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_nickname,width=22,font=('times new roman',11,'bold'))
        criminal_nickname_entry.grid(row=1,column=3,padx=2,sticky=W,pady=7)

        #  Crime Date
        crime_date=Label(upper_frame,text='Crime Date',font=('times new roman',11,'bold'),bg='white')
        crime_date.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        crime_date_entry=ttk.Entry(upper_frame,textvariable=self.var_crime_date,width=22,font=('times new roman',11,'bold'))
        crime_date_entry.grid(row=2,column=1,padx=2,sticky=W,pady=7)

        #  Arrest Date
        arrest_date=Label(upper_frame,text='Arrest Date',font=('times new roman',11,'bold'),bg='white')
        arrest_date.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        arrest_date_entry=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('times new roman',11,'bold'))
        arrest_date_entry.grid(row=2,column=3,padx=2,sticky=W,pady=7)

        #  Crime Location
        crime_loc=Label(upper_frame,text='Crime Location',font=('times new roman',11,'bold'),bg='white')
        crime_loc.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        crime_loc_entry=ttk.Entry(upper_frame,textvariable=self.var_crime_location,width=22,font=('times new roman',11,'bold'))
        crime_loc_entry.grid(row=3,column=1,padx=2,sticky=W,pady=7)

        #  Criminal Address
        criminal_add=Label(upper_frame,text='Criminal Address',font=('times new roman',11,'bold'),bg='white')
        criminal_add.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        criminal_add_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_address,width=22,font=('times new roman',11,'bold'))
        criminal_add_entry.grid(row=3,column=3,padx=2,sticky=W,pady=7)

        #  Crime Type
        crime_type=Label(upper_frame,text='Crime Type',font=('times new roman',11,'bold'),bg='white')
        crime_type.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        crime_type_entry=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('times new roman',11,'bold'))
        crime_type_entry.grid(row=0,column=5,padx=2,sticky=W,pady=7)

        #  Criminal Identification
        criminal_ide=Label(upper_frame,text='Criminal Identification',font=('times new roman',11,'bold'),bg='white')
        criminal_ide.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        criminal_ide_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_ide,width=22,font=('times new roman',11,'bold'))
        criminal_ide_entry.grid(row=1,column=5,padx=2,sticky=W,pady=7)

        #  Criminal Age
        criminal_age=Label(upper_frame,text='Criminal Age',font=('times new roman',11,'bold'),bg='white')
        criminal_age.grid(row=2,column=4,padx=2,sticky=W,pady=7)

        criminal_age_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_age,width=22,font=('times new roman',11,'bold'))
        criminal_age_entry.grid(row=2,column=5,padx=2,sticky=W,pady=7)

        #  Criminal Gender
        criminal_gen=Label(upper_frame,text='Criminal Gender',font=('times new roman',11,'bold'),bg='white')
        criminal_gen.grid(row=3,column=4,padx=2,sticky=W,pady=7)

        criminal_gen_entry=ttk.Entry(upper_frame,textvariable=self.var_criminal_gen,width=22,font=('times new roman',11,'bold'))
        criminal_gen_entry.grid(row=3,column=5,padx=2,sticky=W,pady=7)

        # Buttons (inside the upper frame)
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        # Add button

        button_add=Button(button_frame,text='Record Save',command=add_record,font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        button_add.grid(row=0,column=0,padx=2,sticky=W,pady=7)

        # Update button

        button_up=Button(button_frame,text='Update',command=add_record,font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        button_up.grid(row=0,column=1,padx=2,sticky=W,pady=7)

        # Clear button

        button_clr=Button(button_frame,text='Clear',command= Clear,font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        button_clr.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        # Delete button

        button_del=Button(button_frame,text='Delete',command= delete,font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        button_del.grid(row=0,column=3,padx=2,sticky=W,pady=7)

        # Criminal image

        img4=Image.open('Images/criminal.png')
        img4=img4.resize((470,245),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=0,width=470,height=245)
        
        def reset_img():
            img4=Image.open('Images/criminal.png')
            img4=img4.resize((470,245),Image.ANTIALIAS)
            self.photo4=ImageTk.PhotoImage(img4)
            self.criminal_table.item(0, values=(f'',f'',f'',f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''))
            self.criminal_table.pack(fill=BOTH,expand=1)

            self.img_4=Label(upper_frame,image=self.photo4)
            self.img_4.place(x=1000,y=0,width=470,height=245)
        
        def criminal_img():  # -------> A function which will place the criminal's image on the GUI interface
            img4=Image.open('criminal.jpg')
            img4=img4.resize((470,245),Image.ANTIALIAS)
            self.photo4=ImageTk.PhotoImage(img4)

            self.img_4=Label(upper_frame,image=self.photo4)
            self.img_4.place(x=1000,y=0,width=470,height=245)

        def take_image_test():   # -------> A function which is used to test and detect the images from the images present in the charac folder
            crim_id=  image_test()
            criminal_img()
            criminal_details(crim_id)
            
            
        def take_vid_test():     # -----> A function through which front camera will be switched on and then will take images and then detect
            crim_id= vid_test()
            criminal_img()
            criminal_details(crim_id)
            
        # # Down frame (inside the main frame)
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),bg='white',fg='red')
        down_frame.place(x=10,y=335,width=1480,height=200)

       
        
        # Test frame (below the upper frame)

        test_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        test_frame.place(x=1023,y=490,width=475,height=48)
        
        # test on saved images
        test_imgs=Button(test_frame,text='Test on\nsaved images',command=take_image_test,font=('times new roman',10,'bold'),width=18,bg='blue',fg='white')
        test_imgs.grid(row=0,column=0,padx=1,sticky=W,pady=2)
        
        # test on front camera
        test_cam=Button(test_frame,text='Test on \nfront cam',command=take_vid_test,font=('times new roman',10,'bold'),width=18,bg='blue',fg='white')
        test_cam.grid(row=0,column=1,padx=1,sticky=W,pady=2)
        
                
        # Reset imgages
        reset_but=Button(test_frame,text='Reset\n',command=reset_img,font=('times new roman',10,'bold'),width=18,bg='blue',fg='white')
        reset_but.grid(row=0,column=3,padx=1,sticky=W,pady=2)
        
        
        
        # Table frame (inside the down frame)

        table_frame=Frame(down_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=0,y=0,width=1470,height=172)
        
        # treeview functions ( a tabular representation of the data)
        def criminal_details(crim_id):   # -----> A function which will take criminal id , if the criminal id is not present , nothing will be displayed otherwise criminal's data will be displayed
            if(crim_id == -1):
                self.criminal_table.item(0, values=(f'',f'',f'',f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''
                                               ,f''))
            else:
                crime_info = criminal_dict.get(crim_id)
                # print(crime_info["criminal_no"])
                self.criminal_table.item(0, values=(f'{crim_id}',f'{crime_info["criminal_no"]}',f'{crime_info["name"]}',f'{crime_info["criminal_nickname"]}'
                                                ,f'{crime_info["crime_type"]}'
                                                ,f'{crime_info["crime_loc"]}'
                                                ,f'{crime_info["criminal_add"]}'
                                                ,f'{crime_info["criminal_age"]}'
                                                ,f'{crime_info["criminal_gen"]}'
                                                ,f'{crime_info["crime_date"]}'
                                                ,f'{crime_info["arrest_date"]}'
                                                ,f'{crime_info["criminal_ide"]}'))
            self.criminal_table.pack(fill=BOTH,expand=1)

        # Scroll bar (to scroll the horizontal & vertical axes)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        
        self.criminal_table.heading("1",text="Case ID")
        self.criminal_table.heading("2",text="Criminal No.")
        self.criminal_table.heading("3",text="Criminal Name")
        self.criminal_table.heading("4",text="Criminal Nickname")
        self.criminal_table.heading("5",text="Crime Type")
        self.criminal_table.heading("6",text="Crime Location")
        self.criminal_table.heading("7",text="Criminal Address")
        self.criminal_table.heading("8",text="Criminal Age")
        self.criminal_table.heading("9",text="Criminal Gender")
        self.criminal_table.heading("10",text="Crime Date")
        self.criminal_table.heading("11",text="Arrest Date")
        self.criminal_table.heading("12",text="Criminal Identification")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)
        self.criminal_table.column("9",width=100)
        self.criminal_table.column("10",width=100)
        self.criminal_table.column("11",width=100)
        self.criminal_table.column("12",width=100)
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.insert(parent='', index=0, iid=0, text='', values=('','',''))
        
        



if __name__=="__main__" :
    root=Tk()
    obj=Criminal(root)
    root.mainloop()