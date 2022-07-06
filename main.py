#!/usr/bin/env python
# coding: utf-8

# In[3]:

import PySimpleGUI as sg
import nltk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import random
import numpy as np
import pandas as pd
import os
import gc
from sklearn.model_selection import train_test_split
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings('ignore')

sg.SetOptions(button_color="green")

# In[ ]:


def main():
    
    app = tk.Tk()
    app.geometry('600x100')


    right = Frame(app,bg='black',height = 1000,width = 200,bd=10,relief=RIDGE)
    right.pack()


    name_inp = StringVar()
    password_inp = StringVar()
    def enter():
        if name_inp.get() == "1" and password_inp.get() == "1":
            app.destroy()
            second_win()
        else:
            messagebox.showinfo("Login  ","Incorrect Username or Password")
        
    def second_win():
        df = pd.read_csv("dddd.csv",encoding = "latin1", low_memory=False)
        df.dropna(inplace = True)
        secd = Tk()
        secd.geometry('600x270')
        secd.title("Chose ")
        secd.configure(background="black")
        def logout_t_t_k():
            secd.destroy()
            main()

        def things_to_do():
            secd.destroy()
            t_t_d = Tk()
            t_t_d.geometry('700x700')
            t_t_d.title("things_to_do ")
            def back_t_t_k():
                t_t_d.destroy()
                second_win()
            def Reset():
                cmb.set("")
                comboExample2.set("")
                txtReceipt.delete("1.0",END)


            def get_place():
                df = pd.read_csv("dddd.csv",encoding = "latin1", low_memory=False)
                df.dropna(inplace = True)
                pla = df.loc[(df["Name of City"] == cmb.get())& (df.Cat1 == comboExample2.get()),["Place"]]
                txtReceipt.delete(0.0,"end")
                if pla.empty:
                    messagebox.showinfo("No Place","Sorry this type of category not exists in data ")
                else:
                    for i in pla['Place'].values:
                        
                        txtReceipt.insert("end",f"\n{i}")
                        txtReceipt.see(END)


            Top_t= Frame(t_t_d,width=700,height =100,bd = 5, bg='black',relief = RIDGE)
            Top_t.pack(side=TOP)
            Center_t= Frame(t_t_d,width=700,height =100,bd = 5, bg='black',relief = RIDGE)
            Center_t.pack(side=TOP)
            Bot_t= Frame(t_t_d,width=700,height =500,bd = 5, bg='black',relief = RIDGE)
            Bot_t.pack(side=TOP)

            t_=Label(Top_t,bg='black',fg='white', text="        Welcome To Place Recommendation Engine        ",font=("bold", 20))
            t_.pack()
            btnchs=Button(Center_t,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='Chosse State Below ',bg='black').grid(row=0,column=0)
            btnchc=Button(Center_t,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='chosse Category Blow',bg='black').grid(row=0,column=1)
            btnrst=Button(Center_t,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='Reset',command=Reset,bg='black').grid(row=0,column=2)
            btnext=Button(Center_t,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='Back',bg='black',command=back_t_t_k).grid(row=0,column=3) 
            city = []
            for i in df["Name of City"].unique():
                city.append(i)
            cmb = ttk.Combobox(Center_t, width="23", values=city)
            class TableDropDown(ttk.Combobox):
                def __init__(self, parent):
                    self.current_table = tk.StringVar() # create variable for table
                    ttk.Combobox.__init__(self, parent)#  init widget
                    self.config(textvariable = self.current_table,values = city)
                    #self.current(0) # index of values for current table
                    self.place(x = 500, y = 500, anchor = "w") # place drop down box 
                    #print(cmb.get())
            cmb.grid(row = 2, column = 0)

            d  = []
            #dd = df.loc[(df["Name of City"] == cmb.get()),["Cat1"]]
            for i  in df["Cat1"].unique():
                d.append(i)
                #print(d)
            comboExample2 = ttk.Combobox(Center_t,values=d, width="23")
            class TableDropDown(ttk.Combobox):
                def __init__(self, parent):
                    self.current_table = tk.StringVar() # create variable for table
                    ttk.Combobox.__init__(self, parent)#  init widget
                    self.config(textvariable = self.current_table,values = city)
                    #self.current(0) # index of values for current table
                    self.place(x = 500, y = 500, anchor = "w") # place drop down box 
            comboExample2.grid(row = 2,column = 1)
            
            def t_t_kLogout():
                t_t_d.destroy()
                main()


            btngtplc=Button(Center_t,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='Get Place',command=get_place,bg='black').grid(row=2,column=2)
            btnbck=Button(Center_t,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='Logout',command=t_t_kLogout,bg='black').grid(row=2,column=3)
            txtReceipt=scrolledtext.ScrolledText(Bot_t,width=74,height=29,bg='White',fg="black",bd=4,font=('arial',12,'bold'))
            txtReceipt.grid(row=0,column=0)
            t_t_d.resizable(False,False)
            t_t_d.mainloop()


        def thrdwin():
            secd.destroy()
            root = Tk()
            root.geometry('1000x600')
            root.title("Recommand win ")
            df = pd.read_csv("dddd.csv",encoding = "latin1", low_memory=False)
            df.dropna(inplace = True)
            root.configure(background="black")
            #var = StringVar()

            

            def Recommend():
                txtReceip3.delete(0.0,"end")
                try: 
                    ratings_df = pd.read_csv("ratings_small.csv", low_memory=False)
                    links_df = pd.read_csv("link_small.csv", low_memory=False)
                    place_metadata_df = pd.read_csv("dddd.csv",encoding = "latin1", low_memory=False)
                    credits_df = pd.read_csv("credits.csv", low_memory=False)


                    place_metadata_df = place_metadata_df.loc[(place_metadata_df['Name of City'] == comboExample3.get()),:]
                    place_metadata_df.dropna(inplace = True)
                    def get_list(x, l=5):
                        if isinstance(x, list):
                            names = [i['name'] for i in x]
                        #Check if more than l elements exist. If yes, return only first three. If no, return entire list.
                            if len(names) > l:
                                names = names[:l]
                            return names

                    #Return empty list in case of missing/malformed data
                        return []
                    

                    place_metadata_df['genres'] = place_metadata_df['genres'].apply(literal_eval)
                    place_metadata_df['genres'] = place_metadata_df['genres'].apply(get_list)
                    tmp = ratings_df.groupby(['placeId'])['rating'].mean()
                    R = pd.DataFrame({'id':tmp.index, 'R': tmp.values})
                    tmp = ratings_df.groupby(['placeId'])['rating'].count()
                    v = pd.DataFrame({'id':tmp.index, 'v': tmp.values})
                    C = ratings_df['rating'].mean()
                    m_df = place_metadata_df.merge(R, on=['id'])
                    m_df = m_df.merge(v, on=['id'])
                    m_df['C'] = C
                    m= m_df['v'].quantile(0.9)
                    m_df['m'] = m
                    m_df['Main_score']=(m_df['v']/(m_df['v']+m_df['m']))*m_df['R']+(m_df['m']/(m_df['v']+m_df['m']))*m_df['C']
                    m_df['R_x_v'] = m_df['R'] * m_df['v']
                    m_df[['Place','R_x_v']].sort_values(by=['R_x_v'], ascending=False)
                    del tmp
                    gc.collect()

                    tfidf = TfidfVectorizer(stop_words='english',max_features=10000)
                    tokens = m_df[['Place']]
                    tokens['Place'] = tokens['Place'].fillna('')
                    tfidf_matrix = tfidf.fit_transform(tokens['Place'])
                    from sklearn.metrics.pairwise import linear_kernel
                    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
                    indices = pd.Series(tokens.index, index=tokens['Place']).drop_duplicates()
                    def get_recommendations(title, cosine_sim=cosine_sim):
                        idx = indices[title]
                       
                    # similarity scores of all place with that place
                        sim_scores = list(enumerate(cosine_sim[idx]))

                    # sort the places based on the similarity scores
                        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

                    # scores of the 10 most similar places
                        sim_scores = sim_scores[1:11]

                    # place indices
                        place_indices = [i[0] for i in sim_scores]

                    # top 10 most similar place

                        return tokens['Place'].iloc[place_indices]

                    va = get_recommendations(varr.get())
                    
                    for i in va.values:
                        txtReceip3.insert('end',f"\n{i}")
                        
                except ValueError:
                    messagebox.showinfo("ac "," visit another city")
                except KeyError:
                    messagebox.showinfo("No Recommendations yet ", "visit another city")

            def Top_Place():
                txtReceip.delete(0.0,"end")
                ratings_df = pd.read_csv("ratings_small.csv", low_memory=False)
                links_df = pd.read_csv("link_small.csv", low_memory=False)
                place_metadata_df = pd.read_csv("dddd.csv",encoding = "latin1", low_memory=False)
                credits_df = pd.read_csv("credits.csv", low_memory=False)


                place_metadata_df = place_metadata_df.loc[(place_metadata_df['Name of City'] == comboExample3.get()),:]
                place_metadata_df.dropna(inplace = True)
                def get_list(x, l=5):
                    if isinstance(x, list):
                        names = [i['name'] for i in x]
                        #Check if more than l elements exist. If yes, return only first three. If no, return entire list.
                        if len(names) > l:
                            names = names[:l]
                        return names

                #Return empty list in case of missing/malformed data
                    return []

                place_metadata_df['genres'] = place_metadata_df['genres'].apply(literal_eval)
                place_metadata_df['genres'] = place_metadata_df['genres'].apply(get_list)
                tmp = ratings_df.groupby(['placeId'])['rating'].mean()
                R = pd.DataFrame({'id':tmp.index, 'R': tmp.values})
                tmp = ratings_df.groupby(['placeId'])['rating'].count()
                v = pd.DataFrame({'id':tmp.index, 'v': tmp.values})
                C = ratings_df['rating'].mean()
                m_df = place_metadata_df.merge(R, on=['id'])
                m_df = m_df.merge(v, on=['id'])
                m_df['C'] = C
                m= m_df['v'].quantile(0.9)
                m_df['m'] = m
                m_df['Main_score'] = (m_df['v'] / (m_df['v'] + m_df['m'])) * m_df['R'] + (m_df['m'] / (m_df['v'] + m_df['m'])) * m_df['C']
                m_df['R_x_v'] = m_df['R'] * m_df['v']
                m_df[['Place','R_x_v']].sort_values(by=['R_x_v'], ascending=False)
                ma = m_df.loc[(m_df["Name of City"] == comboExample3.get()) & (m_df["R_x_v"] >= 3.5),["Place"]]
                for i in ma['Place'].values:
                    #txtReceip.insert(END,ma)
                    txtReceip.insert(END,f"\n{i}")
                    txtReceip.see(END)


            def reset3():
                varr.set("")
                txtReceip3.delete("1.0",END)
            def Logout_trd():
                root.destroy()
                main()
                

            Top_= Frame(root,width=1000,height =50,bd = 5, bg='black')
            Top_.pack(side=TOP)

            Top_R= Frame(root,width=1000,height =50,bd = 5, bg='black',relief = RIDGE)
            Top_R.pack(side=TOP)
            
            Left_R= Frame(root,width=500,height =500,bd = 5, bg='black',relief = RIDGE)
            Left_R.pack(side=RIGHT)
            Right_R= Frame(root,width=500,height =500,bd = 5, bg='black',relief = RIDGE)
            Right_R.pack(side=LEFT)

            lblTitle=Label(Top_,font=('arial',16,'bold'),text='Place Recommendation System    \t\t\t     ',
                               bg = "black",fg='white')
            lblTitle.pack(side=LEFT)
            Logout_trd=Button(Top_,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold')
                                ,width=26,text='Logout',command=Logout_trd,bg='black').pack(side=RIGHT)

            btnchosseplc=Button(Top_R,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold')
                                ,width=26,text='Chosse Place to visit :',bg='black').grid(row=0,column=2)
            btnrecomd=Button(Top_R,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold')
                             ,width=26,text="Recommendation",command =Recommend,bg='black').grid(row=1,column=2)
            varr = tk.StringVar(Top_R)

            e1 =Entry(Top_R,width=37,bd=7,bg='white',textvariable=varr).grid(row = 0, column = 3)
            

            btnrecomd=Button(Top_R,padx=20,pady=1,bd=7,fg='white',font=('arial',8,'bold')
                             ,width=26,text="Reset",command=reset3,bg='black').grid(row=1,column=3)


            Total=Button(Top_R,padx=58,pady=1,bd=6,fg='white',font=('arial',8,'bold'),width=16,text='Choose city to visit: ',
                         bg='black').grid(row=0,column=0)
            btnReceipt=Button(Top_R,padx=58,pady=1,bd=6,fg='white',font=('arial',8,'bold'),width=16,text='Top Place',
                              command=Top_Place,bg='black').grid(row=0,column=1)

            #ecmd=Button(F,padx=58,pady=1,bd=6,fg='#5BC8AC',font=('arial',8,'bold'),width=1,text='Get Recommend',
                        #bg='#004445').grid(row=2,column=0)
            city = []
            for i in df["Name of City"].unique():
                city.append(i)

            comboExample3 = ttk.Combobox(Top_R,values=city, width="35")
            class TableDropDown(ttk.Combobox):
                def __init__(self, parent):
                    self.current_table = tk.StringVar() # create variable for table
                    ttk.Combobox.__init__(self, parent)#  init widget  
                    self.config(textvariable = self.current_table,values = city)
                    #self.current(0) # index of values for current table
                    self.place(x = 500, y = 500, anchor = "w") # place drop down box 
            comboExample3.grid(row=1,column=0)

            def Reset1():
                comboExample3.set("")
                txtReceip.delete("1.0",END)


            btnReset=Button(Top_R,padx=58,pady=1,bd=7,fg='white',font=('arial',8,'bold'),width=16,text='Reset', 
                            bg='black',command=Reset1).grid(row=1,column=1)


            txtReceip3=scrolledtext.ScrolledText(Left_R,width=51,height=25,bg='white',fg="black",bd=4,font=('arial',12,'bold'))
            txtReceip3.pack(side =TOP)


            txtReceip=scrolledtext.ScrolledText(Right_R,width=52,height=24,bg='white',fg="black",bd=4,font=('arial',12,'bold'))
            txtReceip.grid(row=0,column=0)

            root.resizable(False,False)
            root.mainloop()


        canvas = Frame(secd,width=600,height = 70,bd = 5, bg='black',relief = RIDGE)
        canvas.pack(side = TOP)
        canvas2 = Frame(secd,width=600,height = 200,bd = 5, bg='black',relief = RIDGE)
        canvas2.pack(side = BOTTOM)
        l = Label(canvas,bg='black',fg='white' , width= 50,text="Make your choice",font=("bold", 50))
        l.pack()
        l2 = Label(canvas2,bg='black',fg='white' , width= 36,text="Click Below",font=("bold", 21))
        l2.place(x= 3 , y = 16)
        b1 = Button(canvas2,bg='black',fg='white' ,bd = 5,command = things_to_do,
                    relief=RIDGE,height=2 ,width=14,text="Things To Do",font=("bold", 18))
        b1.place(x =2, y =90)
        b2= Button(canvas2,bg='black',fg='white' ,bd = 5,relief=RIDGE,height=2 ,
                   width=10,text="Log Out",command=logout_t_t_k,font=("bold", 18))
        b2.place(x =213, y =90)
        b2 = Button(canvas2,bg='black',fg='white' ,bd = 5,relief=RIDGE,height=2 ,command = thrdwin,
                    width=15,text="Recommendation",font=("bold", 18))
        b2.place(x =366, y =90)
        # run it ...
        secd.resizable(False,False)
        secd.mainloop()
        
            
    def destroy():
        app.destroy()
        
    label1 = Label(right, width = 21,font =('slant',10,'bold'),text="Username",relief= RIDGE)
    label1.grid(row=1) 

    label2 = Label(right,width = 21, font =('slant',10,'bold'),text="Password",relief=RIDGE)
    label2.grid(row=3)

    entry1 = Entry(right,width = 31,bd =3, textvariable = name_inp)
    entry1.grid(row=1,column=1)

    entry2 = Entry(right,width = 31,bd = 3, textvariable = password_inp,show="*")
    entry2.grid(row=3,column=1)

    enter_btn = Button(right,width=23,bd = 5, text="Exit", command= destroy,relief=RIDGE)
    enter_btn.grid(row=4, column=0)

    exit_btn = Button(right, padx= 1,bd=5, width = 26,text="Log in", command= enter,relief=RIDGE)
    exit_btn.grid(row=4,column=1)
    app.resizable(False,False)
    app.mainloop()
  

     
main()


# In[ ]:




