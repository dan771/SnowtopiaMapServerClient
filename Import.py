import os

os.system('cmd /c "dotnet DicordChatExporter.CLI\\DiscordChatExporter.Cli.dll export -t "OTYxMTU1NDIzODU0MDA2MzYz.Yk6Cig.uR7t7dWL12ShImi-GrSk_tzFkDA" -c 939905115505180682 -o Chat.txt -f PlainText"')
#Gets a list of all messages from maps-pinboard

with open('Chat.txt', 'r', encoding="utf8") as f:
    lines = f.readlines()

for i in range(19):
    lines.pop(0)
    
lines[0] = '\n'

for i in range(6):
    lines.pop(len(lines)-1)

lines[-1:] = '\n'

with open('Chat.txt', 'w', encoding="utf8") as f:
    lines = f.writelines(lines)

print('Import Sucsessful!')
