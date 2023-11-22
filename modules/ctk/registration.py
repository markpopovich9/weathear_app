import modules.data_base as m_data
import customtkinter as ctk
import os 
import modules.data.values as d_value
m_data.screen.title("регістрація користувача")
m_data.width = 460
m_data.height = 645
m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.width//2}")
def registration():
    global button,name_entry,surname_entry,country_entry,place_entry
    #get бере текст який ми вказуємо у текстовому полі
    country = country_entry.get()
    place =  place_entry.get()
    name = name_entry.get()
    surname = surname_entry.get()
    m_data.cursor.execute("INSERT INTO Users (reg,name,surname,country,place) VALUES (?,?,?,?,?)",(1,name,surname,country,place))
    print(d_value.get_value(cursor=m_data.cursor,name_table="Users"))


    text1.destroy()
    button.destroy()
    name_entry.destroy()
    surname_entry.destroy()
    country_entry.destroy()
    place_entry.destroy()
    import modules.ctk.start as ctk_start
    print(name,surname,country,place)
m_data.screen.resizable(False,False)
# створюємо кнопку при натисканні на неї викликається функція registration
background = ctk.CTkButton(master=m_data.screen,width=m_data.width,height=m_data.height,text="",border_width=5,fg_color="#5DA7B1",border_color="#096C82",hover= False,corner_radius=20)
background.place(x = 0,y = 0)


font = ctk.CTkFont(family=m_data.path,size=28,weight=("bold"))
text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=380,height=55,text="реєстрація користувача",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text1.place(x = 38,y = 42)
font = ctk.CTkFont(family=m_data.path,size=22,weight=("bold"))
text2 = ctk.CTkLabel(font= font,master=m_data.screen,width=121,height=31,text="прівище:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text2.place(x = 46,y = 405)

text3 = ctk.CTkLabel(font= font, master=m_data.screen,width=87,height=31,text="ім'я:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text3.place(x = 46,y = 306)

m_data.screen.iconbitmap(os.path.abspath(__file__+"/../../../icon.ico"))

text4 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text="місто:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text4.place(x = 46,y = 207)

text5 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text="країна:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
text5.place(x = 46,y = 108)
font = ctk.CTkFont(family=m_data.path,size=18,weight=("bold"))
button = ctk.CTkButton(font= font,master=m_data.screen,width=218,height=46,text="зберигти",border_width=3,fg_color="#096C82",command=registration, border_color= "#FFFFFF",text_color="#FFFFFF",corner_radius=20,bg_color="#5DA7B1")
button.place(x = 119,y = 546)
# transparent
# background_corner_colors=(9,108,130)
#ctk.Entry - текстовое поле
name_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 200,height = 46,placeholder_text="",border_width=3,fg_color="#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
surname_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 200,height = 46,placeholder_text="",border_width=3,fg_color="#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
country_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 218,height = 46,placeholder_text="",border_width=3,fg_color="#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
place_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 218,height = 46,placeholder_text="",border_width=3,fg_color = "#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")

country_entry.place(x=38,y=150)
place_entry.place(x=38,y=249)
name_entry.place(x=38,y=348)
surname_entry.place(x=38,y=447)