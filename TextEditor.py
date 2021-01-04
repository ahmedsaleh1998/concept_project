from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser


root=Tk()
root.title('concept -textpade!')
root.geometry("1200x660")
global open_states_name
open_states_name=False
global selected 
selected=False

#create new file function 
def new_file():
    my_text.delete("1.0",END)
    root.title('new_file ')
    status_bar.config(text="new file     ")
    global open_states_name
open_states_name=False
#create open file function 
def open_file():
    my_text.delete("1.0",END)
    text_file=filedialog.askopenfilename(initialdir="C:/Users",title="open file",filetypes=(("Text Files","*.txt"),("Html Files","*.Html"),("css Files","*.css"),("python Files","*.py"),("all Files","*.*")))
    if text_file:
        global open_states_name
        open_states_name=text_file
    
    name=text_file
    status_bar.config(text=f'{name}   ')
    name=name.replace("C:/Users/ahmed/Desktop","")
    root.title(F'{name} -Textpad!')

    #open the file
    text_file=open(text_file,'r')
    stuff =text_file.read()
    # add file to textbox
    my_text.insert(END,stuff)
    #closed the opend file
    text_file.close()
#save as file
def save_as_file():
    global open_states_name
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="C/Users/",title="save file",filetypes=(("Text Files","*.txt"),("Html Files","*.Html"),("css Files","*.css"),("python Files","*.py"),("all Files","*.*")))
    if text_file:
        open_states_name=text_file
    	#update states bar
        name=text_file
        status_bar.config(text=f'Saved{name}   ')
        name=name.replace("C:/Users/ahmed/Desktop/","")
        root.title(f' {name} -Textpad!')
        #save the file
        text_file= open(text_file,'w')
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()
   
# save file function 
def save_file():
    global open_states_name
    if open_states_name:
          #save the file
        text_file= open(open_states_name,'w')
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()
        status_bar.config(text=f'Saved{open_states_name}   ')
    else:
        save_as_file()    
        
######################################
#copy text 
def cut_text(e):
    global selected 
    if e:
        selected=root.clipboard_get()
    else:
        if my_text.selection_get():
            #take selected text from text box
            selected = my_text.selection_get()
            #delete selected text from text box 
            my_text.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)
#####################################
#copy text 
def copy_text(e):

    global selected 
    if e:
        selected=root.clipboard_get()
    if my_text.selection_get():
        #take selected text from text box
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

#####################################
#copy text 
def paste_text(e):
   global selected
   if e:
       selected=root.clipboard_get() 
   else:
        if selected:
            position=my_text.index(INSERT)
            my_text.insert(position,selected)
#####################################
#delete text 
def delete_text ():
    global selected 
    if my_text.selection_get():
        #delete selected text from text box 
        my_text.delete("sel.first","sel.last")
###############################################

#bold it function 
def bold_it():
    #create the font
    bold_font=font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")
    #config the tag
    my_text.tag_configure("bold",font=bold_font)
    #define current tages
    current_tags=my_text.tag_names("sel.first")
    #if to remove it 
    if "bold"in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
        my_text.tag_add("bold","sel.first","sel.last")
    


#bold it function 
def italics_it():
    #create the font
    italics_font=font.Font(my_text,my_text.cget("font"))
    italics_font.configure(slant="italic")
    #config the tag
    my_text.tag_configure("italic",font=italics_font)
    #define current tages
    current_tags=my_text.tag_names("sel.first")
    #if to remove it 
    if "italic"in current_tags:
        my_text.tag_remove("italic","sel.first","sel.last")
    else:
        my_text.tag_add("italic","sel.first","sel.last")
    
#bold it function 
def undo_it():
    pass
#bold it function 
def redo_it():
    pass
################################
#build chinges text color_text_button
def text_color():
    #pick acolor
    my_color=colorchooser.askcolor()[1]
    status_bar.config(text=my_color)

    #create the font
    color_font=font.Font(my_text,my_text.cget("font"))
    
    #config the tag
    my_text.tag_configure("colord",font=color_font,foreground=my_color)
    #define current tages
    current_tags=my_text.tag_names("sel.first")
    #if to remove it 
    if "colord" in current_tags:
        my_text.tag_remove("colord","sel.first","sel.last")
    else:
        my_text.tag_add("colord","sel.first","sel.last")
##############################
#change back ground colord
def bg_color():
     my_color=colorchooser.askcolor()[1]
     if my_color:
         my_text.config(bg=my_color)

############################
#ching all text color 
def all_text_color():
    my_color=colorchooser.askcolor()[1]
    if my_color:
     my_text.config(fg=my_color)


#####################################################
#create tool bar to change the type of text 
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

        

#create main frame 
my_frame=Frame(root)
my_frame.pack(pady=5)
#create text box 
my_text=Text(my_frame,width=97,height=25,font=("Helvetica",16),selectbackground="yellow",selectforeground="black",undo=True)
my_text.pack()
#create oure scrollbar for the text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#config our scroll bar
text_scroll.config(command=my_text.yview)

#create menu 
my_menu=Menu(root)
root.config(menu=my_menu)

#add file menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save  CTRL+S  ",command=save_file)
file_menu.add_command(label="Save as  CTRL+ALT+S  ",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit    ",command=root.quit)
#add edit menu
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy  (CTRL+C)  ",command=lambda: copy_text(False))
edit_menu.add_command(label="Cut   (CTRL+X)  ",command=lambda: cut_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="paste (CTRL+V)  ",command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Delete         ",command=lambda:delete_text())
edit_menu.add_separator()
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
########################
#color menu
color_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="selected text",command=text_color)
color_menu.add_command(label="All text",command=all_text_color)
color_menu.add_command(label="Background",command=bg_color)

#######################
#add status bar to bottom of app
status_bar =Label(root,text='Ready ')
status_bar.pack(fill=X,side=BOTTOM,ipady=5)
##########################
root.bind('<Control-x>',cut_text)
root.bind('<Control-c>',copy_text)
root.bind('<Control-v>',paste_text)
#create button
######bold button
bold_button=Button(toolbar_frame,text="bold",command=bold_it)
bold_button.grid(row=0,column=0,sticky=W,padx=5)
############ italic button
italics_button=Button(toolbar_frame,text="italics",command=italics_it)
italics_button.grid(row=0,column=1,padx=5)
############ italic button
undo_button=Button(toolbar_frame,text="undo",command=undo_it)
undo_button.grid(row=0,column=2,padx=5)
############ italic button
redo_button=Button(toolbar_frame,text="redo",command=redo_it)
redo_button.grid(row=0,column=3,padx=5)
#######################
#text color
color_text_button =Button(toolbar_frame,text="Text Color",command=text_color)
color_text_button.grid(row=0,column=4,padx=5)
root.mainloop()
