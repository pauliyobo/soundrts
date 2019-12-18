Game manual
===========

.. contents::

1. Introduction
---------------

Welcome to SoundRTS!

SoundRTS is a realtime strategy game inspired by Warcraft and Starcraft, but an audiogame, so adapted for the blind.
In this game, you will explore the surroundings, exploit goldmines and woods, build, recruit peasants and soldiers, and fight the enemy!

The game is by default in map mode : you are heading north, and you can select all the object without rotating.
But you can also play in first person mode, nice for exploration and attack.

Windows uses a screen reader (or SAPI 5).
Linux uses Speech Dispatcher.
Mac OS X uses NS Speech Synthesis.
Recorded speech has been totally removed (SoundRTS 1.2 alpha 9).

2. Tutorial
-----------

This tutorial will help you learn the main controls of the game.

2.1 Chapter 1 tutorial
^^^^^^^^^^^^^^^^^^^^^^

If you use Jaws or another screen review, you may have to unactivate it to access to the keyboard.

When the game starts, you'll hear the name of the square where you are: "A1". The presence of a goldmine in A1 is also told. To examine this square, press Tab many times. You will notice that this square has only one exit (a path), a gold mine, a wood, town hall 1 (it's your base), and the peasant 1.

Then press "Page Down" to know if another square can be examined. You'll hear "C1", which contains (press Tab to know that) a farm, a path, a wood and footman 1.

If you press "Page down" again, you will be again in "A1". It means that only 2 squares can be examined now.

Another way of moving in the map is to use the Arrow Keys. This way you can fly over the unknown squares to give the order to go to an unknown square.

The objective of this map is to build 1 farm and 1 barracks. Only the peasant can build. But he needs gold and wood, and a free space (a meadow). To know how much gold, wood, food you have, press Z, X and C.

Let's order the peasant to gather gold. First, to control him, press Q until you hear "peasant 1, awaiting your orders!". Then, press A until you select "exploit" ; then press Tab until you select the gold mine ; then press Enter to confirm. The peasant will start gathering gold.

To go faster you will need more peasants. Press Q until you control the townhall. Then, press A until you select "recruit peasant" then press Enter. After some seconds, a new peasant, peasant 2, will appear.

To ask peasant 2 to gather wood, do like the first one, or, to go faster, press A until you control peasant 2, then press Tab to select the gold mine, then press "Backspace". This key launches the default action on the selected target : here, the default action is "exploit a gold mine".

Before recruiting a third peasant, let's tell the townhall 1 that the newly recruited peasants will have to exploit this gold mine. To do that, press Q until you control townhall 1. Then press Tab until you select the gold mine. Finally, press "Backspace" to give the default order to the townhall : "rally to a gold mine". Then press A to choose "recruit peasant", then press Enter to confirm.

When you have enough gold or when the gold mine is exhausted, press D to control all the peasants then press Tab until you select the wood. Then press "Backspace" to launch the exploitation of the gold mine.

The rest is not difficult.

2.2 Chapter 2 tutorial
^^^^^^^^^^^^^^^^^^^^^^

Hint : group your combat units. To do this, control them (with the S key) and make them patrol between the squares you want to protect.

2.3 Hints and tips
^^^^^^^^^^^^^^^^^^

- Keep your forces focused.
- Make you soldiers patrol. Patrolling soldiers can protect a larger zone while keeping the forces focused.
- Use rally points for buildings. The buildings that can recruit units can define a rally point. The new units will target this rally point. For example a new peasant will exploit a gold mine.
- Use the defensive mode to scout. A unit in defensive mode will flee if it encouters strongers enemies. This way you can know how many enemies are in a square without sacrificing the scouting unit. The peasants are in defensive mode by default but the soldiers can be put in this mode too.
- A fleeing unit forgets its orders. For example, a peasant who is gathering gold won't go back to work after fleeing, while if he fought and survived he would have went on gathering gold.

3. Commands list
----------------

The game consists in giving orders to your units and buildings. To give an order to a unit, you must control it first.
If you press F10 during the game, you will go to the game menu.
If you use Jaws or another screen review, you may have to unactivate it to access to the keyboard.

Moving on the map
^^^^^^^^^^^^^^^^^

The arrow keys make you move from a square to another square in the map. If a direct path exists between the current square and the new square, you will hear a noise depending on the type of the path (path or bridge). If no direct path exists, you will hear a collision noise and you will stay at the same square (press control + arrow keys to fly above an obstacle). If you don't know yet if a path exists (unknown square) then no noise will be heard.

Press shift + arrow keys to move several squares at a time.

Another way to move on the map is to press Page Up, which will lead you to the next interesting square without passing by empty squares. Since SoundRTS 1.1 alpha 3, some variants are available:

- press Alt + PageUp/PageDown to select the previous/next unknown square
- press Shift + PageUp/PageDown to select the Previous/Next Square containing resources

When you control a unit and you press Space, you will automatically follow it when it moves from one square to another one.

Choosing a unit to control
^^^^^^^^^^^^^^^^^^^^^^^^^^

To control the next local unit, press Q.

To control the next building, press W.
To control the next peasant, press E. To control all the local peasants, press D.
To control the next idle peasant, press Alt E. To control all the local idle peasants, press Alt D.
To control the next footman, press R. To control all the local footmen, press F.
To control the next archer, press T. To control all the local archers, press G.
To control the next knight, press Y. To control all the local knights, press H.
To control the next catapult, press U. To control all the local catapults, press J.
To control the next dragon, press I. To control all the local dragons, press K.
To control the next mage, press O. To control all the local mages, press L.

When a key makes you control the next unit, the same key combined with Shift makes you control the previous unit. For example, to control the previous peasant, press Shift + E.

To control all the units of the same type and in the same square than the current unit, press 1.
To control only half or third, press 2 or 3.
To stop controlling a group, press 0.

To control all the local soldiers, press S.
To control all the soldiers and the pesants, press Alt + S.

When a key makes you control a group of local units, the same key combined with control makes you control a group from all the map. For example, to control all the footment, press Control + R or Control + F.

Giving an order: main method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To give an order to a controlled unit, the main method consists in choosing the order in a list and selecting the target if the action requires it.

To choose the order in a list, press A (and Shift A) to select the order.

If you must select a target, press Tab (and Shift Tab) to select the target. To select a remote square as a target, use the arrow keys.

Press Enter to confirm your choice.

Giving an order: alternate, faster method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A second method to give an order consists in selecting the target with Tab (or the arrow keys) and then pressing Backspace. The default order will be given. For example, a peasant targetting a gold mine will exploit it if you press Backspace.

Giving an order: using shortcuts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To give an order with a shortcut, press Alt + A. A message will tell the list of available shortcuts for the currently controlled unit.
Press the shortcut and the order will be executed immediately, unless a target needs to be selected.

Examining the situation
^^^^^^^^^^^^^^^^^^^^^^^

To check the controlled unit (or the controlled group), press Space. Moreover, you will move to the square occupied by the unit (or the group leader).

To know how much gold you have, press Z. Press X for wood, press C for food.

To know the health of the current unit press V.

To examine again an object selected with Tab, press Control.

Giving an order without cancelling the previous ones (queuing commands)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hold down Shift before pressing Enter to confirm the order.

It also works for default orders: hold down Shift before pressing Backspace.

Press Space to check if the unit have several orders to execute.

Here are some situations where queuing commands would be useful:

- Example 1: you want a peasant to scout every starting square in the map (to know where the enemy is). Control the peasant, move the cursor to a starting square, then press Shift + Backspace. Repeat for each starting square.
- Example 2: you want a peasant to exploit several resources. Target a resource, press Shift + Backspace. Repeat. When a resource is exhausted, the peasant will exploit the next one.

Giving an imperative order
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you hold down Control before pressing Enter or Backspace, the order will be imperative.

Units with an imperative order will tend to ignore anything not directly related to the order. If they have to go somewhere and they come across enemy units, they will simply ignore them. This is dangerous most of the time but can be useful in some cases, for example to focus on a very important target.

Here are some situations where an imperative command would be useful:

- Example 1: you want your units to attack a specific enemy building or unit and ignore the rest. Select the target and press Control + Backspace.
- Example 2: you want your units to retreat from a place and ignore the enemy units. Select another square and press Control + Backspace.

You can queue imperative commands too. Hold down Control + Shift instead of Shift. 

Attacking a friendly unit
^^^^^^^^^^^^^^^^^^^^^^^^^

Target the unit and press Shift Backspace: the units will attack the target.

Exception: if the target is a damaged building (or a repairable unit like a catapult) and you are controlling workers, they will repair the target.

Blocking an exit
^^^^^^^^^^^^^^^^

New in 1.2 alpha 10.

To block an exit (path, bridge), you can either:

- order a unit (or several units) to block the path (give the "block" order or use back space with the exit as a target);
- build a wall on it;
- build any building on it.

A unit or a gate will let friendly units pass.

Zoom mode (experimental)
^^^^^^^^^^^^^^^^^^^^^^^^

New in 1.2 alpha 10.

F8: enter or exit zoom mode. Escape exits zoom mode too.

The square in divided in 3 x 3 smaller squares. A zoomed square can be used as a target for an order (go to, essentially).

Recallable control groups
^^^^^^^^^^^^^^^^^^^^^^^^^

New in 1.2 alpha 10.

Control + 6, 7, 8 or 9: sets group 6, 7, 8 or 9 with the currently controlled units

Shift + 6, 7, 8 or 9: extends group 6, 7, 8 or 9 with the currently controlled units

6, 7, 8 or 9: recalls group 6, 7, 8 or 9 

In the menus
^^^^^^^^^^^^

The arrow keys work too : Up and Down to select, Right to confirm, Left to cancel.

Press any letter to select the next item starting with this letter.
Press shift + any letter to select the previous item starting with this letter.

Other commands
^^^^^^^^^^^^^^

F5 and F6: previous/next message in the history.
Alt: interrupt the current sentence.

To quit a game or access to the game menu, press F10. Alt F4 and Control C do the same.

Control + Space: make the game go in first person mode. Escape: go back to map mode.

Home/End, +/- of the numeric keyboard: increase/decrease the general sound volume.
Control Home/End, control +/- of the numeric keyboard: increase/decrease the voice relative volume.

F3: say time
Control F3: minute bell on/off (off by default)

Control + Tab selects only woods, gold mines, meadows, and repairable or buildable targets (damaged buildings, building sites, damaged catapults...).

Alt + R reselects the previously given order. Useful to train the same unit or build the same type of building several times.
Alt + G reselects the previously given order and validate it if no additional parameter is required. For example, to train 5 additional archers, press Alt + G 5 times.
Since SoundRTS 1.1 alpha 3, Alt + A is the same than Alt + G.

Backquote (the key below Escape): console command (only in single player mode). The only useful commands at the moment are add_units (to get units or buildings instantly) and victory (to win, for example to skip a chapter). Example of a "add_units" command: "add_units a1 100 archer". New in SoundRTS 1.2 alpha 9.

4. Multiplayer games
--------------------

4.1 Starting a multiplayer game
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select "multiplayer game", then "choose a server in a list".

In a public server, you will be able to organize a game.

Tip: when you are waiting for players online, you can launch SoundRTS a second time and play locally in single player mode. When a player shows up, press F10 to pause your local game and start playing online.

4.2 Chatting
^^^^^^^^^^^^

You can chat in the server lobby, in the pre-game room, and during the game. The organizer of the game is temporarily unavailable during the selection of the map and of the game speed though.

To say something to everybody in the same room or game, press F7, type your message, and press enter.

Another option is to use Skype (or any similar software) if you know the other players.

4.3 Team play
^^^^^^^^^^^^^

The teams must be created before the game starts. They can't be changed during the game.

Allied players share the knowledge of the map, the victory, the upgrades (new in SoundRTS 1.2 alpha 9), and their units can help each other. A worker can use an allied warehouse to store a resource (the resource will still be added to the worker's army).

In a server game, the computers are not allied by default.

Note: In a single player game from the "single player" menu, the computers are allied.

Tip: to play a single player game with a computer as an ally, launch a private server.

4.4 How to make your server accessible to other players
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To check if your server is accessible from outside your local network, wait for a player to connect, or ideally ask a friend to connect from outside. As a last resort, you can also use a port forwarding tester website (google "port forwarding tester" for example). Be cautious: I can't guarantee that this kind of website isn't malicious! The web site shouldn't require you to install a tool, for example.

In most cases you will have to configure your router to forward incoming TCP connections through port 2500 to the local IP address of your server.

You might also have to configure DHCP in the router to make sure that your server have always the same local IP address.

If you are behind a firewall, you might have to make sure that incoming TCP connections through port 2500 are allowed.

About standalone servers: even if your standalone server is accessible from outside, you might not be able to connect to it from your local network using "choose a server in a list". "Enter the IP address of the server" works in most cases, but it doesn't mean that the server is accessible from outside.

4.5 How to download a map from a server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play a game with the map that you wish to download. Just before the game starts, the map will appear in the `temporary folder`_ and will stay there until another map overwrites it. Depending on the map format, it will be a text file called recent_map.txt or a folder called recent_map.

5. Game elements
----------------

Food
^^^^

The training of a new unit can only happen if the player have enough food rations. If some farms are destroyed or new units are obtained without training, and the food rations become insufficient, the current units will be kept without any problem. No further training will be allowed though.

Tech upgrades
^^^^^^^^^^^^^

The upgrades apply to all the player's units, current and future.

Flying units
^^^^^^^^^^^^

Since SoundRTS 1.1, flying units fly straight to the objective, ignoring the land path.

Invisible units and detectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To defend against an invisible unit, there are at least 3 ways:

- bring a detector unit (or use a detector spell) and attack the unit
- use an area of effect destruction spell on the square containing the unit
- ignore the invisible unit and destroy all the enemy buildings quickly enough

6. More details for customization
---------------------------------

SoundRTS.ini
^^^^^^^^^^^^

This file is located in the `User folder`_ . It contains various parameters about how the game works. When SoundRTS starts, if SoundRTS.ini contains an error, a new file will be generated with as many parameters as possible recovered from the corrupted file. 

Command-line options
^^^^^^^^^^^^^^^^^^^^

From the command-line, the -h option gives the list of available options.

The --mods option overrides the "mods =" line from SoundRTS.ini_ . For example, to start SoundRTS with the soundpack mod and the orc mod: soundrts.exe --mods=soundpack,orc

Sound pack
^^^^^^^^^^

SoundRTS comes with a mod called "soundpack" containing alternative sounds. To activate this mod, in SoundRTS.ini_ replace the "mods =" line with "mods = soundpack". Then restart the game.

SAPI 5 (Windows)
^^^^^^^^^^^^^^^^

In `Soundrts.ini`_, if "srapi = 0", the default SAPI 5 voice will be used directly.

Windows srapi parameter
^^^^^^^^^^^^^^^^^^^^^^^

In `Soundrts.ini`_, use "srapi = 1" to use a screen reader (through ScreenReaderAPI).

Windows srapi_wait parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since I couldn't find a way to know when a screen reader stops talking on Windows, I had to evaluate the duration of a message.
An additional parameter called "srapi_wait" determines how long SoundRTS will wait before sending the next message.
With "srapi_wait = .1" and a message of 10 characters, SoundRTS will wait for .1 * 10 = 1 second.

Increase the value of srapi_wait if some messages are interrupted by the next one.
Decrease the value of srapi_wait if the silence between two messages is too long.


Temporary folder
^^^^^^^^^^^^^^^^

The temporary folder contains the logs and the previously played map.

The temporary folder is located in the `user folder`_ as a folder called "tmp".

User folder
^^^^^^^^^^^

The user folder contains the game settings, the custom maps and mods, and the temporary folder.
An easy way to find the user folder is to open it from the options menu.

If the main folder contains a folder called "user", this folder will be the user folder.
If the "user" folder doesn't exist, the user folder will be located depending on the operating system:

- Windows XP: "C:\\Documents and settings\\your_user_name\\Application data\\SoundRTS unstable"
- Linux: "home/your_user_name/.SoundRTS unstable"

How to create a portable version of SoundRTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since SoundRTS 1.0 beta 10 p, it's possible to have all the game files (log, configuration, custom maps...) stored in the game folder. Here is how to proceed:

- install SoundRTS
- Windows: copy the `game folder` from "Program files" to a writable folder (the desktop, a USB drive, etc)
- In the new SoundRTS folder, create a folder called "user". "user" can be a copy of an existing `user folder`_ (the version must be the same, though).
- Windows: to launch the program, execute "soundrts.exe".

How to change the default speed in single player games
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Find SoundRTS.ini_ in the `user folder`_ and modify the "speed = ..." line. Use an integer number.

Changing some key bindings
^^^^^^^^^^^^^^^^^^^^^^^^^^

Since SoundRTS 1.1, the keyboard layout is defined in a file called bindings.txt located in the `game folder`.

Creating an app for Mac
^^^^^^^^^^^^^^^^^^^^^^^

If you have managed to install the multiplatform version for the Mac, maybe you can create an app to ease the installation for other players.
Here are some hints. Use py2app.
You don't need the source. For example, create a file called soundrts_launcher.py containing this only line: "import soundrts".
You can also create a file called server_launcher.py with the line: "import server".
Make sure that running "python soundrts_launcher.py" actually works.

Using the Windows installer with a limited account (Windows XP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use a limited Windows XP account to install SoundRTS. Just choose another folder than the "program files" folder.

Even if you install SoundRTS with an administrator account, you can play using a limited account.

What makes a map an official multiplayer map?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Official multiplayer maps don't have any sound played before their title. The official multiplayer maps are listed in cfg/official_maps.txt 
with checksums to make sure that they haven't been modified.

How to select a different language?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If cfg/language.txt is empty, the program will select automatically the system's language.
To select a specific language, enter the language code in cfg/language.txt, for example "en", "fr-ca", "pt" or "pt-BR".
Check the res folder to find which language codes are provided.

7. Credits
----------

Note: the following list is not exhaustive. Thanks to all who helped!

This game was written by SoundMUD (soundmud@gmail.com).

Discovery of the French-speaking community of the audio accessible games, and starting ideas: Sabine Gorecki.
Numerous tests and encouragings during the first period of SoundMUD: Alex.
First test of SoundMUD with Linux: Miguel.
Relaunch of SoundMUD project, encouragings during the second period of SoundMUD to bring the strategy game to completion, and very numerous tests: Louis-Rock Lampron et Martin Morin.

English translation: SoundMUD.
German translation: Alexander Westphal from Gameport.
Italian translation: Gabriel Battaglia.
Spanish translation: Alan.

Improvement of the English voice and sounds: Bryan Smart.

Multiplayer map 101 - frontier: Bryan Smart.