import customtkinter 
import modules.data_base as m_data
#import modules.ctk.start as ctk_start 
import modules.ctk.registration as ctk_rg

#width: 179.59px
#height: 142px



import modules.data.column as d_c
import modules.data.table as d_t
import modules.data.values as d_v
d_t.create_table("Users",["id","INTEGER PRIMARY KEY"],m_data.cursor)
d_c.add_column("Users",m_data.cursor,"reg","INTEGER")
d_c.add_column("Users",m_data.cursor,"name","TEXT")
d_c.add_column("Users",m_data.cursor,"surname","TEXT")
d_c.add_column("Users",m_data.cursor,"country","TEXT")
d_c.add_column("Users",m_data.cursor,"place","TEXT")

m_data.screen.mainloop()