import tkinter, customtkinter
import actions

customtkinter.set_default_color_theme("dark-blue")

# To create .exe, run "pyinstaller file_name.py"

class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()
        
        # configure window
        self.title("QATool")
        self.geometry(f"{1100}x{580}")
        
        # root!
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.sidebar_frame = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.sidebar_frame.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # create sidebar frame with widgets
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="QATool", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # UI Scaling
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")
        
        # Quit Button
        self.bt_Quit = customtkinter.CTkButton(self.sidebar_frame, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command= self.close_window)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)
        
        # button to select correct frame IN self.sidebar_frame WIDGET
        self.bt_dashboard = customtkinter.CTkButton(self.sidebar_frame, text="Dashboard", command=self.dash)
        self.bt_dashboard.grid(row=1, column=0, padx=20, pady=10)

        # right side panel, has self.right_dashboard inside it
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
        
        
        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        self.dash() # Initialize to dashboard view

    def dash(self):
        
        self.clear_frame()
        self.logo_label = customtkinter.CTkLabel(self.right_dashboard, text="Dashboard", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self.right_dashboard, width=800)
        self.textbox.grid(row=2, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Dashboard:\n\n" + 
                            "Select a page from the sidebar to the left to see available scripts.\n\n" + 
                            "QA Tool is currently in a development state.")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
    def close_window(self): 
            App.destroy(self)
            
    # Clear all widgets from self.right_dashboard(frame) BEFORE loading those of the new page      
    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()


a = App()
a.mainloop()