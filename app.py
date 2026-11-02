import customtkinter as ctk
from cipher import encrypt, decrypt

# Modo oscuro. También posible con light o system
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear ventana de la app
app = ctk.CTk()

app.title("ABD Cipher v1.0")
app.geometry("700x500")
app.resizable(True, True)


# Añadir título
title = ctk.CTkLabel(
    app,
    text="ABD Cipher",
    font=("Impact", 28, "bold")
)
title.pack(pady=(20,10))

# Campo para el mensaje
message_label = ctk.CTkLabel(
    app,
    text="Message",
    font=("Impact",16)
)
message_label.pack(anchor="w", padx=55)

message_box = ctk.CTkTextbox(
    app,
    width=600,
    height=80
)
message_box.pack(padx=50, pady=(5,20))

# Añadir desplazamineto [1-26]
shift_label = ctk.CTkLabel(
    app,
    text="Displacement",
    font=("Impact", 16)
)
shift_label.pack()

shift_entry = ctk.CTkEntry(
    app,
    width=50,
    placeholder_text="1-26"
)
shift_entry.pack(pady=(2, 5))


# Crear funciones para los botones
# Encriptar
def encrypt_message():
    message = message_box.get("1.0", "end-1c")

    # Crear try/except para que no dé error si se introducen letras en "Displacement"
    try:
        shift = int(shift_entry.get())
    except ValueError:
        result_box.delete("1.0", "end")
        result_box.insert("1.0", "Please enter a valid displacement.")
        return

    result = encrypt(message, shift)

    result_box.delete("1.0", "end")
    result_box.insert("1.0", result)

# Desencriptar
def decrypt_message():
    message = message_box.get("1.0", "end-1c")

    try:
        shift = int(shift_entry.get())
    except ValueError:
        result_box.delete("1.0", "end")
        result_box.insert("1.0", "Please enter a valid displacement.")
        return

    result = decrypt(message, shift)

    result_box.delete("1.0", "end")
    result_box.insert("1.0", result)

# Añadir botones
button_frame = ctk.CTkFrame(app, fg_color ="transparent")
button_frame.pack(pady=10)

# Encriptar
encrypt_button = ctk.CTkButton(
    button_frame,
    text="Encrypt",
    command=encrypt_message,
    width=150
)
encrypt_button.grid(row=0, column=0, padx=10)

# Desencriptar
decrypt_button = ctk.CTkButton(
    button_frame,
    text="Decrypt",
    command=decrypt_message,
    width=150,
    fg_color="#B33A3A",
    hover_color="#8C2E2E"
)
decrypt_button.grid(row=0, column=1, padx=10)


# Obtener resultado
result_label = ctk.CTkLabel(
    app,
    text="Result",
    font=("Impact", 16)
)
result_label.pack(anchor="w", padx=55, pady=(10, 5))

result_box = ctk.CTkTextbox(
    app,
    width=600,
    height=60
)
result_box.pack(padx=50)

# Frame para Clear/Copy
bottom_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
bottom_frame.pack(pady=15)

# Botón "Clear"
def clear_fields():
    message_box.delete("1.0", "end")
    shift_entry.delete(0, "end")
    result_box.delete("1.0", "end")

clear_button = ctk.CTkButton(
    bottom_frame,
    text="Clear",
    command=clear_fields,
    width=120,
    fg_color="#444444",
    hover_color="#333333"
)
clear_button.grid(row=0, column=0, padx=8)

# Botón "Copy"
def copy_result():

    result = result_box.get("1.0", "end-1c")

    if not result:
        return

    app.clipboard_clear()
    app.clipboard_append(result)
    app.update()

copy_button = ctk.CTkButton(
    bottom_frame,
    text="Copy",
    command=copy_result,
    width=80
)

copy_button.grid(row=0,column=1, padx=8)

# Créditos
credits_label = ctk.CTkLabel(
    app,
    text="© 08/2026 Adrián GA · ABD Cipher v1.0",
    font=("Arial", 10)
)
credits_label.pack(side="bottom", anchor="e", padx=15, pady=5)

# Ejecutar aplicación
app.mainloop()