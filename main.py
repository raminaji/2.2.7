import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
global command_textbox, url_entry
def do_command(command):
    global command_textbox, url_entr
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    url_val = url_entry.get()
    if (len(url_val) == 0):
          url_val = "::1"
      
      # use url_val 
    if command != 'tracert':
      p = subprocess.Popen(command + ' ' + str(url_val), stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
    else:
      p = subprocess.Popen('ping' + ' ' + str(url_val), stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
      ipfortracer = (str(p.communicate()[0]).split("[")[1].split("]")[0])
      p = subprocess.Popen(command + ' ' + str(ipfortracer), stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

# Save function.
def enterbutton(*args):
  do_command('ping')
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

frame_URL = tk.Frame(root, pady=10,  bg="black")
frame_URL.pack()

url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("times new roman", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="circle",
    fg="blue",
    bg="green")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) 
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black")
frame.pack()
# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()
ping_btn = tk.Button(frame, text="Ping", command=lambda:do_command("ping"))
ping_btn.pack()
ns_btn = tk.Button(frame, text="NsLookup", command=lambda:do_command("nslookup"))
ns_btn.pack()
tr_btn = tk.Button(frame, text="Tracert", command=lambda:do_command("tracert"))
tr_btn.pack()

save_btn = tk.Button(frame, text="Save", command=mSave)
save_btn.pack()

root.bind('<Return>', enterbutton)
root.mainloop()

