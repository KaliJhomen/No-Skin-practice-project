import customtkinter as ctk 
from PIL import Image
import classes
main= ctk.CTk()
main.geometry(f"1230x690")
main.resizable(False,False)

def salir():
    main.quit()
def main_menu():
    global main_menu_options
    frame=ctk.CTkFrame(main, width=1230,height=690,fg_color="gray1")
    frame.grid()
    frame.grid_propagate(False)
    title=ctk.CTkLabel(frame, text="NO-SKIN", font=ctk.CTkFont("Pixellari", 150, "bold"), text_color="firebrick1")
    title.place(relx=0.5, rely=0.2, anchor="center")
    main_menu_options= ["New Game", "Close Game"]
    selected_index= 0
    def select_option_menu():
        selected_option= main_menu_options[selected_index]
        if selected_option=="New Game":
            character_select()
        elif selected_option=="Close Game":
            salir()
    new_game_label=ctk.CTkLabel(frame, text="New Game",font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="gray30", fg_color="transparent")
    new_game_label.place(relx=0.5,rely=0.4, anchor="center")    
    close_game_button=ctk.CTkLabel(frame, text="Close Game",font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="gray30", fg_color="transparent")
    close_game_button.place(relx=0.5, rely=0.5, anchor="center")
    
    confirm_label=ctk.CTkLabel(frame, text="Confirm", font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="snow", fg_color="transparent")
    confirm_label.place(relx=0.12, rely=0.92, anchor="center")
    
    z_label=ctk.CTkLabel(frame, text="Z", font=ctk.CTkFont("Pixellari", 30, "bold"), text_color="gray1",fg_color="snow", width=25, height=35)
    z_label.place(relx=0.05, rely=0.92, anchor="center")

def character_select():
    classes.clear_window(main)
    main_frame= ctk.CTkFrame(main, width=1230, height=690, fg_color="gray1")
    main_frame.grid()
    main_frame.grid_propagate= False
    
    choose_your_character=ctk.CTkLabel(main_frame, 250,40,text="Choose your character", font=ctk.CTkFont("Pixellari",30,"bold"))
    choose_your_character.place(relx=0.5,rely=0.05, anchor="center")
    noire_text=ctk.CTkLabel(main_frame, 250,40, text="Noire, the Goddess´s weapon", font=ctk.CTkFont("Pixellari", 30))
    noire_text.place(relx=0.2, rely= 0.2, anchor="center")
    hearts_label=ctk.CTkLabel(main_frame,250,50)
    hearts_label.place(relx=0.2,rely=0.3, anchor="center")
    set_image(hearts_label,"images/heart.png",45,35)
    
    z_label=ctk.CTkLabel(main_frame, text="Z", font=ctk.CTkFont("Pixellari", 30, "bold"), text_color="gray1",fg_color="snow", width=25, height=35)
    z_label.place(relx=0.9, rely=0.9, anchor="center")
    
    next_button=ctk.CTkButton(main_frame, text=">", font=ctk.CTkFont("Pixellari", 45), text_color="snow",fg_color="gray5",corner_radius=15, width=50, height=30)
    next_button.place(relx=0.95, rely=0.5, anchor="center")
    
def choose_location_screen():
    classes.clear_window(main)
    main_frame=ctk.CTkFrame(main, width=1230, height=690, fg_color="gray1")
    main_frame.grid_propagate=False
    main_frame.grid()
    
    choose_location_label=ctk.CTkLabel(main_frame, 250,40, text="Choose the location", font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="orange red")
    choose_location_label.place(relx=0.5, rely=0.1, anchor="center")
    
    next_tab_button=ctk.CTkButton(main_frame, text=">", font=ctk.CTkFont("Pixellari", 30), text_color="snow",fg_color="gray5",corner_radius=15, width=25, height=30)
    next_tab_button.place(relx=0.65, rely=0.1, anchor="center")   

    events_and_probabilities_frame=ctk.CTkFrame(main_frame, 500, height=250, fg_color="snow")
    events_and_probabilities_frame.place(relx=0.55, rely=0.75, anchor="center")
    
    text_label=ctk.CTkLabel(events_and_probabilities_frame, text="Events and their probabilities", font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="orange red")
    text_label.place(relx=0.5, rely=0.1, anchor="center")
#fight
def fight_screen():
    main_frame=ctk.CTkFrame(main, width=1230, height=690, fg_color="gray1")
    main_frame.grid()
    main_frame.grid_propagate=False
    
    enemy_frame=ctk.CTkFrame(main_frame, width=500, height=490, fg_color="gray15")
    enemy_frame.place(relx=0.5, rely=0.35, anchor="center")
    current_enemy_name_label=ctk.CTkLabel(enemy_frame, 100,40,text={classes.current_enemy.name}, font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="orange red")
    current_enemy_name_label.place(relx=0.5, rely=0.1, anchor="center")
   
    
    heart_image= Image.open("images/heart.png")
    heart_image= heart_image.resize((30,25), Image.NEAREST)
    heart_image_ctk= ctk.CTkImage(heart_image, heart_image, (30,25))
    
    empty_heart_image= Image.open("images/empty_heart.png")
    empty_heart_image= empty_heart_image.resize((30,25), Image.NEAREST)
    empty_heart_image_ctk= ctk.CTkImage(empty_heart_image, empty_heart_image, (30,25))
    #player hearts system   
    for i in range(classes.current_player.max_hearts):          
        current_player_hearts_label=ctk.CTkLabel(main_frame, 100, 40, image=heart_image_ctk, text="", anchor="w", fg_color="transparent")
        current_player_hearts_label.place(relx=(0.07+i*0.03), rely=0.15, anchor="center")
    #enemy hearts system
    for i in range(classes.current_enemy.max_hearts):
        current_enemy_hearts_label=ctk.CTkLabel(enemy_frame, 100, 40, text="", image=heart_image_ctk, anchor="w")
        current_enemy_hearts_label.place(relx=(0.5+i*0.075), rely=0.2, anchor="e")
    
    actions_frame=ctk.CTkFrame(main_frame, width=1230, height=200, fg_color="gray7")
    actions_frame.place(relx=0.5,rely=0.85, anchor="center")  
    
    next_action_label=ctk.CTkLabel(actions_frame, text=">", font=ctk.CTkFont("Pixellari", 30), text_color="snow",fg_color="gray5",corner_radius=15, width=25, height=30)
    next_action_label.place(relx=0.35, rely=0.45, anchor="center")    
    
    z_label=ctk.CTkLabel(actions_frame, text="Z", font=ctk.CTkFont("Pixellari", 30, "bold"), text_color="gray1",fg_color="snow", width=25, height=35)
    z_label.place(relx=0.96, rely=0.8, anchor="center")    

    melee_weapon_name_label=ctk.CTkLabel(actions_frame, 100, 50, text={classes.current_player.melee_weapon.weapon_name}, font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="orange red")
    melee_weapon_name_label.place(relx=0.5, rely=0.15, anchor="center")  
    
    melee_weapon_accuracy_label= ctk.CTkLabel(actions_frame, 100, 50, text=f"Accuracy: {classes.current_player.melee_weapon.base_accuracy}", font=ctk.CTkFont("Pixellari", 35, "bold"), text_color="snow")
    melee_weapon_accuracy_label.place(relx=0.54, rely=0.4, anchor="center", )
    
    melee_weapon_damage_label=ctk.CTkLabel(actions_frame, 100, 50, text=f"Damage: {classes.current_player.melee_weapon.base_damage}", font=ctk.CTkFont("Pixellari", 35, "bold"))
    melee_weapon_damage_label.place(relx=0.51, rely=0.6, anchor="center")
def game_over_screen():
    classes.clear_window(main)
    main_frame= ctk.CTkFrame(main, 1230, 690, fg_color="gray1")
    main_frame.grid()
    classes.current_player= None
    classes.current_enemy= None
    
    you_lose=ctk.CTkLabel(main_frame,text="Pendejo", font=ctk.CTkFont("Pixellari", 100))
    you_lose.place(relx=0.5,rely=0.5, anchor="center")
   
        
def set_image(widget, image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.NEAREST)
    photo_image = ctk.CTkImage(light_image=resized_image,
                                dark_image=resized_image,
                                size=(width, height))    
    widget.configure(image=photo_image, text="")
    widget.image = photo_image   
    
def on_key_press(event):
    global selected_index
    if event.keysym=="Up":
        selected_index=(selected_index-1)%len(main_menu_options)
    elif event.keysym=="Down":
        selected_index=(selected_index+1)%len(main_menu_options)
    elif event.keysym=="Return":
        select_option()
    update_menu()

def update():
    for i, option in enumerate(main_menu_options):
        if i==selected_index:
            menu_labels[i].config(bg="blue", fg="white")
        else:
            menu_labels[i].config(bg="white", fg="black")


main_menu()
main.mainloop()
