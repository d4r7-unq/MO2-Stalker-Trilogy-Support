from ..basic_game import BasicGame

class StalkerCoPGame(BasicGame):
    Name = "S.T.A.L.K.E.R.: Call of Pripyat EE Support Plugin"
    Author = "DIGIT4L_RA7EN"
    Version = "0.1"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Call of Pripyat Enhanced Edition."

    GameName = "S.T.A.L.K.E.R.: Call of Pripyat EE"
    GameShortName = "stalkercallofpripyatee"
    GameNexusName = "stalkercallofpripyatee"

    GameBinary = "%GAME_PATH%/xrEngine.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%USERPROFILE%\Saved Games\STALKER Call of Prypiat - EE\STEAM"
    GameIniFiles= "%USERPROFILE%\Saved Games\STALKER Call of Prypiat - EE\STEAM/user.ltx"
    GameSaveExtension = "scop"
    GameSavesDirectory = "%USERPROFILE%\Saved Games\STALKER Call of Prypiat - EE\STEAM/savedgames"

    GameSteamId = 2427430