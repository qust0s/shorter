import sys
import rich
import banner
import random
import pyshorteners

from config import links
from rich.console import Console
from rich.prompt import Confirm

console = Console()

def Shorter():

    try:
        link = console.input("[bold red]Insert link> ")

    except ValueError:
           console.print("[red]ERROR!")
           
    if not link:
       config = Confirm.ask("[bold red]use link's from config?[/]")

       if not config:
          sys.exit()
               
       else:
            with console.status("Reduction"):
                 shorter = pyshorteners.Shortener()
                 short_link = shorter.tinyurl.short(random.choice(links))

            console.print("[bold green][+] Your Link[/]:", short_link)
            
    else:
         with console.status("Reduction"):
              shorter = pyshorteners.Shortener()
              short_link = shorter.tinyurl.short(link)

         console.print("[bold green][+] Your Link[/]:", short_link)
         
Shorter()          
        
