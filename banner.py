import rich
import pyfiglet
from rich.console import Console

console = Console()

banner = pyfiglet.figlet_format(text="SHORTER", font="slant")
print(banner)

console.print(
'''
[+] Creator: qust0s.t.me 
[+] GitHub: github.com/qust0s
''', style = "bold white"
)
