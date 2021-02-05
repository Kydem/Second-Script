#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Settings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Tic Tac Toe"
Website = "https://www.twitch.tv/germansausagesarezewurst"
Description = "Starts a game of Tic Tac Toe"
Creator = "GermanSausages"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
Settings_Module = MySettings

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    Log("Init Called")
    EnsureLocalDirectoryExists("settings")

    ScriptSettings = MySettings(SettingsFile)
    Log("Init Ended")
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    Log("Execute Called")
    if not data.IsFromTwitch() or not data.IsChatMessage():
        return
        Log("Execute is Chat message")

    if Settings_Module.Command.lower() in data.IsChatMessage():
        result = Parent.GetDisplayName(data.User)

    Log("Excute Ended")
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

def EnsureLocalDirectoryExists(dirName):
    directory = os.path.join(os.path.dirname(__file__), dirName)
    if not os.path.exists(directory):
        os.makedirs(directory)

def Log(message):
    Parent.Log("TicTacToe", str(message))
    return

def SendMessage(message):
    Parent.SendsStreamMessage(message)
    return
