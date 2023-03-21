# Intéragir en python avec Minecraft Java Edition

Pour Minecraft Java v1.19.3

1 - installer python si ce n'est pas déjà fait, faire la suite dans un terminal en mode admin

2 - installer pip :

```bat
python -m ensurepip --upgrade
```

3 - installer mcpi : 

```bat
pip install mcpi
```

# Minecraft et le reste du bordel :

1 - installer Minecraft Launcher

2 - dans C:\XboxGames\Minecraft Launcher\Content clic droit sur Minecraft.exe -> propriétés -> compatibilité et cocher "Exécuter ce programme en tant qu'utilisateur"

3 - installer Minecraft java

4 - installer java [https://download.oracle.com/java/19/archive/jdk-19.0.2_windows-x64_bin.exe](https://download.oracle.com/java/19/archive/jdk-19.0.2_windows-x64_bin.exe)

5 - si ce n'est pas déjà fait, télécharger le jar du dernier BuildTool de Spigot : [https://hub.spigotmc.org/jenkins/job/BuildTools/lastStableBuild/](https://hub.spigotmc.org/jenkins/job/BuildTools/lastStableBuild/)

6 - mettre le BuildTool dans un dossier qui lui sera propre, et dans ce dossier shift+clic droit -> ouvrir la fenêtre powershell ici et saisir : 

```bat
java -version #pour être sûr que java fonctionne, sinon ajouter java dans le PATH
```

si java fonctionne, saisir :

```bat
java -jar ./BuildTools.jar
```

7 - ça a dû créer tout un tas de fichiers, dont spigot-1.19.3.jar (adapte la version si besoin, patate!). Au même endroit, créer un fichier StartMinecraftServer_1.19.3.bat et l'ouvrir avec vscode. Dedans il faut mettre :

```bat
@echo off
java -Xms512M -Xmx1024M -jar spigot-1.19.3.jar
pause
```

9 - lancer le bat, puis fermer le terminal qui s'est ouvert. Ensuite, dans le fichier eula.txt qui s'est créé, remplacer :
```bat
eula=false
```
par :
```bat
eula=true
```

10 - dans le dossier plugins, télécherger le jar dispo sur [https://dev.bukkit.org/projects/raspberryjuice](https://dev.bukkit.org/projects/raspberryjuice)

11 - relancer le bat (autoriser l'accès au pare-feu si nécessaire) et ne pas fermer le terminal qui s'ouvre

12 - lancer Minecraft Java, et cliquer sur MULTIPLAYER -> Add Server

13 - dans Server Name, mettre ce que vous voulez

14 - dans Server Adress, mettre 127.0.0.1 puisque votre serveur fonctionne en local

15 - valider, et lancer le nouveau serveur (mais pas trop loin)

16 - pour la documentation : [https://github.com/zhuowei/RaspberryJuice](https://github.com/zhuowei/RaspberryJuice)

17 - voir aussi [https://github.com/martinohanlon/mcpi](https://github.com/martinohanlon/mcpi)

---
![](https://cdn.discordapp.com/attachments/932672918859702355/1070964072599781387/image.png)

![](https://cdn.discordapp.com/attachments/932672918859702355/1070961072279916674/image.png)
