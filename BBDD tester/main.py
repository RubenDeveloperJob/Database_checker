# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle
import mysql.connector
import paramiko


def check_database_connection(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        conn.close()
        messagebox.showinfo("Estado de la base de datos", "La base de datos está operativa.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos.\nError: {e}")


def check_ssh_connection(host, user, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password, timeout=5)
        ssh.close()
        messagebox.showinfo("Estado de la conexión SSH", "La conexión SSH está establecida.")
    except paramiko.AuthenticationException:
        messagebox.showerror("Error de autenticación", "Error: Fallo de autenticación. Comprueba las credenciales.")
    except paramiko.SSHException as e:
        messagebox.showerror("Error SSH", f"No se pudo establecer la conexión SSH.\nError: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al intentar conectar por SSH.\nError: {e}")


def main():
    root = tk.Tk()
    root.title("Comprobación de la conexión")

    style = ThemedStyle(root)
    style.set_theme("arc")

    frame = ttk.Frame(root, padding="20")
    frame.pack()

    host_label = ttk.Label(frame, text="Host:")
    host_label.grid(row=0, column=0, padx=5, pady=5)

    host_entry = ttk.Entry(frame)
    host_entry.grid(row=0, column=1, padx=5, pady=5)

    user_label = ttk.Label(frame, text="Usuario:")
    user_label.grid(row=1, column=0, padx=5, pady=5)

    user_entry = ttk.Entry(frame)
    user_entry.grid(row=1, column=1, padx=5, pady=5)

    password_label = ttk.Label(frame, text="Contraseña:")
    password_label.grid(row=2, column=0, padx=5, pady=5)

    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    database_label = ttk.Label(frame, text="Base de datos:")
    database_label.grid(row=3, column=0, padx=5, pady=5)

    database_entry = ttk.Entry(frame)
    database_entry.grid(row=3, column=1, padx=5, pady=5)

    query_label = ttk.Label(frame, text="Sentencia SQL:")
    query_label.grid(row=4, column=0, padx=5, pady=5)

    query_entry = ttk.Entry(frame, width=40)
    query_entry.grid(row=4, column=1, padx=5, pady=5)

    result_text = tk.Text(frame, height=10, width=50)
    result_text.grid(row=5, columnspan=2, padx=5, pady=5)

    def check_database():
        host = host_entry.get()
        user = user_entry.get()
        password = password_entry.get()
        database = database_entry.get()

        if not all((host, user, password, database)):
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        check_database_connection(host, user, password, database)

    def check_ssh():
        host = host_entry.get()
        user = user_entry.get()
        password = password_entry.get()

        if not all((host, user, password)):
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        check_ssh_connection(host, user, password)

    def execute_query():
        host = host_entry.get()
        user = user_entry.get()
        password = password_entry.get()
        database = database_entry.get()
        query = query_entry.get()

        if not all((host, user, password, database, query)):
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        # Aquí puedes ejecutar la consulta SQL o cualquier acción que desees realizar

    check_database_button = ttk.Button(frame, text="Comprobar conexión a la base de datos", command=check_database)
    check_database_button.grid(row=6, columnspan=2, pady=5)

    check_ssh_button = ttk.Button(frame, text="Comprobar conexión SSH", command=check_ssh)
    check_ssh_button.grid(row=7, columnspan=2, pady=5)

    execute_button = ttk.Button(frame, text="Ejecutar consulta SQL", command=execute_query)
    execute_button.grid(row=8, columnspan=2, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()


